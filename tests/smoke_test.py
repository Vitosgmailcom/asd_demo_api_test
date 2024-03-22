from src.Helper.userHelperDB import USerHelperDB

import pytest

@pytest.mark.tcid99
def test_get_random_user_DB():
    exec = USerHelperDB()
    result = exec.get_random_user_info_from_DB(qty=1)

    # import pdb; pdb.set_trace()

    assert result[0]['group'] == 'APG777', f"Expected group: 'APG777' but DB returned group: '{result[0]['group']}'"




