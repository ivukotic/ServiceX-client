import sys
import pandas as pd
from func_adl_servicex import ServiceXSourceUpROOT

dataset_name = "data15_13TeV:data15_13TeV.00282784.physics_Main.deriv.DAOD_PHYSLITE.r9264_p3083_p4165_tid21568807_00"
if len(sys.argv) > 1:
    dataset_name = sys.argv[1]

src = ServiceXSourceUpROOT(dataset_name, "CollectionTree")
data = src.Select("lambda e: {'JetPT': e['AnalysisJetsAuxDyn.pt']}") \
    .AsParquetFiles('junk.parquet') \
    .value()
df = pd.read_parquet(data[0])
print(df)
