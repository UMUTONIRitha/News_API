from app import app
import urllib.request,json
from .news import News
from .sources import Source

# Getting api key
api_key = app.config['NEWS_API_KEY']
source_url = app.config['SOURCES_API_LINK']
# Getting the movie base url
base_url = app.config["NEWS_API_LINK"]

def my_source():
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = source_url.format(api_key)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)
        source_results = []
        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            # news_results = process_results(movie_results_list)
            for item in source_results_list:  
                category = item.get('category')
                name = item.get('name')
                description = item.get('description')
                url = item.get('url')
                # if poster:
                source_object = Source(category,name,description,url)
                source_results.append(source_object)
            return source_results








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
                publishedAt = item.get('publishefrom app import app
import urllib.request,json
from .models import sources,articles

Source = sources.Source
Article = articles.Artcle

# Getting api key
api_key = app.config['NEWS_API_KEY']
# Getting the source base url
base_url = app.config["SOURCE_API_BASE_URL"]
# Getting the article  url
articles_url = app.config["ARTICLE_API_BASE_URL"]

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        source_results = None
        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)
    return sources_results
def process_sources(sources_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects
    Args:
        sources_list: A list of dictionaries that contain movie details
    Returns :
        sources_results: A list of movie objects
    '''
    sources_results = []
    for item in sources_list:
        id = item.get('id')
        name = item.get('name')
        category = item.get('category')
        description = item.get('description')
        url = item.get('url')
        if id:
            sources_object = Source(id,name,category,description,url)
            sources_results.append(sources_object)
    return sources_results



def get_articles(id):
    '''
    function to return a list
    '''
    get_articles_url=articles_url.format(id,api_key)
    with urllib.request.urlopen(get_articles_url)as url:
        articles_results=json.loads(url.read())
        articles_object=None
        if articles_results['articles']:
            articles_object=process_articles(articles_results['articles'])
    return articles_object
def process_articles(articles_list):
    '''
    function to list all articles
    '''
    articles_object=[]
    for item in articles_list:
        title= item.get('title')
        description = item.get('description ')
        url = item.get('url')
        urlToImage = item.get('urlToImage')
        publishedAt = item.get('publishedAt')
        if urlToImage:
           articles_result=Article(title,description,url,urlToImage,publishedAt)
           articles_object.append(articles_result)
    return articles_objectdAt')
                url = item.get('url')
                urlToImage = item.get('urlToImage')
               

                if urlToImage:

                    news_object = News(author,title,description,publishedAt,url,urlToImage)
                    news_results.append(news_object)
            return news_results