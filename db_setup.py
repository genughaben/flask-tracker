## start: config part ##
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

## end: config part ##


## begin class definition ##

class Food(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(String(80), nullable = False)
    kcal = db.Column(db.Float, nullable = False)

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
    food = models.ForeignKey(Food, related_name="entries")
    owner = models.ForeignKey('auth.User',  # ADD THIS FIELD
                              related_name='entries',
                              on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=1, default=Decimal(0.0))
    amount_type = models.CharField(max_length=20)
    kcal = models.DecimalField(max_digits=8, decimal_places=1, default=Decimal(0.0))
    date = models.DateField('entry date', default=now().date())
    created = models.DateTimeField('creation date', auto_now_add=True)
    updated = models.DateTimeField('update date', auto_now=True)


    restaurant_id = db.Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)
    ## end: mapper ##

## end class definition ##

### insert at the end of file ###

engine = create_engine(
  'sqlite:///restaurantmenu.db'
)

Base.metadata.create_all(engine)
