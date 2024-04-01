
from src.Helper.userHelperDB import USerHelperDB

import pytest

@pytest.mark.tcid99
def test_get_random_user_from_ASK_DB():
    qty = 2
    exec_db = USerHelperDB()
    result_db = exec_db.get_random_user_info_from_DB(qty=qty)

    assert len(result_db) == int(qty), f"Expected qty: '{qty} but returned: '{len(result_db)}''"

    # import pdb; pdb.set_trace()




