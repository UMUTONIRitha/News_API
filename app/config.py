
class Config:
    NEWS_SOURCES_URL = 'https://newsapi.org/v2/sources?category={}&apiKey={}'
    NEWS_ARTICLES_URL= 'https://newsapi.org/v2/everything?q=bitcoin&apiKey={}'
   
    # NEWS_API_KEY = 'f747d2632bd44a26aa624f00083b9df3'
class ProdConfig:
    pass

class DevConfig:
    
    DEBUG = True