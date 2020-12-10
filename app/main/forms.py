from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from ..models import Session
from wtforms.validators import DataRequired


class SessionForm(FlaskForm):
    setTime = StringField('Work Time', validators=[DataRequired()])
    setBreak = StringField('Break Time', validators=[DataRequired()])
    setPurpose = TextAreaField('Enter Break Activity', validators=[DataRequired()])
    submit = SubmitField('Submit')