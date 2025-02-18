

from pages.add_employee import add_employee, read_data_from_excel, del_employee


def test_add_employee(setup):
    driver = setup
    data_output = read_data_from_excel()
    add_employee(driver, data_output)
    del_employee(driver, data_output)
    # verify_employees_added(driver)

