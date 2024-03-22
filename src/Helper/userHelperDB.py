from src.DAO.connectDAO import ConnactDAO

import random

class USerHelperDB(object):
    def __init__(self):
        self.db_connect = ConnactDAO()


    def get_random_user_info_from_DB(self, qty=1):

        sql = f"SELECT * FROM users WHERE `group`='APG777' order by id ASC LIMIT 10;"
        result = self.db_connect.execute_SELECT(sql)

        return random.sample(result, qty)

