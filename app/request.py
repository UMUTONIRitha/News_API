from app import app
import urllib.request,json
from .news import News_sources,News_Articles



# Getting api key
api_key = None
# Getting the news base url
source_url = None
article_news_url = None

def config_request(app):
    global api_key,base_url,article_news_url
    api_key = app.config['NEWS_API_KEY']
    source_url = app.config["NEWS_SOURCES_URL"]
    article_news_url = app.config["NEWS_ARTICLES_URL"]


def my_sources_news(category):
    '''
    function that gets json response to our url request
    '''
    get_sources_url = source_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)
    return sources_results

def process_sources(sources_list):
    '''
    function that processes the news and transform them to a list of objects
    args:
        source_list :a list of dictionaries that contain news details
    returns:
        sources_results:a list of news source objects
    '''

    sources_results = []
    for sources_item in sources_results:
        id = sources_item.get('id')
        name = sources_item.get('name')
        description = sources_item.get('description')
        url = sources_item.get('url')
        category = sources_item.get('category')

        sources_object = Sources(id,name,description,url,category)
        sources_results.append(sources_object)

    return sources_results

def my_articles_news(id):
    '''
    Function that gets the json response to our url request
    '''

    get_newsArticles_url = article_news_url.format(id,api_key)
    print(get_newsArticles_url)

    with urllib.request.urlopen(get_newsArticles_url) as url:
    
        articles_results= json.loads(url.read())

        articles_object = None
        if articles_results['articles']:
            articles_object = process_articles(articles_results['articles'])
           
    return articles_object

def process_articles(articles_list):
    '''
    '''
    articles_object = []
    for item in articles_list:
        id = item.get('id')
        author = item.get('author')
        title = item.get('title')
        description = item.get('description')
        publishedAt = item.get('publishedAt')
        url = item.get('url')
        urlToImage = item.get('urlToImage')

        if urlToImage:
            articles_result = News_Articles(id,author,title,description,publishedAt,url,urlToImage)
            articles_object.append(articles_result)
               
    return articles_object