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
    )

    if login == []:
        return False
    else: return login[0][1]

def add_task(data):
    db = db_connect.ohMysql(
        ip='192.168.1.10',
        user='admin',
        password="",
        current_db='myPomidoro'
    )
    login = get_login(data['token'])

    print(data)
    ## (task, description, interval, count/repeat, timer, user)
    dat = db.create(
        'tasks',
        (data['task'], data['description'], int(data['intervall']), int(data['repeat']), 0, login, 0, data['group'])
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

    if(login == False): return False

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
        if w[7] != 2: tmp.append(w);

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

def get_groups(token):
    login = get_login(token)
    if login == False: return "Error"

    db = db_connect.ohMysql(
        ip='192.168.1.10',
        user='admin',
        password="",
        current_db='myPomidoro'
    )

    tasks = get_tasks(token)

    groups = []
    for w in tasks:
        groups.append(w[-1])
    groups = list(set(groups))

    return groups