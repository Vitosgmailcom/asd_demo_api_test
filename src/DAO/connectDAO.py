from src.Utility.credentialsUtility import credentialsDB

import pymysql.cursors

class ConnactDAO(object):
    def __init__(self):
        self.cred = credentialsDB()

    def connect_ASK_DB(self):
        connection = pymysql.connect(
            user=self.cred['db_user'],
            password=self.cred['db_pass'],
            database=self.cred['db_name'],
            host=self.cred['db_host'],
            port=int(self.cred['db_port'])
            )
        return connection

    def execute_SELECT(self, sql):
        conn = self.connect_ASK_DB()

        with conn.cursor(pymysql.cursors.DictCursor) as cursor:

            cursor.execute(sql)
            result = cursor.fetchall()

            return result


