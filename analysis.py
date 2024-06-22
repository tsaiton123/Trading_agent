import yfinance as yf
import pandas as pd  
import numpy as np
import time

def get_accerleration(stock_ticker):
    # Get the historical data of past 10 minutes (or more to get better calculation)
    data = yf.download(stock_ticker, period='1d', interval='1m').tail(10)
    # print(data)

    # Ensure we have enough data
    if len(data) < 10:
        return "Not enough data to calculate acceleration."
    
    # Calculate velocity: change in price per minute
    velocity = data['Close'].diff()
    
    # Calculate acceleration: change in velocity per minute
    acceleration = velocity.diff()

    # Get the latest acceleration
    latest_acceleration = acceleration.iloc[-1]
    
    return latest_acceleration