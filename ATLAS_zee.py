#  from https://github.com/d-w-liu/documentation/blob/1.0/ServiceX%20stuff/ElectronData_1.1.ipynb

from servicex import ServiceXDataset
from servicex.minio_adaptor import MinioAdaptor
from servicex.servicex_adaptor import ServiceXAdaptor
# from func_adl_xAOD import ServiceXDatasetSource
from func_adl_servicex import ServiceXSourceXAOD

# import uproot_methods
import matplotlib.pyplot as plt

import datetime


def create_dataset(dataset_name):
    sxdataset = ServiceXDataset(dataset_name)

    return sxdataset


zee_dataset = create_dataset(
    'mc15_13TeV:mc15_13TeV.361106.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Zee.merge.DAOD_STDM3.e3601_s2576_s2132_r6630_r6264_p2363_tid05630052_00')
zmm_dataset = create_dataset(
    'mc15_13TeV:mc15_13TeV.361107.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Zmumu.merge.DAOD_STDM3.e3601_s2576_s2132_r6630_r6264_p2363_tid05630078_00')


def retrieve_data(dataset):
    data = ServiceXSourceXAOD(dataset) \
        .Select('lambda e: (e.Electrons("Electrons"), e.Muons("Muons"))') \
        .Select('lambda ls: (ls[0].Select(lambda e: e.pt()), ls[0].Select(lambda e: e.eta()), \
                         ls[0].Select(lambda e: e.phi()), ls[0].Select(lambda e: e.e()), \
                         ls[1].Select(lambda m: m.pt()), ls[1].Select(lambda m: m.eta()), \
                         ls[1].Select(lambda m: m.phi()), ls[1].Select(lambda m: m.e()))') \
        .AsAwkwardArray(('ElePt', 'EleEta', 'ElePhi', 'EleE', 'MuPt', 'MuEta', 'MuPhi', 'MuE')) \
        .value()
    return data


def four_vectorize(leptons_per_event, lepton_type):
    four_vector = uproot_methods.TLorentzVectorArray.from_ptetaphi(
        leptons_per_event[bytes(f"{lepton_type}Pt", 'utf-8')
                          ], leptons_per_event[bytes(f"{lepton_type}Eta", 'utf-8')],
        leptons_per_event[bytes(f"{lepton_type}Phi", 'utf-8')
                          ], leptons_per_event[bytes(f"{lepton_type}E", 'utf-8')],
    )

    return four_vector


def organize_leptons(dataset, lepton_type):
    v_leptons = four_vectorize(dataset, lepton_type)
    v_leptons = v_leptons[v_leptons.counts >= 2]
    dileptons = v_leptons[:, 0] + v_leptons[:, 1]

    return dileptons


def plot_data(dielectrons, dimuons):
    plt.figure(figsize=(12, 6))
    plt.hist(dielectrons.mass/1000.0, bins=100, range=(0, 200))
    plt.title('Di-Electron Mass')
    plt.xlabel('$m_{ee}$ [GeV]')
    plt.ylabel('Count')
    plt.show()

    plt.figure(figsize=(12, 6))
    plt.hist(dimuons.mass/1000.0, bins=100, range=(0, 200))
    plt.title('Di-Muon Mass')
    plt.xlabel('$m_{\mu\mu}$ [GeV]')
    plt.ylabel('Count')
    plt.show()


zee_retrieved_data = retrieve_data(zee_dataset)
zmm_retrieved_data = retrieve_data(zmm_dataset)

zee_die = organize_leptons(zee_retrieved_data, 'Ele')
zee_dim = organize_leptons(zee_retrieved_data, 'Mu')

plot_data(zee_die, zee_dim)

zmm_die = organize_leptons(zmm_retrieved_data, 'Ele')
zmm_dim = organize_leptons(zmm_retrieved_data, 'Mu')

plot_data(zmm_die, zmm_dim)
