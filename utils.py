from firstrade import account, order, symbols
import yfinance as yf
import pandas as pd  

def get_tickers(url='https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'):
    # Use pandas to read the table from the Wikipedia page
    tables = pd.read_html(url)

    # The first table on the page contains the S&P 500 companies
    sp500_df = tables[0]

    # Display the DataFrame
    # print(sp500_df.head())

    # Extract the ticker symbols
    tickers = sp500_df['Symbol'].tolist()

    return tickers
