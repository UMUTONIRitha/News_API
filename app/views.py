from flask import render_template,request,redirect,url_for
from app import app
from .request import my_news
# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    myNewsData = my_news()
    print(myNewsData)
    return render_template('index.html',data=myNewsData)