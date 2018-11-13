from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    password = StringField('password:', validators=[DataRequired()])
    submit = SubmitField('Submit')
