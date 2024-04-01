
from src.DAO.connectDAO import ConnactDAO

import random

class UserHelperDB(object):
    def __init__(self):
        self.exec = ConnactDAO()

    def get_random_user_ASK(self, qty=1):
        sql = f"SELECT * FROM users WHERE `group`='APG777' order by id ASC LIMIT 10;"
        exec_db = self.exec.execute_SELECT(sql)

        return random.sample(exec_db, qty)

