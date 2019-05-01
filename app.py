import os
import sys
from flask import Flask
from flask_mongoengine import MongoEngine

sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '../../')))

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'users'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/users'
db = MongoEngine()
db.init_app(app)

from endpoints import *

if __name__ == '__main__':
    app.run()
