from flask import render_template
# from app import app
from . import main
# Views

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to the Pizza-shop'
    return render_template('index.html')