from prophet import Prophet
import pandas as pd

def run_forecast(df: pd.DataFrame, periods: int = 30):
    # Expecting df to have columns 'ds' and 'y'
    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)

    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(periods)
