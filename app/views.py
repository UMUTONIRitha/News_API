from flask import render_template,request,redirect,url_for
from app import app
from .request import get_sources, get_articles
from .models import sources,articles

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting cateory news

    general_sources = get_sources('general')
    technology_sources = get_sources('technology')
    entertainment_sources = get_sources('entertainment')
    business_sources = get_sources('business')
    health_sources = get_sources('health')

    title = 'Home - Welcome to The best category news Website Online'
    return render_template('index.html', title = title,general = general_sources,technology = technology_sources,entertainment = entertainment_sources,business = business_sources,health = health_sources)


@app.route('/sources/<id>')
def articles(id):
    '''
    View article page function that returns the article details page and its data
    '''
    articles = get_articles(id)
    title = f'You are viewing {id}'
    
    return render_template('article.html',title = title,articles = articles)