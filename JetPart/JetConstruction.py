import numpy as np
from random import random
from time import clock
# E of each patron in first pair of patrons is approx. scale/2
e_crit = 1
# alpha has to be smaller than or equal to 1
alpha = 0.5

# c = 1 unit system.
# Thus, p = E, for limit: m -> 0.

# Input: Four-momentum vector W, with W[0] = E, W[1-3] = (px,py,pz)
# Output: Matrix of four-momentum vector (so, 3-D), with values after hadronization


def parton_shower(W, e_crit = 1):
    ret = []
    if W[0] <= e_crit:
        return [W]
    e_z = W[0] * (2/(1+random())-1)
    azimuth_angle = (2*np.pi/(1+random()) - np.pi)
    polar_angle = (np.pi/(1+random()) - np.pi/2)

    # Angle of given four-momentum vector
    delta = np.pi/2
    if not W[1] == 0:
        delta = np.arctan(W[2]/W[1])
    pz = e_z * np.cos(polar_angle)
    py = e_z * np.sin(polar_angle) * np.sin(delta+azimuth_angle)

    # E^2 = p^2 = px^2 + py^2 + pz^2
    px = np.sqrt(e_z**2 - py**2 - pz**2)

    for p in parton_shower([e_z, px, py, pz], e_crit=e_crit):
        ret.append(p)
    for p in parton_shower([W[0] - e_z, W[1] - px, W[2] - py, W[3] - pz], e_crit=e_crit):
        ret.append(p)
    return ret


def collision(e_crit = 10**-1, alpha = 1):
    ret = []
    e_parton = -np.log(-alpha*random()+1)/alpha

    azimuth_angle = random()*2*np.pi
    polar_angle = random() * np.pi

    pz = e_parton * np.cos(polar_angle)
    py = e_parton * np.sin(polar_angle) * np.sin(azimuth_angle)
    px = np.sqrt(e_parton**2 - pz**2 - py**2)
    if np.pi/2 < azimuth_angle < 3 * np.pi/2:
        px *= -1

    for p in parton_shower([e_parton, px, py, pz], e_crit=e_crit):
        ret.append(p)
    for p in parton_shower([e_parton, -px, -py, -pz], e_crit=e_crit):
        ret.append(p)
    return ret
