import streamlit as st
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# Title
st.title("📈 Supply Chain Demand Forecasting")

# Upload CSV
uploaded_file = st.file_uploader("Upload your sales data (.csv)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Raw Data", df.head())

    # Rename for Prophet
    df.rename(columns={"Date": "ds", "Sales": "y"}, inplace=True)

    # Train model
    model = Prophet()
    model.fit(df)

    # Future data
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)

    st.write("### Forecasted Data", forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail())

    # Plot
    st.write("### Forecast Plot")
    fig1 = model.plot(forecast)
    st.pyplot(fig1)

    st.write("### Forecast Components")
    fig2 = model.plot_components(forecast)
    st.pyplot(fig2)
