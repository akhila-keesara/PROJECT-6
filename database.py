import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

st.title("📦 Supply Chain Demand Forecast")

# Input: Number of forecast days
periods = st.number_input("Enter number of days to forecast:", min_value=1, max_value=365, value=30)

if st.button("Get Forecast"):
    with st.spinner("Calling FastAPI..."):
        response = requests.post("http://127.0.0.1:8000/forecast", json={"periods": periods})
        
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data)
            st.success("Forecast received!")

            st.subheader("Forecast Table")
            st.dataframe(df)

            st.subheader("Forecast Chart")
            fig, ax = plt.subplots()
            ax.plot(df["ds"], df["yhat"], label="Forecast")
            ax.fill_between(df["ds"], df["yhat_lower"], df["yhat_upper"], alpha=0.3, label="Confidence")
            ax.set_xlabel("Date")
            ax.set_ylabel("Predicted Demand")
            ax.legend()
            st.pyplot(fig)
        else:
            st.error(f"API Error: {response.status_code}")
