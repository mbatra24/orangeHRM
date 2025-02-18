from pages.leave_list_menu import assign_leave


def test_leave_menu(setup):
    driver = setup
    # leave_menu(driver)
    assign_leave(driver)
