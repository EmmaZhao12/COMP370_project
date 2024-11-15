import requests
import json
from datetime import datetime, timedelta

#your API key
api_key = "5d0ce2b34d6f4040b96084a889eb0f30"
start_date = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")

url = "https://newsapi.org/v2/everything"
params = {
    'q': 'Donald Trump OR Trump',  
    'language': 'en',
    #change domains to news outlets you want, might take more than 5
    'domains': 'thestar.com,ctvnews.ca,globalnews.ca,nationalpost.com,theglobeandmail.com,rabble.ca,huffpost.com,torontosun.com,vancouversun.com,nationalpost.com,montrealgazette.com',     
    'from': {str(start_date)},  
    'apiKey': api_key
}

all_articles = []  
for page in range(1, 6):  
    params['page'] = page
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        all_articles.extend(articles)
        
        if len(articles) < 100:
            break
    else:
        print(f"Failed to fetch page {page}: {response.status_code}")
        break

print(f"Found {len(all_articles)} articles in total.")


with open('donald_trump_articles_CAN.json', 'w', encoding='utf-8') as json_file:
    json.dump(all_articles, json_file, indent=4, ensure_ascii=False)


