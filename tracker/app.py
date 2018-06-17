from flask import Flask
from flask_cors import CORS
from flask_classful import FlaskView, route

from entry import EntryView
from food_group import GroupView
from food import FoodView
from statistic import StatisticView


class StartView(FlaskView):
    @route('/')
    def index(self):
        return "Startseite"


def create_app():
    '''
     Create a Flask application using the app facory pattern
     :return: Flask app
     '''

    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    StartView.register(app, route_base='/')
    EntryView.register(app, route_base='/')
    GroupView.register(app)
    FoodView.register(app)
    StatisticView.register(app)

    return app
