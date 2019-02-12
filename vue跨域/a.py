from flask import Flask,render_template,request,redirect,url_for,session
from flask import Flask, session, redirect, url_for, escape, request
from flask import send_file, send_from_directory,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)
@app.route('/')

def index():
    a=[{"id":10010,"name":'admin',"age":28},{"id":10011,"name":'admin2',"age":19}]
    return jsonify(a)
	
	
	

app.run(host='0.0.0.0')
