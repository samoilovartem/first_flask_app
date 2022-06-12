from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField(validators=[DataRequired()], render_kw={'class': 'form-control'})
    password = PasswordField(validators=[DataRequired()], render_kw={'class': 'form-control'})
    submit = SubmitField(render_kw={'class': 'btn btn-primary'})
