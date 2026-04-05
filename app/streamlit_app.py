# app/streamlit_app.py

import streamlit as st
import numpy as np
from PIL import Image

from simulation.pipeline import run_simulation
from config import DEFAULT_CONFIG
from utils.metrics import mse, psnr, snr
from utils.image_generator import generate_default_image

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
st.set_page_config(layout="wide")

st.title("📷 Photon-Limited Imaging Simulator")

# =========================
# Sidebar: Parameters
# =========================
st.sidebar.header("Simulation Parameters")

T = st.sidebar.slider("Exposure Time", 0.1, 10.0, 1.0)
eta = st.sidebar.slider("Quantum Efficiency", 0.1, 1.0, 0.7)
dark_current = st.sidebar.slider("Dark Current", 0.0, 0.1, 0.01)
read_noise = st.sidebar.slider("Read Noise Std", 0.0, 5.0, 1.0)
max_size = st.sidebar.slider("Max Image Size", 128, 1024, 512)
config = DEFAULT_CONFIG.copy()
config.update({
    "T": T,
    "eta": eta,
    "dark_current": dark_current,
    "read_noise_std": read_noise
})

# =========================
# Sidebar: Image Input
# =========================
st.sidebar.header("Input Image")

use_default = st.sidebar.checkbox("Use Default Synthetic Image", True)

uploaded_file = st.file_uploader("Upload image", type=["png", "jpg", "jpeg"])
N_max = st.sidebar.slider("Max Photon Count", 1, 5000, 1000)

config.update({
    "N_max": N_max,
    "eta": eta,
    "dark_current": dark_current,
    "read_noise_std": read_noise
})
# =========================
# Image Processing Function
# =========================
def process_uploaded_image(uploaded_file, max_size=512):
    img = Image.open(uploaded_file).convert("L")

    # Resize if too large
    width, height = img.size
    max_dim = max(width, height)

    if max_dim > max_size:
        scale = max_size / max_dim
        new_size = (int(width * scale), int(height * scale))
        img = img.resize(new_size, Image.Resampling.LANCZOS)

    img = np.array(img).astype(np.float32) / 255.0
    return img

# =========================
# Select Image Source
# =========================
if use_default:
    image = generate_default_image()

elif uploaded_file is not None:
    image = process_uploaded_image(uploaded_file, max_size)

else:
    st.warning("No image selected. Using default image.")
    image = generate_default_image()

# =========================
# Run Simulation
# =========================
noisy = run_simulation(image, config)

# =========================
# Display
# =========================
col1, col2 = st.columns(2)

with col1:
    st.subheader("Original")
    st.image(image, clamp=True)

with col2:
    st.subheader("Simulated")
    st.image(noisy / (np.max(noisy) + 1e-8), clamp=True)

# =========================
# Metrics
# =========================
st.subheader("Metrics")

mse_val = mse(image * 255, noisy)
psnr_val = psnr(image * 255, noisy)
snr_val = snr(noisy)

st.write(f"MSE: {mse_val:.2f}")
st.write(f"PSNR: {psnr_val:.2f}")
st.write(f"SNR: {snr_val:.2f}")