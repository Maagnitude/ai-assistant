import requests
from creds import news_key

def get_news():
    
    newslist = []
    base_url = f"http://api.mediastack.com/v1/news?access_key={news_key}&countries=us&languages=en&limit=1"
    
    data = requests.get(base_url).json()
    
    if "data" in data and len(data["data"]) > 0:
        for i in range(len(data["data"])):
            newslist.append(data["data"][i]["description"])
        return newslist
    
    