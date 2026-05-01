# 🛡️ BoT-IoT Attack Detection & IP Analysis Dashboard

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg" />
  <img src="https://img.shields.io/badge/Streamlit-App-red.svg" />
  <img src="https://img.shields.io/badge/Machine%20Learning-Enabled-green.svg" />
  <img src="https://img.shields.io/badge/Status-Active-success.svg" />
</p>

---

## 📌 Overview

This project is a **Machine Learning-based Network Intrusion Detection System** built using the **BoT-IoT dataset**.

It predicts whether network traffic is:

* ✅ **Normal (0)**
* 🚨 **Attack (1)**

The results are displayed using an interactive **Streamlit dashboard**, which also highlights **unique attacker IP addresses** for deeper analysis.

---

## ✨ Features

* 🔍 ML-based attack detection
* 📊 Interactive Streamlit dashboard
* 🚨 Filter traffic where `attack_prediction = 1`
* 🌐 Extract and display **unique attacker IPs**
* 📈 Attack distribution visualization

---

## 🧠 Tech Stack

* Python 🐍
* Pandas
* Scikit-learn
* Streamlit
* NumPy

---

## 📂 Project Structure

```
project_root/
│
├── app.py             # Main Streamlit application (UI + prediction logic)
├── model.pkl          # Trained machine learning model
├── scaler.pkl         # Data scaler for preprocessing
├── requirements.txt   # Project dependencies
```

---

## ⚙️ Installation

```bash
# Clone repository
git clone https://github.com/sanikayadav2024/iot_security_ui.git

# Navigate to project folder
cd iot_security_ui

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
streamlit run app.py
```

Then open in your browser:

```
http://localhost:8501
```

---

## 📈 Output

* 📋 Table of predictions
* 🌐 Unique attacker IP list
* 📊 Attack distribution chart

---

## 📸 Screenshots (Add yours)

> 💡 Tip: Add screenshots here to make your project stand out on GitHub

```

<img width="1447" height="843" alt="image" src="https://github.com/user-attachments/assets/6b698dff-a48f-4736-ac36-e5ad136a3b4d" />

```

---

## 👨‍💻 Author

**Sanika Yadav**
GitHub: https://github.com/sanikayadav2024

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
