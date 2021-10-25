import sys
from func_adl_servicex import ServiceXSourceUpROOT

dataset_name = "root://eospublic.cern.ch//eos/opendata/atlas/OutreachDatasets/2020-01-22/4lep/MC/mc_345060.ggH125_ZZ4lep.4lep.root"
if len(sys.argv) > 1:
    dataset_name = sys.argv[1]
if len(sys.argv) > 2:
    backend = sys.argv[2]


src = ServiceXSourceUpROOT([dataset_name], 'mini', backend_name=backend)
r = (
    src.Select(lambda e: {'lep_pt': e['lep_pt']}).AsAwkwardArray().value()
)
print(r)
