import flask.Flask as Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    kcal = db.Column(db.Float, nullable=False)


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food = db.Column(db.Integer, db.ForeignKey('food.id'))
    # owner = models.ForeignKey('auth.User',  # ADD THIS FIELD
    #                           related_name='entries',
    #                           on_delete=models.CASCADE)
    group_id = db.Column(db.Integer, db.ForeignKey('food_group.id'))
    # models.DecimalField(max_digits=6, decimal_places=1, default=Decimal(0.0))
    amount = db.Column(db.Float, nullable=False)
    amount_type = db.Column(db.String(max_length=20))
    kcal = db.Column(db.Decimal(2))
    entry_date = db.Column(db.DateTime(default=now().date()))
    created = models.DateTimeField('creation date', auto_now_add=True)
    updated = models.DateTimeField('update date', auto_now=True)


    # restaurant_id = db.Column(Integer, ForeignKey('restaurant.id'))
    # restaurant = relationship(Restaurant)


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)
