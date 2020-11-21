class Config:
    NEWS_API_LINK = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey={}'
    SOURCES_API_LINK = 'https://newsapi.org/v2/sources?apiKey={}'
class ProdConfig:
    pass

class DevConfig:
    NEWS_API_LINK = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey={}'
    SOURCES_API_LINK = 'https://newsapi.org/v2/sources?apiKey={}'
    DEBUG = True