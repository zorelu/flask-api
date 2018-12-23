from flask import send_file, send_from_directory,jsonify
from flask import Flask, session, redirect, url_for, escape, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api.db'
db = SQLAlchemy(app)

##订阅数据库
class User(db.Model):
    __tablename__ = 'user'
    useid = db.Column(db.Integer, primary_key=True)
    secret = db.Column(db.String(100))
    token = db.Column(db.String(110))
# users = User.query.filter(User.useid == user_id).first()
# print(users.token)
#返回usetoken 错误信息
def reusetoken(token,mes):
    data = {
        "token": token,
        "mes": mes
    }
    return data

##使用用户id，密码获取token
@app.route('/v1.0/token', methods=['GET', 'POST'])
def token():
    # remove the username from the session if it's there
    if request.method == 'GET':
        useid = request.args.get('userid', '')
        secret = request.args.get('secret', '')
        if secret == '' or useid == '':
            token = "no userid or secret "
            mes = "no secret 4001"
        else:
            try:
                users = User.query.filter(User.useid == useid, User.secret == secret).first()
                token = users.token
                mes = "ok 2000"
            except BaseException:
                token = "not token in sqlserver"
                mes ="no sql select 4002"
                # return "userid={},secret={}".format(useid,secret)
        data = {
            "useid":useid ,
            "secret":secret,
            "token": token,
            "mes":mes
             }
        return jsonify(data)
    else:
        return  'this is post no allow'


##使用token
@app.route('/v1.0/usetoken', methods=['GET', 'POST'])
def usetoken():
    token = request.args.get('token', '')
    if token =='' :
        mes = "eoor 4003"
        return jsonify(reusetoken(token,mes))
    else:
        intoken = User.query.filter(User.token == token).first()
        if intoken == None:
            mes = "no token in sql"
            token="no token"
            return jsonify(reusetoken(token,mes))
        else:
            token=intoken.token
            mes ="2000 ok"
            return jsonify(reusetoken(token,mes))


app.run(host='0.0.0.0')