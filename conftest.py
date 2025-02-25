import time

import pytest

from functions.functions import app_launch, login, closedriver


@pytest.fixture
def setup():
    # below driver is a variable
    driver = app_launch("chrome")
    login(driver)
    time.sleep(2)
    yield driver
    closedriver(driver)


# # @pytest.fixture
# def setup():
#     # below driver is a variable
#     driver = app_launch()
#     login(driver)
#     time.sleep(2)
#     return driver
#     # closedriver(driver)

