🛡️ BoT-IoT Attack Detection & IP Analysis Dashboard
📌 Overview

This project is a Machine Learning-based Network Intrusion Detection System built using the BoT-IoT dataset.
It predicts whether network traffic is normal (0) or an attack (1) and displays results using an interactive Streamlit dashboard.

The application also extracts and visualizes unique attacker IP addresses for further analysis.

🧠 Tech Stack
Python 🐍
Pandas
Scikit-learn
Streamlit
NumPy

Project Structure

project_root
|
|---app.py            # Streamlit main application
|---model.pkl          # Trained ML model
|---scaler.pkl          # scaler
|---requirements.txt     # Dependencies


⚙️ Installation
# Clone repository
git clone https://github.com/sanikayadav2024/iot_security_ui.git

# Navigate to project
cd iot_security_ui

# Install dependencies
pip install -r requirements.txt

▶️ Usage
streamlit run app.py

Then open in browser:
http://localhost:8501

📈 Output
Table of predictions
Unique attacker IP list
Attack distribution chart

👨‍💻 Author

Your Name
GitHub: https://github.com/sanikayadav2024
