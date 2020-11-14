# from mysql.connector import connect

import auth
import db_connect
from flask import Flask
from flask import request
from flask_cors import CORS
from flask import jsonify

ip = '192.168.1.111'
user = 'admin'
password = ""
db_name = 'myPomidoro'

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login', methods=['POST', 'GET'])
def f_login():
    check = auth.check(request.get_json())


    if check:
        check['status'] = 'success'
    else:
        check = {'status':'error'}

    return jsonify(check)

@app.route('/registration', methods=['POST', 'GET'])
def f_registration():
    login = request.get_json()['login']
    password = request.get_json()['password']

    check = auth.check_login(login)

    if check == 'ok':
        check = {'status': 'success'}
        auth.create_user(login,password)

    elif check == 'conflict':
        check = {'status': 'conflict'}
    else:
        check = {'status':'error'}

    return jsonify(check)

if __name__ == '__main__':
    app.run(host="192.168.1.106")