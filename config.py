#!/usr/bin/python3

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dgQkcB$q>Xqb-%L/SIg1Le,7'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://sheen_user:Ta%40wa2892003@localhost/sheen_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False