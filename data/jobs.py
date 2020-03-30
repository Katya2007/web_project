import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase

from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, StringField, PasswordField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    job_link = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    link_to_google_form = sqlalchemy.Column(sqlalchemy.String, nullable=True)    

    def __repr__(self):
        return f'<Job> {self.job}'



