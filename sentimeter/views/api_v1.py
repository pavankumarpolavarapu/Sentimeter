import traceback
import requests
import flask
from flask import Response
from sentimeter import app


@app.route('/api/v1/test')
def test():
    """
    Testing the Flask Application
    """
    return "It Works!!!"

