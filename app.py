import os
import sys

from cerberus import Validator
from flask import Flask, jsonify
from flask_mongoengine import MongoEngine

validator = Validator()
sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '../../')))

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'users'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/users'
db = MongoEngine()
db.init_app(app)


def CORSify(resp):
    if type(resp) is dict:
        resp = jsonify(resp)
    resp.headers.add("Access-Control-Allow-Origin", "*")
    return resp


from endpoints import *

if __name__ == '__main__':
    app.run()
