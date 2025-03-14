from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from flask import Flask, request, make_response

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    image = db.Column(db.Text)
    price = db.Column(db.Float)


  


