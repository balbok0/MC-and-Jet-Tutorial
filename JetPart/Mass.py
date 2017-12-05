import numpy as np


def distance(parton1, parton2):
    pT1 = np.sqrt(parton1[1]**2 + parton1[2]**2)
    pT2 = np.sqrt(parton2[1]**2 + parton2[2]**2)

    phi1 = np.arccos(parton1[1]/pT1)
    eta1 = np.arcsinh(parton1[3]/pT1)

    phi2 = np.arccos(parton2[1]/pT2)
    eta2 = np.arcsinh(parton2[3]/pT2)
    return np.sqrt((phi1-phi2)**2 + (eta1-eta2)**2)



def SimpleMass(Jet):
    max = []
    max_2 = []
    pT_max = -np.inf
    pT_max_2 = -np.inf
    for parton in Jet:
        pT = np.sqrt(parton[1]**2 + parton[2]**2)
        if pT > pT_max_2:
            if pT > pT_max:
                pT_max = pT
                max = parton
            else:
                pT_max_2 = pT
                max_2 = parton
    E1 = max[0]
    E2 = max_2[0]
    delta_R = distance(max, max_2)
    return E1*E2*delta_R
