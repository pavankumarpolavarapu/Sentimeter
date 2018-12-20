import logging
from flask import Flask
from os import environ

app = Flask(__name__)
app.config['DEBUG'] = True
DATABASE_PATH = 'app/Assets/SQLite.db'

import sentimeter.views
app.run()