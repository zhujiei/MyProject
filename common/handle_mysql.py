import pymysql
from common.handle_config import conf

class HandleDB:

    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def connect(self):
        '''连接数据库'''
        self.db = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.username,
            password=self.password)

    def get_cursor(self):
        '''获取游标'''
        self.cursor = self.db.cursor()
        return self.cursor

    def close(self):
        '''关闭连接'''
        self.cursor.close()
        self.db.close()

    def select_one(self, sql, **value):
        '''查询一条数据'''
        result = None
        try:
            self.connect()
            cursor = self.get_cursor()
            cursor.execute(sql, *value)
            result = cursor.fetchone()
            self.close()
        except Exception as e:
            print(e)
        return result

    def select_all(self, sql, **value):
        '''查询多条数据'''
        list_data = ()
        try:
            self.connect()
            cursor = self.get_cursor()
            cursor.execute(sql, *value)
            list_data = self.cursor.fetchall()
            self.close()
        except Exception as e:
            print(e)
        return list_data

    def update(self, sql, **value):
        '''修改数据'''
        try:
            self.connect()
            cursor = self.get_cursor()
            cursor.execute(sql, *value)
            self.db.commit()
            # self.close()
        except Exception as e:
            self.db.rollback()
            print(e)
        finally:
            '''关闭游标、连接'''
            self.cursor.close()
            self.close()

    def delete(self, sql, **value):
        '''删除数据'''
        try:
            self.connect()
            cursor = self.get_cursor()
            cursor.execute(sql, *value)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print(e)
        finally:
            '''关闭游标、连接'''
            self.cursor.close()
            self.close()


db = HandleDB(
            host=conf.get('mysql', 'host'),
            port=conf.getint('mysql', 'port'),
            username=conf.get('mysql', 'username'),
            password=conf.get('mysql', 'password')
            )

if __name__ == '__main__':
    sql = "SELECT * from test_qichacha.cc_order WHERE buyer_id ='584d084095794d7c8ff3091305f67b6e' AND pay_status ='2';"
    rows = db.select_all(sql=sql)
    print(rows)
    print(type(rows))
    print(len(rows))


