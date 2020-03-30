from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, StringField, PasswordField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = PasswordField('Введите почтовый адрес', validators=[DataRequired()])  
    submit = SubmitField('Получить ссылки на задания и гуглформы')