from pages.add_entitlements import add_entitlements, assign_leave, validate_assign_leave


def test_add_entitlements(setup):
    driver= setup
    print("setup complete-calling add entit")
    emp_name = add_entitlements(driver)
    print("add enti complete")
    assign_leave(driver, emp_name)
    validate_assign_leave(driver, emp_name)
