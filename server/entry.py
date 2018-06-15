# -*- coding: utf-8 -*-
from flask import Flask
from flask_classful import FlaskView, route


class EntryView(FlaskView):
    route_base = '/'

    @route('/entry')
    @route('/entry/list')
    def list(self):
        return "Einträge - Liste"

    @route("/entry/list/<string:day_or_week_identifier>")
    def day(self, day_or_week_identifier):
        # add swtich that checks for 'today', 'yesterday', date:date or week-num or 'week'
        return u"Einträge von {}".format(day_or_date)

    @route('/entry/<int:id>')
    def entry(self, id):
        return "Ein einzelner Eintrag {}".format(id)

    @route('entry/new')
    def new(self):
        return "Neuer Eintrag"

    @route('entry/edit/<int:id>')
    def edit(self, id):
        return "Eintrag {} bearbeiten".format(id)

    @route('entry/delete/<int:id>')
    def delete(self, id):
        return u"Eintrag {} löschen".format(id)
