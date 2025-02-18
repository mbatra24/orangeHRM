from pages.left_menu import left_menu


def test_left_menu(setup):
    # driver = setup()
    driver = setup
    left_menu(driver)