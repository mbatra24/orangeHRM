import time

from pages.recruitment import recruitment, candidates


def test_recruitment(setup):
    driver = setup
    first_nm = recruitment(driver)
    candidates(driver, first_nm)
    # time.sleep(3)
    driver.save_screenshot("reports/newrecruitment.png")
