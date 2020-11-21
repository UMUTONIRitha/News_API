from app import app
import urllib.request,json
from .news import News

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_LINK"]
def my_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = []

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            # news_results = process_results(movie_results_list)
            for item in news_results_list:
              
                author = item.get('author')
                title = item.get('title')
                description = item.get('description')
                publishedAt = item.get('publishedAt')
                url = item.get('url')
                urlToImage = item.get('urlToImage')
               

                if urlToImage:

                    news_object = News(author,title,description,publishedAt,url,urlToImage)
                    news_results.append(news_object)
            return news_results