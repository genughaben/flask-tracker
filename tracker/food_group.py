# -*- coding: utf-8 -*-
from flask_classful import FlaskView, route


class GroupView(FlaskView):

    @route('/')
    @route('/list')
    def index(self):
        return u"Liste von Gruppennamen"

    @route('<int:id>')
    def get(self, id):
        return "Ein einzelne Gruppe {}".format(id)

    def new(self):
        return "Neue Gruppe"

    @route('/edit/<int:id>')
    def edit(self, id):
        return "Gruppe {} bearbeiten".format(id)

    @route('/delete/<int:id>')
    def delete(self, id):
        return u"Gruppe {} löschen".format(id)
