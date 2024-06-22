from firstrade import account, order, symbols
import os
import sys
import json
import time
import datetime
import logging
import argparse
import requests
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from tqdm import tqdm


from news_sentiment import get_sentiment
from utils import *
from analysis import *

class agent:

    def __init__(self, name, cash, stocks, username, password, pin):
        self.name = name
        self.cash = cash
        self.stocks = stocks


        # # Create a session
        # ft_ss = account.FTSession(username, password, pin)
        # # Get account data
        # ft_accounts = account.FTAccountData(ft_ss)
        # if len(ft_accounts.account_numbers) < 1:
        #     raise Exception("No accounts found or an error occured exiting...")
        # # Print ALL account data
        # print(ft_accounts.all_accounts)

        # # Print 1st account number.
        # print(ft_accounts.account_numbers[0])

        # # Print ALL accounts market values.
        # print(ft_accounts.account_balances)

    def buy(self, stock, amount):
        self.cash -= stock.price * amount
        self.stocks[stock] = self.stocks.get(stock, 0) + amount

    def sell(self, stock, amount):
        self.cash += stock.price * amount
        self.stocks[stock] -= amount
        if self.stocks[stock] == 0:
            del self.stocks[stock]

    def sentiment_analysis(self, stock_ticker):
        sentiment = get_sentiment(stock_ticker)
        print(sentiment)

    def momentum_strategy(self, stock_ticker):
        acc = get_accerleration(stock_ticker)
        print(acc)


    def __str__(self):
        return f'{self.name} has {self.cash} cash and {self.stocks} stocks'

    def __repr__(self):
        return str(self)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Trade Agent')
    parser.add_argument('--username', required=True, help='Firstrade username')
    parser.add_argument('--password', required=True, help='Firstrade password')
    parser.add_argument('--pin', required=True, help='Firstrade pin')
    args = parser.parse_args()

    a = agent('John', 1000, {}, args.username, args.password, args.pin)
    # a.sentiment_analysis("AAPL")

    # init a dataframe with columns ['ticker', 'acceleration']
    df = pd.DataFrame(columns=['ticker', 'acceleration'])

    tickers = get_tickers()
    for ticker in tqdm(tickers):
        acc = float(get_accerleration(ticker))
        df = df._append({'ticker': ticker, 'acceleration': acc}, ignore_index=True)

    print(df)
    # sort the dataframe by acceleration
    df = df.sort_values(by='acceleration', ascending=False)
    print(df)