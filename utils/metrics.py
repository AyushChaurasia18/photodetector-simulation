# utils/metrics.py
import numpy as np

def mse(original, noisy):
    return np.mean((original - noisy) ** 2)

def psnr(original, noisy):
    mse_val = mse(original, noisy)
    if mse_val == 0:
        return float("inf")
    return 20 * np.log10(255.0 / np.sqrt(mse_val))

def snr(signal):
    mean = np.mean(signal)
    std = np.std(signal)
    return mean / (std + 1e-8)