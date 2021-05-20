import random
from func_adl_servicex import ServiceXSourceXAOD
from servicex import ignore_cache

random.seed()

# huge data container 37646 files
# dataset_name = "data17_13TeV:data17_13TeV.periodK.physics_Main.PhysCont.DAOD_PHYS.grp17_v01_p4150"
# 308 files
dataset_name = "data17_13TeV:data17_13TeV.00339500.physics_Main.deriv.DAOD_PHYS.r10258_p3399_p4150_tid22781071_00"

# 2949 Tokio
dataset_name = "data17_13TeV:data17_13TeV.00340453.physics_Main.deriv.DAOD_PHYS.r12419_p4421_p4441_tid24675365_00"


src = ServiceXSourceXAOD(dataset_name)
df = src \
    .SelectMany('lambda e: e.Jets("AntiKt4EMTopoJets")') \
    .Select('lambda j: j.pt()/'+str(random.random())) \
    .AsPandasDF('JetPt') \
    .value()
print(df)
