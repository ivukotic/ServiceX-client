import sys
import random
from func_adl_servicex import ServiceXSourceXAOD
from servicex import ignore_cache

random.seed()

# huge data container 37646 files
dataset_name = "data17_13TeV:data17_13TeV.periodK.physics_Main.PhysCont.DAOD_PHYS.grp17_v01_p4150"

if len(sys.argv) > 1:
    dataset_name = sys.argv[1]

src = ServiceXSourceXAOD(dataset_name)
df = src \
    .SelectMany('lambda e: e.Jets("AntiKt4EMTopoJets")') \
    .Select('lambda j: j.pt()/'+str(random.random())) \
    .AsPandasDF('JetPt') \
    .value()
print(df)
