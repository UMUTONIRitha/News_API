
class Config:
    NEWS_API_LINK = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey={}'

class ProdConfig:
    pass

class DevConfig:
    NEWS_API_LINK = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey={}'
    DEBUG = True