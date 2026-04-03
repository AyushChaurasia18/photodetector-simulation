# core/photon.py
import numpy as np

def compute_lambda(image, N_max):
    return image * N_max

def generate_photons(lam):
    return np.random.poisson(lam)