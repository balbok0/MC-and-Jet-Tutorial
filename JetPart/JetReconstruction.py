from JetConstruction import collision
from copy import deepcopy
import numpy as np
from Graph import histo3d


def reconstruct(parton_shower, R, n):

    rec_init_partons = []
    number_of_partons = 0
    changable_parton_shower = deepcopy(parton_shower)

    while len(changable_parton_shower) > 1:
        min_d = find_min_d(changable_parton_shower, R, n)
        created_parton = np.add(changable_parton_shower.pop(min_d[2]),changable_parton_shower.pop(min_d[1]))
        changable_parton_shower.append(created_parton)

        pT = np.sqrt(created_parton[1]**2 + created_parton[2]**2)
        if min_d[0] < pT**(2*n):
            number_of_partons += 1
            rec_init_partons.append(changable_parton_shower.pop(len(changable_parton_shower) - 1))

    if len(changable_parton_shower) == 1:
        number_of_partons += 1
        rec_init_partons.append(changable_parton_shower[0])

    return [number_of_partons, rec_init_partons]


def find_min_d(parton_shower, R, n):

    minimum = [np.inf, 0, 0]
    for parton in range(len(parton_shower)):
        d_ij = find_min_d_i(parton_shower, parton, R, n)
        if d_ij[0] < minimum[0]:
            minimum = d_ij

    return minimum


def find_min_d_i(parton_shower, index, R, n):

    min_d = np.inf
    j_index = 0
    i = parton_shower[index]

    p_i = np.sqrt(i[1]**2 + i[2]**2)
    # How to calculate eta and phi: https://en.wikipedia.org/wiki/Pseudorapidity
    phi_i = np.arccos(i[1]/p_i)
    eta_i = np.arcsinh(i[3]/p_i)

    for j in range(index+1, len(parton_shower)):
        parton_j = parton_shower[j]
        p_j = np.sqrt(parton_j[1] ** 2 + parton_j[2] ** 2)

        min_pT = min(p_j**(2*n), p_i**(2*n))

        # Calculate delta_i_j
        delta_phi = phi_i - np.arccos(parton_j[1]/p_j)
        delta_eta = eta_i - np.arcsinh(parton_j[3]/p_j)
        delta_i_j = np.sqrt(delta_phi**2 + delta_eta**2)

        if min_pT * delta_i_j / R < min_d:
            min_d = min_pT * delta_i_j / R
            j_index = j
    return [min_d, index, j_index]


