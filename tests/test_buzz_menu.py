from pages.buzz_menu import buzz_menu


def test_buzz_menu(setup):
    driver = setup
    buzz_menu(driver)
    driver.save_screenshot("Reports/buzz.png")