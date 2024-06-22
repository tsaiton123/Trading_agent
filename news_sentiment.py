import requests
import os
import pandas as pd
from transformers import pipeline

def get_news(stock_ticker, num_articles=20, api_key='YOUR_NEWSAPI_KEY'):
    url = f'https://newsapi.org/v2/everything?q={stock_ticker}&apiKey={api_key}&pageSize={num_articles}'
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch news: {response.status_code}, {response.text}")

    data = response.json()
    articles = data.get('articles', [])

    news_list = []
    for article in articles:
        news_list.append({
            "headline": article["title"],
            "link": article["url"],
            "source": article["source"]["name"],
            "published_at": article["publishedAt"]
        })

    return pd.DataFrame(news_list)

def get_sentiment(stock_ticker):

    api_key = '66824c56e5f54659ab9a92b6995c471f'  # Replace with your actual API key
    stock_ticker = "AAPL"
    news_df = get_news(stock_ticker, api_key=api_key)

    classifier = pipeline("sentiment-analysis")
    result = []
    
    for headline in news_df['headline']:
        result.append(classifier(headline))

    return result

if __name__ == '__main__':
    # Example usage
    api_key = '66824c56e5f54659ab9a92b6995c471f'  # Replace with your actual API key
    stock_ticker = "AAPL"
    news_df = get_news(stock_ticker, api_key=api_key)

    # Display the DataFrame
    from IPython.display import display
    display(news_df)

    news_df['headline']

    classifier = pipeline("sentiment-analysis")
    for headline in news_df['headline']:
        result = classifier(headline)
        
        print(headline,':',result,'\n')
        # end line
   