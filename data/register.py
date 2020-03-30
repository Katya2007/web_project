from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, StringField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    surname = StringField('Фамилия ученика', validators=[DataRequired()])
    name = StringField('Имя ученика', validators=[DataRequired()]) 
    email = EmailField('Почтовый адрес', validators=[DataRequired()])
    telephone = StringField('Телефон', validators=[DataRequired()])
    class_ = StringField('Класс', validators=[DataRequired()])
    
    submit = SubmitField('Запись данных ученика')
