from fastapi import FastAPI
from model import run_forecast
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

class ForecastRequest(BaseModel):
    periods: int = 30  # Days to forecast

@app.post("/forecast")
def forecast(data: ForecastRequest):
    df = pd.read_csv("sample_data.csv")
    forecast_df = run_forecast(df, data.periods)
    return forecast_df.to_dict(orient="records")
