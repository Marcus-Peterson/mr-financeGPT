import torch
import torch.nn as nn
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

class StockData:
    def __init__(self, ticker):
        self.ticker = ticker
        self.scaler = MinMaxScaler(feature_range=(0, 1))

    def fetch_data(self, start_date, end_date, interval='1d'):
      tickerData = yf.Ticker(self.ticker)
      tickerDf = tickerData.history(period=interval, start=start_date, end=end_date)
      return tickerDf['Close']

    def normalize_data(self, data):
        return self.scaler.fit_transform(data.values.reshape(-1,1))

    # Example: A simple PyTorch model (e.g., for future forecasting or analysis)
    class SimpleModel(nn.Module):
        def __init__(self):
            super(StockData.SimpleModel, self).__init__()
            self.linear = nn.Linear(1, 1)

        def forward(self, x):
            return self.linear(x)

    def apply_model(self, data):
        model = self.SimpleModel()
        # Dummy implementation - real model would have training, inference, etc.
        return model(torch.tensor(data).float()).detach().numpy()


