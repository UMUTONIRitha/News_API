from flask import render_template,request,redirect,url_for
from app import app
from .request import my_sources_news,my_articles_news

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    general = my_sources_news('general')
    entertainment = my_sources_news('entertainment')
    business = my_sources_news('business')
    health = my_sources_news('health')
    sports = my_sources_news('sports')
    science = my_sources_news('technology')

    title = ' NEWS FIRST'
    return render_template('index.html',general=general,technology=technology,health=health,science=science,entertainment=entertainment,sports=sports,business=business)

@app.route('/newsArticles/<id>')
def news(id):
    '''
    view page function that returns both the news article and its data
    '''

    articles = my_articles_news(id)
    title = 'NEWS FIRST'

    return render_template('newsArticles.html',articles=articles,title=title)