from app import app
import urllib.request,json
from .news import News
from .sources import Sources

# Getting api key
api_key = app.config['NEWS_API_KEY']
source_key = app.config['SOURCES_API_LINK']
# Getting the movie base url
base_url = app.config["NEWS_API_LINK"]

def my_sources():
    '''
    function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = []

        if get_sources_response['sourcesNews']:
            sources_results_list = get_sources_response['sourcesNews']
            # news_results = process_results(sources_results_list)
            for new in sources_results_list:

                category = new.get('category')
                name = new.get('name')
                description = new.get('description')
                url = new.get('url')

                sources_object = Sources(category,name,description,url)
                sources_results.append(sources_object)
            return sources_results








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
            # news_results = process_results(news_results_list)
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