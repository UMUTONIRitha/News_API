class News_sources:
    '''
    class of news source to define news object
    '''

    def __init__ (self,id,name,description,url,category):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category







class News_Articles:
    def __init__ (self,id,author,title,description,publishedAt,url,urlToImage):

        self.news_id = id
        self.news_author = author
        self.news_title = title
        self.news_description = description
        self.news_publishedAt = publishedAt
        self.news_url = url
        self.news_urlToImage = urlToImage