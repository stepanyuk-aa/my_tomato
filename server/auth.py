import random
import db_connect

def check(loging_data):
    print(loging_data)
    if loging_data['password'] == get_password(loging_data['login']):
        token = gen_token()
        add_session(loging_data['login'], token)
        return {'token':token}
    else: return False

def get_password(login):
    db = db_connect.ohMysql(
        ip='192.168.1.10',
        user='admin',
        password="",
        current_db='myPomidoro'
    )

    dat = db.read(
        'users',
        {
            'key':'login',
            'if':'=',
            'value':login
        }
            )
    if dat:
        return dat[0][2]
    else:
        return False

def add_session(login, token):
    db = db_connect.ohMysql(
        ip='192.168.1.10',
        user='admin',
        password="",
        current_db='myPomidoro'
    )

    db.update(
        'users',
        {
            'set': {
                'key': 'token',
                'value': token
            },
            'if': {
                'key': 'login',
                'value': login
            }
        }
    )

def gen_token():
    token = ""
    seq = [1,2,3,4,5,6,7,8,9,
            'q','w','e','r','t','y','u','i','o','p','a','s','d'
            ,'f','g','h','j','k','l','z','x','c','v','b','n','m']

    for w in range(0,20):
        token += str(random.choice(seq))

    return token

def check_login(login):
    db = db_connect.ohMysql(
        ip='192.168.1.10',
        user='admin',
        password="",
        current_db='myPomidoro'
    )

    dat = db.read(
        'users',
        {
            'key':'login',
            'if':'=',
            'value':login
        }
            )

    if dat != []:
        return "conflict"
    else:
        return 'ok'

def create_user(login, password):
    db = db_connect.ohMysql(
        ip='192.168.1.10',
        user='admin',
        password="",
        current_db='myPomidoro'
    )

    dat = db.create(
        'users',
        (login, password, '', 0)
    )