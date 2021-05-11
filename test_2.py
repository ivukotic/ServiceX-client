import random
from func_adl_servicex import ServiceXSourceXAOD

random.seed()

dataset_name = "mc15_13TeV:mc15_13TeV.361106.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Zee.merge.DAOD_STDM3.e3601_s2576_s2132_r6630_r6264_p2363_tid05630052_00"
src = ServiceXSourceXAOD(dataset_name)
r = src \
    .Select('lambda e: (e.Electrons("Electrons"), e.Muons("Muons"))') \
    .Select('lambda ls: (ls[0].Select(lambda e: e.pt() / '+str(random.random())+'), \
                            ls[0].Select(lambda e: e.eta()), \
                            ls[0].Select(lambda e: e.phi()), \
                            ls[0].Select(lambda e: e.e()), \
                            ls[1].Select(lambda m: m.pt()), \
                            ls[1].Select(lambda m: m.eta()), \
                            ls[1].Select(lambda m: m.phi()), \
                            ls[1].Select(lambda m: m.e()))') \
    .AsAwkwardArray(('ElePt', 'EleEta', 'ElePhi', 'EleE', 'MuPt', 'MuEta', 'MuPhi', 'MuE')) \
    .value()
print(r)
