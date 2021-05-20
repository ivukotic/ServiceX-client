import random
from func_adl_servicex import ServiceXSourceXAOD

random.seed()

dataset_name = "mc15_13TeV:mc15_13TeV.361106.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Zee.merge.DAOD_STDM3.e3601_s2576_s2132_r6630_r6264_p2363_tid05630052_00"

# 2949 Tokio
dataset_name = "data17_13TeV:data17_13TeV.00340453.physics_Main.deriv.DAOD_PHYS.r12419_p4421_p4441_tid24675365_00"


src = ServiceXSourceXAOD(dataset_name)
df = src \
    .SelectMany('lambda e: e.Jets("AntiKt4EMTopoJets")') \
    .Where('lambda j: j.pt() / '+str(random.random())+' > 30.0') \
    .Select('lambda j: j.eta()') \
    .AsPandasDF('JetPt') \
    .value()
print(df)
