# simulation/pipeline.py

import numpy as np
from core.photon import compute_lambda, generate_photons
from core.detector import apply_quantum_efficiency, add_dark_current
from core.noise import add_read_noise
from core.adc import apply_gain, clip_signal, quantize

def run_simulation(image, config):
    
    eta = config["eta"]
    dark_current = config["dark_current"]
    read_noise_std = config["read_noise_std"]
    gain = config["gain"]
    bit_depth = config["bit_depth"]
    V_max = config["V_max"]
    N_max = config["N_max"]
    lam = compute_lambda(image, N_max)
    T = config["T"]
    photons = generate_photons(lam)

    # Step 2: detection
    electrons = apply_quantum_efficiency(photons, eta)

    # Step 3: dark current
    dark = add_dark_current(image.shape, dark_current, T)

    signal = electrons + dark

    # Step 4: read noise
    signal = add_read_noise(signal, read_noise_std)

    # Step 5: ADC
    signal = apply_gain(signal, gain)
    signal = clip_signal(signal, V_max)
    digital = quantize(signal, bit_depth, V_max)

    return digital