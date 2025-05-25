import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

# Load model and scaler
model = joblib.load("final_rf_model.pkl")
scaler = joblib.load("final_scaler.pkl")

st.title("Caravan Insurance Purchase Predictor")
st.markdown("Upload customer data to predict insurance purchase likelihood.")

# File uploader
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("### Uploaded Data Preview", data.head())

    # Feature check
    if data.shape[1] != 85:
        st.error("Uploaded data must have exactly 85 features (Feature_0 to Feature_84)")
    else:
        # Assign column names
        data.columns = [f"Feature_{i}" for i in range(85)]

        # Standardize input
        data_scaled = scaler.transform(data)

        # Make predictions
        probs = model.predict_proba(data_scaled)[:, 1]
        preds = (probs >= 0.5).astype(int)

        # Output results
        result_df = data.copy()
        result_df["Predicted_Probability"] = probs
        result_df["Predicted_Caravan"] = preds

        st.write("### Predictions", result_df[["Predicted_Probability", "Predicted_Caravan"]])

        # Download option
        csv = result_df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Predictions", csv, "predictions.csv", "text/csv")
