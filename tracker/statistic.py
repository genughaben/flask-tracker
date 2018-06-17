# -*- coding: utf-8 -*-
from flask import Flask
from flask_classful import FlaskView, route

class StatisticView(FlaskView):

    @route('/')
    def index(self):
        return u"Übersichtsstatistik"

    @route("<string:day_or_timespan_identifier>")
    def day(self, day_or_timespan_identifier):
        # add swtich that checks for 'today', 'yesterday', date:date or week-num or 'week'
        return u"Statistik für {}".format(day_or_timespan_identifier)
