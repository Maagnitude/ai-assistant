import requests
from creds import news_key

def get_news():
    
    newslist = []
    base_url = f"http://api.mediastack.com/v1/news?access_key={news_key}&countries=us&languages=en&categories=science&limit=1"
    
    data = requests.get(base_url).json()
    
    if "data" in data and len(data["data"]) > 0:
        for i in range(len(data["data"])):
            news = data["data"][i]["description"]
            news = news.replace("&#8217;", "'")
            newslist.append(news)
        return newslist
    
    