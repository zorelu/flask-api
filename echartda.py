from flask import send_file, send_from_directory,jsonify
from flask import Flask, session, redirect, url_for, escape, request
from flask_sqlalchemy import SQLAlchemy
import json
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api.db'
db = SQLAlchemy(app)

##订阅数据库
class Ecahrt(db.Model):
    __tablename__ = 'echart'
    id = db.Column(db.String(100), primary_key=True)
    data = db.Column(db.String(100))
rdata=[]
for a in Ecahrt.query.all():
    # print(a.data)
    rdata.append(a.data)

print(rdata)