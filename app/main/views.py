from flask import render_template, url_for, flash, redirect, request, abort
from . import main
from flask_login import login_required, current_user
from ..import db

@main.route('/')
def index():
    """
    Function that returns the index page
    """
    return render_template('index.html')

