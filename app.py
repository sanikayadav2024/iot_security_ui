import streamlit as st
import numpy as np
import pandas as pd
import joblib

scaler = joblib.load("scaler.pkl")
model = joblib.load("model.pkl")   

st.set_page_config(page_title="IoT Security Dashboard", layout="wide")

st.title("🔐 IoT Security Monitoring Dashboard")

st.sidebar.header("📂 Upload Data")
uploaded_file = st.sidebar.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📊 Raw Data")
    st.write(df.head())


    df.columns = df.columns.str.strip()

    drop_cols = ['pkSeqID', 'stime', 'ltime', 'seq','smac','dmac','soui','doui','sco','dco']
    df.drop(columns=drop_cols, inplace=True, errors='ignore')

    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.fillna(0, inplace=True)

    df.drop(columns=['attack'], errors='ignore', inplace=True)

    X = df.select_dtypes(include=np.number).values

    expected_features = scaler.n_features_in_

    if X.shape[1] > expected_features:
        X = X[:, :expected_features]
    elif X.shape[1] < expected_features:
        padding = np.zeros((X.shape[0], expected_features - X.shape[1]))
        X = np.hstack((X, padding))

    X_scaled = scaler.transform(X)

    predictions = model.predict(X_scaled)

    df['Prediction'] = predictions

    total_devices = len(df)
    hacked_devices = int(df['Prediction'].sum())
    safe_devices = total_devices - hacked_devices

    st.subheader("📊 Device Status Overview")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Devices", total_devices)
    col2.metric("Hacked Devices 🚨", hacked_devices)
    col3.metric("Safe Devices ✅", safe_devices)

    st.subheader("🧠 Prediction Results")
    st.write(df.head(20))
    attacks = df[df['Prediction'] == 1]
    unique_pairs = attacks[['saddr', 'daddr']].drop_duplicates()
    

# Show only IP addresses of attacks
    st.subheader("🚨 Attack IP Addresses")

# Fix column names if needed (check your dataset!)
    st.write(unique_pairs)

    st.subheader("📈 Attack Distribution")
    st.bar_chart(df['Prediction'].value_counts())

else:
    st.info("👈 Upload a CSV file to start monitoring IoT devices")

# ==================