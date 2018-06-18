from flask import Flask
from flask_cors import CORS
from flask_classful import FlaskView, route

from tracker.entry import EntryView
from tracker.food_group import GroupView
from tracker.food import FoodView
from tracker.statistic import StatisticView

app = Flask(__name__)
CORS(app)


class StartView(FlaskView):
    @route('/')
    def index(self):
        return "Startseite"


StartView.register(app, route_base='/')
EntryView.register(app, route_base='/')
GroupView.register(app)
FoodView.register(app)
StatisticView.register(app)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8765)
