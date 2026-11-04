"""Rebuild the two record figures from shipped data; never execute the study.

MIT, Copyright (c) 2026 Sho Miyazaki. Requires matplotlib only.
An explicit external output directory is required to protect the frozen payload.
"""
import argparse
import csv
import json
from pathlib import Path

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir',required=True,type=Path)
    args=parser.parse_args()
    root=Path(__file__).resolve().parents[1]
    dest=args.output_dir.resolve()
    if dest==root or root in dest.parents:
        parser.error('Choose an output directory outside the frozen repository.')
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'none','axes.spines.top':False,'axes.spines.right':False,'savefig.facecolor':'white','svg.hashsalt':'C01_CD_v1.0.0'})
    dest.mkdir(parents=True,exist_ok=True)
    state=json.loads((root/'figures/figure1_states.json').read_text())
    fig,ax=plt.subplots(figsize=(12.4,7.5));ax.set_xlim(0,12.4);ax.set_ylim(0,7.5);ax.axis('off')
    colors={'real':('#EAF1F7','#376281'),'limited':('#EDF4F2','#3C6E60'),'unrun':('#F2F2F2','#74787C'),'stop':('#FFF0DB','#A56920')}
    ax.text(.35,7.1,'Evidence and execution boundaries',fontsize=20,fontweight='bold',color='#17394D')
    ax.text(.35,6.72,'Frozen Windows 11 · CPU only · ~16 GiB RAM · Boltz-2 v2.2.1',fontsize=12,color='#53646C')
    def box(x,y,w,h,title,body,typ):
        bg,edge=colors[typ];ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.07,rounding_size=0.12',linewidth=1.3,edgecolor=edge,facecolor=bg))
        ax.text(x+.2,y+h-.34,title,fontweight='bold',fontsize=12,color=edge,va='center')
        ax.text(x+.2,y+h-.68,body,fontsize=11,color='#243A43',va='top',linespacing=1.5)
    box(.4,4.86,5.55,1.35,'Real inference · standard',state['real_inference']['standard']+'\nNo final structure or confidence', 'real')
    box(6.45,4.86,5.55,1.35,'Real inference · chunking enabled',state['real_inference']['official_chunking']+'\nNo final structure or confidence', 'real')
    ax.text(.4,4.4,'Separate limited checks — historical observations, no real-model promotion',fontsize=12,fontweight='bold',color='#3C6E60')
    iso=state['isolated_tests']
    box(.4,2.66,3.66,1.44,'Isolated operators',f"Step 3: {iso['step3_cases']} COMPLETE\nStep 4: {iso['step4_numeric_checks']} numeric / {iso['step4_branch_probes']} probes\nStep 4 uses test-only weights", 'limited')
    box(4.55,2.66,3.45,1.44,'Synthetic tracing','Complete / exception / abrupt\nEvent-contract checks\nSynthetic modules', 'limited')
    cap_mib=state['windows_small_workers']['cap_bytes']//(1024**2)
    box(8.5,2.66,3.5,1.44,'Windows small workers',f'Final S3 v1.2: {cap_mib} MiB cap\nNormal / denial / cleanup\nNo full-model safety proof','limited')
    box(.4,.65,5.55,1.24,'Real-model stage diagnostics',state['real_model_stage_diagnostics']+' (internal diagnostic ③-C)','unrun')
    box(6.45,.65,5.55,1.24,'Final feasibility decision',state['final_decision']+' (B1)\nIndependent scientific MSC not established','stop')
    # The dashed relation is a decision boundary, not a successful execution path.
    ax.add_patch(FancyArrowPatch((6.45,1.26),(5.98,1.26),arrowstyle='-|>',mutation_scale=13,linewidth=1.4,color='#A56920',linestyle='--'))
    ax.text(.4,.14,'Evidence map, not a timeline. Small-test PASS does not establish real-model completion, improvement or safety.',fontsize=10.5,color='#53646C')
    fig.subplots_adjust(0,0,1,1)
    fig.savefig(dest/'figure1_evidence_boundary.svg',metadata={'Date':None})
    fig.savefig(dest/'figure1_evidence_boundary.png',dpi=180,metadata={'Software':'C01 CD figure source'})
    plt.close(fig)

    with (root/'data/memory_samples_curated.csv').open(newline='',encoding='utf-8') as f:rows=list(csv.DictReader(f))
    fig,axs=plt.subplots(1,2,figsize=(12.4,5.3),sharex=True,sharey=True)
    for ax,run,panel,color in zip(axs,['standard','chunking'],['A','B'],['#286487','#438270']):
        data=[r for r in rows if r['execution']==run]
        xx=[float(r['elapsed_s']) for r in data]; yy=[float(r['system_commit_headroom_gib']) for r in data]
        # Individual observations only: no connecting/interpolated line.
        ax.scatter(xx,yy,s=8,color=color,alpha=.86,linewidths=0,zorder=3)
        ax.axhline(2,color='#AC6A1D',linestyle=(0,(5,4)),linewidth=1.3,zorder=2)
        ax.scatter([xx[-1]],[yy[-1]],s=85,facecolors='none',edgecolors='#AC6A1D',linewidths=1.8,zorder=5)
        ax.annotate(f'Last sample\n{xx[-1]:.3f} s; {yy[-1]:.5f} GiB',xy=(xx[-1],yy[-1]),xytext=(xx[-1]-23,4.0),fontsize=10,color='#6D491F',arrowprops={'arrowstyle':'-','color':'#AC6A1D','linewidth':1})
        ax.text(1,2.32,'2 GiB monitor STOP threshold',fontsize=9,color='#965A14')
        ax.set_title(f'{panel}  '+('Standard CPU inference' if run=='standard' else 'Chunking-enabled CPU attempt'),loc='left',fontsize=12,fontweight='bold',pad=12)
        ax.text(.02,.96,f'n = {len(data)} saved samples',transform=ax.transAxes,va='top',color='#53646C',fontsize=10)
        ax.set_xlim(0,56);ax.set_ylim(0,12);ax.set_xticks([0,10,20,30,40,50]);ax.set_yticks([0,2,4,6,8,10,12]);ax.grid(axis='y',alpha=.18)
        ax.set_xlabel('Elapsed time from execution start (s)',labelpad=9)
    axs[0].set_ylabel('Sampled system commit headroom (GiB)',labelpad=10)
    fig.suptitle('Sampled system commit headroom during CPU inference attempts',fontsize=17,fontweight='bold',x=.07,ha='left',y=.98,color='#17394D')
    fig.text(.07,.045,'Both terminal reports record MEMORY_STOP. Exact stop-event elapsed time was not logged; no event-time marker is inferred.',fontsize=10,color='#53646C')
    fig.subplots_adjust(left=.07,right=.98,bottom=.20,top=.83,wspace=.12)
    fig.savefig(dest/'figure2_commit_headroom.png',dpi=200,metadata={'Software':'C01 CD figure source'})
    fig.savefig(dest/'figure2_commit_headroom.svg',metadata={'Date':None})
    plt.close(fig)
    print(json.dumps({'output_directory':str(dest),'figures':2,'interpolation':False,'stop_event_marker':False,'source_state_kind':state['kind']}))

if __name__=='__main__':main()
