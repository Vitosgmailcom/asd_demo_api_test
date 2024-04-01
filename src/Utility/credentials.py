
import os

def credentialsDB():
    db_user = os.environ.get('DB_USER')
    db_pass = os.environ.get('DB_PASS')
    db_name = os.environ.get('DB_NAME')
    db_port = os.environ.get('DB_PORT')
    db_host = os.environ.get('DB_HOST')

    if not db_user and not db_pass:
        raise Exception(f"THe DB_USER and DB_PASS must be set up")
    else:
        cred_info = {
            'db_user': db_user,
            'db_pass': db_pass,
            'db_name': db_name,
            'db_port': db_port,
            'db_host': db_host,
        }
        return cred_info


