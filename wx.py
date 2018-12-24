from flask import send_file, send_from_directory,jsonify
from flask import Flask, session, redirect, url_for, escape, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api.db'
db = SQLAlchemy(app)

class Wx(db.Model):
    __tablename__ = 'wx'
    type = db.Column(db.String(100))
    name = db.Column(db.String(100),primary_key=True)
    url = db.Column(db.String(110))
wxifo=Wx.query.all()

for a in wxifo:
    b = {
        "type":a.type,
        "name":a.name,
        "url":a.url
    }
    print(b)
c= {
    "body":b
    }
print(c)