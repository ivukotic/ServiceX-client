import servicex as sx
from func_adl_servicex import ServiceXSourceXAOD

toy_dataset = "mc15_13TeV:mc15_13TeV.361106.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Zee.merge.DAOD_STDM3.e3601_s2576_s2132_r6630_r6264_p2363_tid05630052_00"
sx_dataset = sx.ServiceXDataset(toy_dataset, "xaod")
df = ServiceXSourceXAOD(sx_dataset) \
    .SelectMany('lambda e: e.Jets("AntiKt4EMTopoJets")') \
    .Select('lambda j: j.pt()/1000.0') \
    .AsPandasDF('JetPt') \
    .value()

print(df)
