from appl.database import db
from flask_sqlalchemy import SQLAlchemy
from datetime import date

class User(db.Model):
    __tablename__ = "user"
    #user_details
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    email=db.Column(db.String,nullable=False)
    telephone=db.Column(db.Integer,unique=True,nullable=False)
    address=db.Column(db.String,nullable=False)
    dob=db.Column(db.String,nullable=False)

class Category(db.Model):
    __tablename__ = "category"
    category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column(db.String, nullable=False)
    category_rel=db.relationship("Product")
    def convert(self):
        return {
            'c_id': self.category_id
        }

class Product(db.Model):
    __tablename__ = "product"
    # Columns ie Product_details
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    owner = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    name = db.Column(db.String, unique=True, nullable=False)
    units = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    shelf_life = db.Column(db.Integer, nullable=False)
    manufacturer_details = db.Column(db.String, nullable=False)
    fsaai_license = db.Column(db.String, nullable=False) 
    
   
    # Correct the ForeignKey declaration
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'), nullable=False)
    category = db.relationship('Category')

    def convert(self):
        return {
            
            'c_id': self.category_id
            
        }

class Purchases(db.Model):
    __tablename__ = "purchases"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product = db.Column(db.Integer, nullable=False)
    owner = db.Column(db.Integer, nullable=False)
    customer = db.Column(db.Integer, nullable=False)
    count = db.Column(db.Integer, nullable=False)
    date_added = db.Column(db.Date, nullable=False, default=date.today)