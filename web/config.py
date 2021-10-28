# config.py

import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('../.env')
load_dotenv(dotenv_path=dotenv_path)


class BaseConfig(object):
    SECRET_KEY = os.environ['SECRET_KEY']
    DEBUG = os.environ['DEBUG']
    DB_NAME = os.environ['DB_NAME']
    DB_PASS = os.environ['DB_PASS']
    SQLALCHEMY_DATABASE_URI = 'sqlite+pysqlcipher://:{0}@/{1}?cipher=aes-256-cfb&kdf_iter=64000'.format(
        DB_PASS, DB_NAME
    )
