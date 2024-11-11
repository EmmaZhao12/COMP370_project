from pathlib import Path
from dotenv import load_dotenv
import os
from requests import get
import datetime
import json

query_string = 'https://newsapi.org/v2/everything?'



def fetch_latest_news(api_key, news_keywords, news_sources):
    current_date = datetime.date.today()
    lookback = datetime.date.today() - datetime.timedelta(30)
    
    edited_keyword = []
    for i in range(len(news_keywords)):
        if i != 0:
            edited_keyword.append('OR')
        if ' ' in news_keywords[i]:
            news_keywords[i] = f'+"{news_keywords[i]}"' 
        edited_keyword.append(news_keywords[i])
    edited_keyword = ''.join(edited_keyword)
    news_sources = ','.join(news_sources)

    for i in range(1,6):
        query = f'{query_string}q={edited_keyword}&domains={news_sources}&sortBy=publishedAt&page={i}&language=en&from={str(lookback)}&to={str(current_date)}&apiKey={api_key}'
        response = get(query)
        response = response.json()

    with open(f"page{i}.json", "w") as fp:
        json.dump(response, fp, indent=4)

if __name__ == "__main__":
    key='ed0028ec564b480bac2b1f94947559ee'
    final_keywords = ['Donald Trump', 'donald trump', 'Trump', 'Donald']
    news_outlets = ['cbc.ca', 'ctvnews.ca', 'globalnews.ca', 'cnn.com', 'nytimes.com', 'foxnews.com', 'msn.com', 'usatoday.com']
    fetch_latest_news(key, final_keywords, news_outlets)

