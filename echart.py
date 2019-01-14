from flask import Flask,render_template,request,redirect,url_for,session
from flask import Flask, session, redirect, url_for, escape, request
from flask_sqlalchemy import SQLAlchemy
import json
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api.db'
db = SQLAlchemy(app)
class Ecahrt(db.Model):
    __tablename__ = 'echart'
    id = db.Column(db.String(100), primary_key=True)
    data = db.Column(db.String(100))
rdata=[]


@app.route('/')

def index():
    return render_template('b.html')

@app.route('/data')
def data():
    for d in Ecahrt.query.all():
        # print(a.data)
        rdata.append(d.data)
    print(rdata)
    # a = ["1","2","3","2","3","8"]
    a = rdata
    b= json.dumps(a)
    return b


app.run(host='0.0.0.0')