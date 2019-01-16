import os
from flask import Flask,render_template,request,redirect,url_for,session
from flask import Flask, session, redirect, url_for, escape, request
from flask_sqlalchemy import SQLAlchemy
import json
#data = os.popen(cmd)

app = Flask(__name__)

def index():
    return render_template('b.html')

@app.route('/data')
def data():
    ip = "127.0.0.1"

    cmd = "nmap" + " " + "{0}".format(ip)
    data = os.popen(cmd).read()


    print data
    # a = ["1","2","3","2","3","8"]
    #b= json.dumps(data)
    return data


app.run(host='0.0.0.0')
