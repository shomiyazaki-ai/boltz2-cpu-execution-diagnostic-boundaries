"""Offline, read-only saved-record verification. No historical experiment runs.

MIT License, Copyright (c) 2026 Sho Miyazaki; see ../LICENSE.
Python 3.10+; standard library only. Output is JSON on stdout.
"""
import csv
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT=Path(__file__).resolve().parents[1]
CHECKS=[]

def check(name,condition,scope='public bytes / saved-record consistency'):
    CHECKS.append({'check':name,'status':'PASS' if condition else 'FAIL','scope':scope})

def load(name):
    return json.loads((ROOT/name).read_text(encoding='utf-8'))

def rows(name):
    with (ROOT/name).open(encoding='utf-8',newline='') as f:
        return list(csv.DictReader(f))

def events(name):
    return [json.loads(l) for l in (ROOT/name).read_text(encoding='utf-8').splitlines() if l.strip()]

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def visible_files():
    return {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file() and not any(x in ('.git','__pycache__') for x in p.relative_to(ROOT).parts) and p.suffix!='.pyc'}

def verify():
    listed={}
    for line in (ROOT/'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines():
        h,n=line.split('  ',1)
        if n in listed or re.fullmatch('[0-9a-f]{64}',h) is None:
            raise ValueError('Invalid or duplicate checksum entry')
        p=(ROOT/n).resolve()
        if ROOT not in p.parents:
            raise ValueError('Checksum path escapes root')
        listed[n]=h
    check('checksum exact coverage',set(listed)==visible_files()-{'SHA256SUMS.txt'})
    check('checksum byte identity',all((ROOT/n).is_file() and digest(ROOT/n)==h for n,h in listed.items()))
    mf=rows('docs/EVIDENCE_MANIFEST.csv')
    check('manifest public hashes',all((ROOT/m['public_path']).is_file() and digest(ROOT/m['public_path'])==m['public_sha256'] for m in mf))
    check('manifest exact evidence coverage',{m['public_path'] for m in mf}=={p for p in visible_files() if p.startswith('evidence/')})
    cross=rows('data/table3_claim_evidence_crosswalk.csv')
    check('ten claim records',{x['claim_id'] for x in cross}=={f'CD{i:02d}' for i in range(1,11)})
    check('claim links resolve',all((ROOT/p).exists() for c in cross for p in c['public_evidence_path'].split(';')))
    check('each claim has selected source identity',all(any(c['claim_id'] in m['claim_ids'].split(';') for m in mf) for c in cross))

    projection=rows('data/memory_samples_curated.csv')
    table=rows('data/execution_summary.csv')
    expected=load('verification/expected_results.json')
    check('expected execution table rows',[dict(x) for x in table]==[{k:str(v) for k,v in r.items()} for r in expected['executions']])
    for run,n,last_t,commit,avail,rss,private in [('standard',271,46.75,.45690,2.22477,8515.270,10881.168),('chunking',305,53.0,.38760,1.87646,8678.559,10875.980)]:
        mem=load(f'evidence/cpu_run_records/{run}_memory.json')
        report=load(f'evidence/cpu_run_records/{run}_report.json')
        cfg=load(f'evidence/cpu_run_records/{run}_config.json')
        data=[x for x in projection if x['execution']==run]
        check(run+' sample count',len(mem)==len(data)==n==report['monitor_samples'])
        check(run+' sample time order',all(a['elapsed_s']<b['elapsed_s'] for a,b in zip(mem,mem[1:])))
        fields={'elapsed_s':'elapsed_s','stage':'stage','system_commit_headroom_gib':'commit_headroom_gib','available_physical_ram_gib':'available_gib'}
        match=all(all(str(s[mk])==d[dk] for dk,mk in fields.items()) and d['sample_index']==str(i) and d['process_tree_rss_mib']==str(s['tree']['rss_sum_mib']) and d['process_tree_private_bytes_mib']==str(s['tree']['private_sum_mib']) for i,(s,d) in enumerate(zip(mem,data)))
        check(run+' all sample CSV projections',match)
        numeric_sums=all(abs(sum(Decimal(str(p['rss_mib'])) for p in s['tree']['processes'])-Decimal(str(s['tree']['rss_sum_mib'])))<=Decimal('.002') and abs(sum(Decimal(str(p['private_mib'])) for p in s['tree']['processes'])-Decimal(str(s['tree']['private_sum_mib'])))<=Decimal('.002') for s in mem)
        check(run+' process tree numeric sums (rounding tolerance 0.002 MiB)',numeric_sums)
        last=mem[-1]
        check(run+' terminal values',(last['elapsed_s'],last['commit_headroom_gib'],last['available_gib'],last['tree']['rss_sum_mib'],last['tree']['private_sum_mib'])==(last_t,commit,avail,rss,private))
        check(run+' first sampled commit STOP breach',[i for i,s in enumerate(mem) if s['commit_headroom_gib']<2]==[n-1])
        check(run+' MEMORY_STOP and no success',report['reason']=='MEMORY_STOP' and report['prediction_success'] is False and report['output_qc_status']=='NOT_RUN' and 'TRAINER_PREDICT_RETURNED' not in [x['event'] for x in report['events']],'historical report inspection; no original-PC output census')
        check(run+' polling guard not hard cap',report['memory_guard_os_hard_limit'] is False)
        check(run+' frozen config',all(cfg[k]==v for k,v in {'precision':'32-true','seed':101,'sampling_steps':200,'recycling_steps':3,'diffusion_samples':1,'step_scale':1.5,'msa_cap':4096}.items()))
        st=next(t for t in table if t['execution']==run)
        check(run+' summary against records',int(st['monitor_samples'])==len(mem) and float(st['gate_b_commit_headroom_gib'])==report['gate_b']['commit_headroom_gib'] and float(st['terminal_commit_headroom_gib'])==last['commit_headroom_gib'] and st['stop_event_elapsed_s']=='NOT_RECORDED')
    env=load('data/frozen_environment.json')
    msa=load('evidence/cpu_run_records/msa_dataset_qc.json')
    rescue=load('evidence/cpu_run_records/msa_rescue_qc.json')
    check('MSA shape and denominators',msa['real_dataset']['seed_a']['msa']['shape']==env['combined_prediction_dataset_msa_shape']==[6634,263] and rescue['chains']['A']['raw_rows']==8116 and rescue['chains']['B']['raw_rows']==7149 and env['per_chain_preprocessing_cap']==4096 and next(c for c in msa['caps'] if c['cap']==4096)['fully_paired_rows']==env['fully_paired_rows']==2539)

    isolated=rows('data/isolated_test_summary.csv')
    child_paths=sorted((ROOT/'evidence/isolated_operator_tests/step3').glob('*.json'))
    child=[json.loads(p.read_text(encoding='utf-8')) for p in child_paths]
    check('Step 3 saved child records',len(child)==16 and all(j['status']=='COMPLETE' and j['checkpoint_loaded'] is False and j['predict_called'] is False and j['check']==0 for j in child))
    check('Step 3 summary end RSS',[float(x['rss_end_mib']) for x in isolated if x['test_level']=='Step 3 isolated operator']==[j['rss_end_mib'] for j in child])
    check('Step 3 no claimed operator peak',all('peak_sampled_rss_mib' not in j for j in child))
    step=load('evidence/isolated_operator_tests/step4_results.json')
    check('Step 4 six saved numeric flags',len(step['numerics'])==6 and all(all(j[k] is True for k in ['shape_equal','finite','allclose_1e-5','rng_std_unchanged','rng_chunk_unchanged']) for j in step['numerics']) and step['checkpoint_loaded'] is False and step['prediction_performed'] is False,'saved flags only; no tensor numerical rerun')
    probes=step['patch_integration']['probes']
    check('Step 4 three saved probes',len(probes)==3 and all(j['pass'] for j in probes) and [j['token_count'] for j in probes]==[64,263,385] and probes[1]['capture']['chunk_transition_msa']==32 and probes[1]['capture']['chunk_outer_product']==4)
    check('Step 4 summary matches stored max_abs',[float(x['max_abs']) for x in isolated if x['test_level']=='Step 4 test-only weights']==[j['max_abs'] for j in step['numerics']])
    chunk=load('evidence/cpu_run_records/chunking_report.json')
    names=[x['event'] for x in chunk['events']]
    check('adapter applied before recorded model load',names.index('CHUNK_PATCH_APPLIED')<names.index('MODEL_LOADED_WAITING_FOR_GATE_B'))

    trace=events('evidence/diagnostic_tests/synthetic_events.jsonl')
    stack=[];balanced=True
    for t in trace:
        if t['phase']=='enter':stack.append(t['name'])
        if t['phase']=='exit':
            if not stack or stack.pop()!=t['name']:balanced=False
    check('synthetic completed event contract',len(trace)==26 and [x['seq'] for x in trace]==list(range(26)) and trace[-1]['name']=='TRACE_COMPLETE' and balanced and not stack and sum(x['name']=='MSAModule' and x['phase']=='enter' for x in trace)==4 and sum(x['name']=='PairformerModule' and x['phase']=='enter' for x in trace)==4,'synthetic saved trace; no real-model event claim')
    exc=events('evidence/diagnostic_tests/exception_events.jsonl'); abrupt=events('evidence/diagnostic_tests/abrupt_trace.jsonl')
    check('incomplete traces not success',exc[-1]['name']=='TRACE_INCOMPLETE' and all(x['name']!='TRACE_COMPLETE' for x in exc+abrupt) and len(abrupt)==1 and abrupt[0]['phase']=='enter')

    final=load('evidence/diagnostic_tests/s3_final_summary.json')
    expected_last={'normal':('NORMAL_COMPLETE',0),'overlimit':('MEMORY_ERROR_OBSERVED',42),'exception':('WORKER_EXCEPTION',1),'unlimited':('NORMAL_COMPLETE',0)}
    for case,(last,code) in expected_last.items():
        c=final['cases'][case];log=events(f'evidence/diagnostic_tests/s3_final/{case}/events.jsonl');done=load(f'evidence/diagnostic_tests/s3_final/{case}/completed.json');setup=load(f'evidence/diagnostic_tests/s3_final/{case}/setup.json')
        check('final S3 '+case+' event/exit/readback',c['pass'] and c['last_event']==log[-1]['event']==last and c['completed']['worker_exitcode']==done['worker_exitcode']==code and c['setup']==setup and c['completed']==done and setup['membership_confirmed'] and setup['assignment_before_resume'],'historical Windows small-worker record only')
    check('final S3 96 MiB cap',all(final['cases'][x]['setup']['cap_bytes']==100663296 and final['cases'][x]['setup']['readback']['job_memory_limit_bytes']==100663296 for x in ['normal','overlimit','exception','parent_kill']))
    peak=final['cases']['overlimit']['completed']['readback_after']['peak_job_memory_used_bytes']
    check('overlimit counter caveat preserved',peak==101978112 and peak>100663296)
    check('final S3 parent cleanup observation',final['cases']['parent_kill']['child_gone_after_parent_kill'] is True and final['cases']['parent_kill']['controller_exit']==1,'saved assertion; not dynamically re-executed')
    old=load('evidence/diagnostic_tests/s3_superseded_summary.json')
    check('old S3 contradiction retained',all(old['cases'][x]['pass'] and old['cases'][x]['last_event']=='WORKER_EXCEPTION' and old['cases'][x]['completed']['worker_exitcode']==0 for x in ['normal','unlimited']))
    check('Step 6 contradictory child exit retained',load('evidence/diagnostic_tests/step6_job_summary.json')['results']['normal']['pass'] and load('evidence/diagnostic_tests/step6_normal_parent_done.json')['child_exitcode']==1)
    check('B1 final saved decision',load('evidence/stop_decisions/b1_decision.json')['decision']=='NO_GO_TO_B2_UNDER_FIXED_STOP_RULE','decision inspection; not universal infeasibility proof')
    fig=load('figures/figure1_states.json')
    check('figure state boundaries',fig['real_inference']['standard']==fig['real_inference']['official_chunking']=='MEMORY_STOP' and fig['real_model_stage_diagnostics']=='NOT RUN' and fig['final_decision']=='NO-GO / research STOP' and fig['independent_scientific_MSC']=='NOT ESTABLISHED' and fig['isolated_tests']['step3_cases']==len(child) and fig['isolated_tests']['step4_numeric_checks']==len(step['numerics']) and fig['isolated_tests']['step4_branch_probes']==len(probes) and fig['windows_small_workers']['cap_bytes']==100663296)
    readme=(ROOT/'README.md').read_text(encoding='utf-8')
    check('README twelve main sections',len(re.findall(r'^## \d+\.',readme,re.M))==12)
    broken=[]
    for md in ROOT.rglob('*.md'):
        text=md.read_text(encoding='utf-8')
        for link in re.findall(r'\]\(([^)]+)\)',text):
            if link.startswith(('https://','http://','#','mailto:')):continue
            if not (md.parent/link.split('#',1)[0]).exists():broken.append(str(md.relative_to(ROOT))+':'+link)
    check('Markdown relative file links',not broken)
    check('figure source uses samples without interpolated lines','ax.scatter(xx,yy' in (ROOT/'figures/make_figures.py').read_text(encoding='utf-8') and 'ax.plot(xx,yy' not in (ROOT/'figures/make_figures.py').read_text(encoding='utf-8'),'static source/data consistency; no independent pixel regeneration')

def main():
    try:verify()
    except (OSError,ValueError,KeyError,IndexError,StopIteration,TypeError) as exc:
        CHECKS.append({'check':'verification completed without missing/malformed evidence','status':'FAIL','detail':str(exc)})
    ok=all(x['status']=='PASS' for x in CHECKS)
    print(json.dumps({'status':'PASS WITH EXPLICIT LIMITATIONS' if ok else 'FAIL','checks':CHECKS,'not_run':['historical Windows execution','Boltz inference','checkpoint/sequence input regeneration','tensor allclose/RNG recomputation','real-model stage diagnostics','Zenodo/GitHub publication'],'scientific_MSC':'NOT ESTABLISHED'},indent=2))
    return 0 if ok else 1

if __name__=='__main__':sys.exit(main())
