# 📷 Physics-Based Simulation of Photon-Limited Imaging with Photodetector Noise

## 📖 Overview
This project implements a modular, physics-based simulation of low-light imaging systems, modeling the complete process from incident light to digital image formation.

The simulation captures:
- Photon arrival statistics (Poisson processes)
- Detector physics (quantum efficiency, dark current)
- Electronic noise (read noise)
- Analog-to-digital conversion (ADC)

The goal is to study how fundamental physical limits affect image quality, especially in photon-limited regimes.

---

## 🎯 Objectives
- Model photon-limited imaging systems from first principles
- Simulate realistic photodetector behavior
- Incorporate multiple noise sources:
  - Shot noise
  - Dark current
  - Read noise
- Build an interactive simulation interface (Streamlit)
- Analyze degradation using quantitative metrics (SNR, PSNR, MSE)

---

## 🧠 System Pipeline
Scene Intensity  
↓  
Photon Generation (Poisson)  
↓  
Quantum Efficiency (Detection)  
↓  
Dark Current Addition  
↓  
Read Noise (Gaussian)  
↓  
Analog Signal  
↓  
ADC (Gain → Clipping → Quantization)  
↓  
Final Digital Image  

---

## ⚙️ Mathematical Model
S(x,y) = Poisson(ηλ(x,y) + λ_dark) + N(0, σ_read²)

Where:
- λ(x,y) = (I(x,y) · P₀ · T) / (hν)
- η = quantum efficiency
- λ_dark = dark current
- σ_read² = read noise variance

---

## 🏗️ Project Structure
photon_imaging_sim/
│
├── app/
│   └── streamlit_app.py
│
├── core/
│   ├── photon.py
│   ├── detector.py
│   ├── noise.py
│   └── adc.py
│
├── simulation/
│   └── pipeline.py
│
├── utils/
│   └── metrics.py
│
├── config.py
├── requirements.txt
└── README.md

---

## 🧰 Installation
```bash
pip install -r requirements.txt
```

---

## ▶️ Running the App
```bash
streamlit run app/streamlit_app.py
```

---

## 📊 Metrics
- Signal-to-Noise Ratio (SNR)
- Mean Squared Error (MSE)
- Peak Signal-to-Noise Ratio (PSNR)

---

## 🚀 Future Work
- Color sensor simulation (Bayer filter)
- Spatial non-uniformity
- Motion blur modeling
- ML-based denoising
- Medical imaging applications

---

## 📎 Status
🚧 Work in Progress

---

## 👤 Author
Ayush Chaurasia  

