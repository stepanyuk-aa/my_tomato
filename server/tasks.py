import db_connect

def get_login(token):
    db = db_connect.ohMysql(
        ip='192.168.1.10',
        user='admin',
        password="",
        current_db='myPomidoro'
    )
    login = db.read(
        'users',
        {
            'key': 'token',
            'if': '=',
            'value': token
        }
    )[0][1]

    if type(login) == type(""):
        return login
    else: return False

def add_task(data):
    db = db_connect.ohMysql(
        ip='192.168.1.10',
        user='admin',
        password="",
        current_db='myPomidoro'
    )
    login = get_login(data['token'])

    ## (task, description, interval, count/repeat, timer, user)
    dat = db.create(
        'tasks',
        (data['task'], data['description'], int(data['intervall']), int(data['repeat']), 0, login)
    )

    if dat == None:
        return {'status':'ok'}
    else:
        return {'status':'error'}

def get_tasks(token):
    db = db_connect.ohMysql(
        ip='192.168.1.10',
        user='admin',
        password="",
        current_db='myPomidoro'
    )
    login = get_login(token)

    tasks = db.read(
        'tasks',
        {
            'key': 'user',
            'if': '=',
            'value': login
        }
    )

    tmp = []
    for w in tasks:
        if w[7] != 2: tmp.append(w); print(w[7])

    for w in tmp: print(w)

    return tmp

def update_task(data):
    login = get_login(data['token'])
    if login == False: return "Error"

    db = db_connect.ohMysql(
        ip='192.168.1.10',
        user='admin',
        password="",
        current_db='myPomidoro'
    )

    for key in ('task', 'description', 'intervall', 'count', 'timer'):
        res = db.update(
            'tasks',
            {
                'set': {
                    'key': key,
                    'value': data[key]
                },
                'if': {
                    'key': 'id',
                    'value': data['id']
                }
            }
        )
        # return res

def change_status(data):
    login = get_login(data['token'])
    if login == False: return "Error"

    db = db_connect.ohMysql(
        ip='192.168.1.10',
        user='admin',
        password="",
        current_db='myPomidoro'
    )

    res = db.update(
        'tasks',
        {
            'set': {
                'key': 'status',
                'value': data['status']
            },
            'if': {
                'key': 'id',
                'value': data['id']
            }
        }
    )

    # return res

