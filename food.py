# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from flask_classful import FlaskView, route

class FoodView(FlaskView):

    @route('/')
    @route('/list')
    def index(self):
        return u"Liste von Lebensmitteln"

    @route("/group/<string:group_name>")
    def list_of_group(self, group_name):
        # add swtich that checks for 'today', 'yesterday', date:date or week-num or 'week'
        return u"Lebensmittel aus Gruppe {}".format(group_name)

    @route('<int:id>')
    def get(self, id):
        # return "Ein einzelnes Lebensmittel {}".format(id)
        food_db = FoodDB()
        example_food = food_db.return_foods()
        return jsonify(example_food)

    def new(self):
        return "Neues Lebensmittel"

    @route('/edit/<int:id>')
    def edit(self, id):
        return "Lebensmittel {} bearbeiten".format(id)

    @route('/delete/<int:id>')
    def delete(self, id):
        return u"Lebensmittel {} löschen".format(id)

# -*- coding: utf-8 -*-
class FoodDB():

    def __init__(self):
        pass

    def return_foods(self):
        example_food = [{
            "id": 1,
            "name": "Tofu",
            "group": "Huelsenfruechte",
            "kcal": 76.0
        }]
        return example_food
