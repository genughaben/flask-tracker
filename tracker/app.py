from flask import Flask
from flask_cors import CORS
from flask_classful import FlaskView, route

from tracker.entry import EntryView
from tracker.food_group import GroupView
from tracker.food import FoodView
from tracker.statistic import StatisticView


class StartView(FlaskView):
    @route('/')
    def index(self):
        return "Startseite"


def create_app(settings_override=None):
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
