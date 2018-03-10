import os
from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)

current_dir = os.path.dirname(os.path.abspath(__file__))
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}/{}'.format(current_dir, 'db/app.db')
db = SQLAlchemy(app)
admin = Admin(app, name='Flask Admin Exploration')

# Declare Models

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	email = db.Column(db.String)
	password = db.Column(db.String)
	supplier = db.relationship('Product', backref=db.backref('products', lazy=True))

class Product(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	supplier_id = db.Column(db.Integer, db.ForeignKey('user.id')) 

# END of Model declaration

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Product, db.session))

if __name__ == ('__main__'):
	app.run()
