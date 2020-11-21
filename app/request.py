from app import app
import urllib.request,json
from .news import News
# Getting api key
api_key = app.config['News_Api_key']
# Getting the news base url
base_url = app.config["News_Api_Link"]
def my_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        news_results = None
        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            # news_results = process_results(movie_results_list)
            for item in news_results_list:
                source = item.get('source')
                author = movie_item.get('author')
                title = movie_item.get('title')
                description = movie_item.get('description')
                publishedAt = movie_item.get('publishedAt')
                url = movie_item.get('url')
                poster = movie_item.get('urlToImage')
                # if poster:
                news_object = Movie(source,author,title,description,publishedAt,url,poster)
                news_results.append(news_object)
            return news_results