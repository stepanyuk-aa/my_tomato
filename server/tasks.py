import db_connect

def add_task(data):
    db = db_connect.ohMysql(
        ip='192.168.1.10',
        user='admin',
        password="",
        current_db='myPomidoro'
    )

    # Get user login
    login = db.read(
        'users',
        {
            'key': 'token',
            'if': '=',
            'value': data['token']
        }
    )[0][1]

    ## (task, description, interval, count/repeat, timer, user)
    dat = db.create(
        'tasks',
        (data['task'], data['description'], int(data['interval']), int(data['repeat']), 0, login)
    )

    if dat == None:
        return {'status':'ok'}
    else:
        return {'status':'error'}