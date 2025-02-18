import time

from pages.recruitment import recruitment


def test_recruitment(setup):
    driver = setup
    recruitment(driver)
    time.sleep(3)
    driver.save_screenshot("reports/newrecruitment.png")
