from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse
import matplotlib.pyplot as plt
import uvicorn
import io
from datetime import datetime, timedelta
import os
from ai_code import StockData
import yfinance as yf
import pandas as pd
from fastapi.responses import StreamingResponse
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/privacy-policy")
async def privacy_policy(request: Request):
  return templates.TemplateResponse("privacy-policy.html", {"request": request})



# Helper function to calculate dates
def get_dates_from_period(period, interval):
    end_date = datetime.now()
    if interval in ['1m', '2m', '5m', '15m', '30m', '60m', '90m']:
        end_date = datetime.now() - timedelta(days=7)  # Yahoo Finance limitation for minute intervals
    if period == 'month':
        start_date = end_date - timedelta(days=30)
    elif period == 'year':
        start_date = end_date - timedelta(days=365)
    elif period == 'day':
        start_date = end_date - timedelta(days=1)
    elif period == 'hour':
        start_date = end_date - timedelta(hours=1)
    elif period == 'minute':
        start_date = end_date - timedelta(minutes=1)
    elif period == 'week':
      start_date = end_date - timedelta(weeks=1)
    else:
        raise HTTPException(status_code=400, detail="Invalid period")
    return start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')



# Endpoint to get raw data
@app.get("/data/{ticker}/{period}/{interval}")
async def get_data(ticker: str, period: str, interval: str = '1d'):
    start_date,end_date = get_dates_from_period(period, interval)
    stock = StockData(ticker)
    data = stock.fetch_data(start_date, end_date, interval)
    return data.to_dict()

# Endpoint to get normalized data
@app.get("/normalized-data/{ticker}/{period}/{interval}")
async def get_normalized_data(ticker: str, period: str, interval: str = '1d'):
    start_date, end_date = get_dates_from_period(period, interval)
    stock = StockData(ticker)
    data = stock.fetch_data(start_date, end_date, interval)
    normalized_data = stock.normalize_data(data)
    return normalized_data.tolist()

# Endpoint to get model-applied data
@app.get("/model-data/{ticker}/{period}/{interval}")
async def get_model_data(ticker: str, period: str, interval: str = '1d'):
    start_date, end_date = get_dates_from_period(period, interval)
    stock = StockData(ticker)
    data = stock.fetch_data(start_date, end_date, interval)
    normalized_data = stock.normalize_data(data)
    model_data = stock.apply_model(normalized_data)
    return model_data.tolist()

# Endpoint to plot and return the graph as PNG
@app.get("/plot/{ticker}/{period}/{interval}")
async def plot_data(ticker: str, period: str, interval: str = '1d'):
    start_date, end_date = get_dates_from_period(period, interval)
    stock = StockData(ticker)
    data = stock.fetch_data(start_date, end_date, interval)
    normalized_data = stock.normalize_data(data)

    plt.figure(figsize=(10,6))
    plt.plot(data.index, normalized_data, label='Normalized Closing Price')
    plt.title(f'{ticker} Price Fluctuation')
    plt.xlabel('Date')
    plt.ylabel('Normalized Price')
    plt.legend()

    plot_file = f'{ticker}_plot.png'
    plt.savefig(plot_file)
    plt.close()

    return FileResponse(plot_file)


@app.get("/alphavantage/intraday/{symbol}{interval}")
async def get_alphavantage_data(intraday:str, symbol:str, interval:str):
  url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey=demo"
  
  

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)


