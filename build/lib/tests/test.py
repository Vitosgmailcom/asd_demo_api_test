
import logging as log
import pytest

@pytest.mark.tcid0
def test_test():
    log.info("Hello world")
    log.debug("Debug")

