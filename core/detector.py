# core/detector.py
import numpy as np

def apply_quantum_efficiency(photons, eta):
    # Poisson thinning
    return np.random.poisson(eta * photons)

def add_dark_current(shape, dark_rate, T):
    lam_dark = dark_rate * T
    return np.random.poisson(lam_dark, size=shape)