
from src.Utility.credentialsUtility import credentialsDB

import pymysql.cursors
import logging as log

class ConnectDAO(object):
    def __init__(self):
        self.cred_info = credentialsDB()
        log.info(self.cred_info)

        # import pdb; pdb.set_trace()
    def connectASK(self):
        connection = pymysql.connect(
            user=self.cred_info['db_user'],
            password=self.cred_info['db_pass'],
            database=self.cred_info['db_name'],
            port=self.cred_info['db_port'],
            host=self.cred_info['db_host']
        )
        return connection




    def execute_SELECT(self, sql):
        conn = self.connectASK()

        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result






