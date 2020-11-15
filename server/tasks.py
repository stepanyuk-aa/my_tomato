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
        (data['task'], data['description'], int(data['interval']), int(data['repeat']), 0, login)
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
    return tasks

def update_task(data):
    login = get_login(data['token'])
    if login == False: return "Error"

    db = db_connect.ohMysql(
        ip='192.168.1.10',
        user='admin',
        password="",
        current_db='myPomidoro'
    )

    for key in ('task', 'description', 'interval', 'count', 'timer'):
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

        print(res)
        # return res
