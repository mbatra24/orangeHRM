from pages.loginpage import loginpage


def test_loginpage(setup):
    driver = setup
    driver.save_screenshot("Reports/inventory.png")
    loginpage(driver)