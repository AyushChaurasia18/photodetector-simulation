# core/adc.py
import numpy as np

def apply_gain(signal, gain):
    return gain * signal

def clip_signal(signal, V_max):
    return np.clip(signal, 0, V_max)

def quantize(signal, bit_depth, V_max):
    levels = 2 ** bit_depth
    delta = V_max / levels
    return np.floor(signal / delta)