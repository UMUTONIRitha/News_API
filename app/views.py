from flask import render_template,request,redirect,url_for
from app import app
from .request import my_news,my_sources
# Views
@app.route('/')
def sources():
    '''
    View root page function that returns the source page and its data
    '''
    mySourcesData = my_sources()
    print(mySourcesData)
    return render_template('sources.html',sourceData=mySourcesData)


@app.route('/articles')
def index():
    '''
    View second page function that returns the index page and its data
    '''
    myNewsData = my_news()
    print(myNewsData)
    return render_template('index.html',data=myNewsData)