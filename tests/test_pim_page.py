from pages.pim_page import pim_page


def test_pim_page(setup):
    driver = setup
    driver.save_screenshot("Reports/pim.png")
    pim_page(driver)
