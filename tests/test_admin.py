from pages.admin import admin, top_navigation


def test_admin(setup):
    driver = setup
    admin(driver)
    top_navigation(driver)
