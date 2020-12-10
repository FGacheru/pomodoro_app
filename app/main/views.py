from app.models import Session
from flask import render_template, url_for, flash, redirect, request, abort
from flask.globals import session
from . import main
from flask_login import login_required, current_user
from ..import db
from .forms import SessionForm

@main.route('/')
def index():
    """
    Function that returns the index page
    """
    return render_template('index.html')



@main.route('/pomodoro', methods = ['GET','POST'])
@login_required
def new_session():
    form = SessionForm()
    
    if form.validate_on_submit():
        setTime = form.setTime.data
        setBreak = form.setBreak.data
        setPurpose = form.setPurpose.data

        #updated session
        new_session = Session(setTime=setTime, setBreak=setBreak, setPurpose=setPurpose, user=current_user)

        #save session
        new_session.save_session()
        return redirect(url_for('main.index'))   

    return render_template('session.html', form = form)         