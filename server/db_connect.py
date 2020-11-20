import mysql.connector
import config

class ohMysql(object):
    """ip, user, password="""""
    # def __init__(self, ip=config.host, user=config.user, password=config.password, current_db=config.database):
    def __init__(self, ip, user, password, current_db):
        self.mysqldb = mysql.connector.connect(
            host=ip,
            user=user,
            password=password,
            database=current_db
        )
        self.mycursor = self.mysqldb.cursor()

    def create(self, table, values):
        """
        data = ('vasy1','112345','', 0)
        db.create('users',data)
        """
        try:
            if (table == "users"):
                table = """INSERT INTO users 
                    (login, password, token, time) 
                    VALUES (%s, %s, %s, %s)"""
            if (table == 'tasks'):
                table = """INSERT INTO tasks 
                    (`task`, `description`, `intervall`, `count`, `timer`, `user`, `status`, `group`)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

            self.mycursor.execute(table,values)
            self.mysqldb.commit()
            print('Record inserted successfully...')
        except:
            self.mysqldb.rollback()

    def read(self, table, values):
        """
        # table: 'string'
        # values:
        {
            'key':'login',
            'if':'=',
            'value':login
        }
        """
        try:
            sql_q = "SELECT * FROM " + table

            if values != 'all':
                sql_q = sql_q + ' WHERE ' + values['key'] + values['if'] + "'" + values['value'] + "'"

            self.mycursor.execute(sql_q)

            return self.mycursor.fetchall()

        except:
            self.mysqldb.rollback()
            return 'Error'

    def update(self,table, values):
        """
        db.update(
            'users',
            {
                'set':{
                    'key':'password',
                    'value':'Skill39!'
                },
                'if':{
                    'key':'login',
                    'value':'admin'
                }
            }
        )
        """
        try:

            sql_q = "UPDATE %s SET %s = '%s' WHERE %s = '%s'" % \
                    (table, values['set']['key'],
                     values['set']['value'],
                     values['if']['key'],
                     values['if']['value']
                     )

            self.mycursor.execute(sql_q)
            self.mysqldb.commit()
            print('Update successfully...')

        except:
            self.mysqldb.rollback()

    def delete(self, table, values):
        try:
            sql_q = "DELETE FROM %s WHERE %s %s '%s'" % (table, values['key'], values['if'], values['value'])
            self.mycursor.execute(sql_q)
            self.mysqldb.commit()
        except:
            self.mysqldb.rollback()
    def close(self):
        self.mysqldb.close()



# db = db_connect.ohMysql(ip,user,password,db_name)

# data = ('vasy1','112345','', 0)
# db.create('users',data)

# db.delete(
#     'users',
#     {
#         'key':'login',
#         'if':'=',
#         'value':'test2'
#     }
# )



# print(db.read(
#     'users',{'key':'login', 'if':'=','value':'vasy1'}
# ))

# db.close()