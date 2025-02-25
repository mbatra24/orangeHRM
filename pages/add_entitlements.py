import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


names = ["a", "b", "c", "d"]

def add_entitlements(driver, wait):
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.XPATH, "//span[text()='Leave']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(//nav[@class='oxd-topbar-body-nav'])/ul/li[3]").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Add Entitlements").click()
    time.sleep(3)
    # to make the code work with the below function we need to call this function
    emp_name = add_entitlements_name(driver,wait)
    return emp_name
    # this css is shorter version of the above. "> means the div is directly under the one before before and if no > then it could be anywhere under the div:'div:nth-child(2) div:nth-child(2) > div > div > input'

def add_entitlements_name(driver, wait):
    ctl_name = driver.find_element(By.CSS_SELECTOR, "form > div:nth-child(2) > div > div > div > div:nth-child(2) > div > div > input")
    ctl_name.click()
    time.sleep(2)
    for name in names:
        ctl_name.send_keys(name)
        time.sleep(2)
        driver.save_screenshot("list.png")
        lst = driver.find_elements(By.CSS_SELECTOR, "div.oxd-autocomplete-dropdown > div")
        print(len(lst))
        display_list_items(driver, lst)
        if len(lst) > 0:
            ctl_name.send_keys(Keys.ARROW_DOWN + Keys.RETURN)
            time.sleep(4)
            emp_name = ctl_name.get_attribute("value")
            print(emp_name)
            time.sleep(4)
            dd = driver.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])[1]")
            dd.click()
            dd.send_keys(Keys.ARROW_DOWN * 5 + Keys.RETURN)
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR,"div:nth-child(3) > div > div:nth-child(3) > div > div:nth-child(2) > input").send_keys("20")
            driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
            time.sleep(2)
            print(wait.until(presence_of_element_located((By.CSS_SELECTOR, ".oxd-text--card-body"))).text)
            wait.until(element_to_be_clickable((By.CSS_SELECTOR, ".oxd-button--secondary.orangehrm-button-margin"))).click()
            driver.save_screenshot("entitlements.png")
            time.sleep(4)
            return emp_name

def display_list_items(driver, lst):
    for i in range(0, len(lst)):
        print(f'lst[{i}].text {lst[i].text}')



# def add_entitlements(driver):
#     wait = WebDriverWait(driver, 10)
#     driver.find_element(By.XPATH, "//span[text()='Leave']").click()
#     time.sleep(2)
#     driver.find_element(By.XPATH, "(//nav[@class='oxd-topbar-body-nav'])/ul/li[3]").click()
#     time.sleep(2)
#     driver.find_element(By.LINK_TEXT, "Add Entitlements").click()
#     time.sleep(3)
#     # this css is shorter version of the above. "> means the div is directly under the one before before and if no > then it could be anywhere under the div:'div:nth-child(2) div:nth-child(2) > div > div > input'
#     name = driver.find_element(By.CSS_SELECTOR, "form > div:nth-child(2) > div > div > div > div:nth-child(2) > div > div > input")
#     name.click()
#     time.sleep(2)
#     name.send_keys("a")
#     time.sleep(2)
#     name.send_keys(Keys.ARROW_DOWN+Keys.RETURN)
#     time.sleep(2)
#     emp_name = name.get_attribute("value")
#     print(emp_name)
#     time.sleep(2)
#     dd = driver.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])[1]")
#     dd.click()
#     dd.send_keys(Keys.ARROW_DOWN*5+Keys.RETURN)
#     time.sleep(2)
#     driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) > div > div:nth-child(3) > div > div:nth-child(2) > input").send_keys("20")
#     driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
#     time.sleep(2)
#     print(wait.until(presence_of_element_located((By.CSS_SELECTOR,".oxd-text--card-body"))).text)
#     wait.until(element_to_be_clickable((By.CSS_SELECTOR,".oxd-button--secondary.orangehrm-button-margin"))).click()
#     driver.save_screenshot("entitlements.png")
#     time.sleep(4)
#     return emp_name

def assign_leave(driver, emp_name):
    # driver.find_element(By.XPATH, "//span[text()='Leave']").click()
    element = WebDriverWait(driver, 10).until(element_to_be_clickable((By.LINK_TEXT, "Assign Leave")))
    element.click()
    print(driver.current_url)
    # time.sleep(3)
    wait = WebDriverWait(driver, 10)
    name = wait.until(presence_of_element_located((By.CSS_SELECTOR, "form > div:nth-child(1) > div > div > div > div:nth-child(2) > div > div > input")))
    # name = driver.find_element(By.CSS_SELECTOR, "form > div:nth-child(1) > div > div > div > div:nth-child(2) > div > div > input")
    # time.sleep(2)
    name.send_keys(emp_name)
    time.sleep(2)
    name.send_keys(Keys.ARROW_DOWN + Keys.RETURN)
    dd = wait.until(presence_of_element_located((By.XPATH, "//div[@class='oxd-select-text-input']")))
    # dd = driver.find_element(By.XPATH, "//div[@class='oxd-select-text-input']")
    dd.send_keys(Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.RETURN)
    # time.sleep(4)
    print(wait.until(presence_of_element_located((By.CSS_SELECTOR, ".orangehrm-leave-balance-text"))).text)
    # print(driver.find_element(By.CSS_SELECTOR, ".orangehrm-leave-balance-text").text)
    # time.sleep(2)
    # start_date = driver.find_element(By.CSS_SELECTOR, ".oxd-input--active:nth-child(1)")
    start_date = driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[1]")
    # start_date.click()
    print("start date field clicked")
    # time.sleep(5)
    start_date.send_keys("2025-20-02")

    time.sleep(2)
    end_date = driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[2]")
    # end_date.click()
    print("end date field clicked")
    time.sleep(2)
    # end_date.send_keys(Keys.BACK_SPACE+Keys.BACK_SPACE+Keys.BACK_SPACE+Keys.BACK_SPACE+Keys.BACK_SPACE)
    end_date.send_keys(Keys.BACK_SPACE * 10)
    time.sleep(3)
    end_date.send_keys("2025-22-02")
    time.sleep(2)
    driver.save_screenshot("enddate.png")
    driver.find_element(By.CSS_SELECTOR, "div > div > form > div.oxd-form-actions > button").click()
    time.sleep(2)
    driver.save_screenshot("assign_leave.png")
    time.sleep(2)


def validate_assign_leave(driver, emp_name):
    driver.find_element(By.LINK_TEXT, "Leave List").click()
    time.sleep(2)
    ctl_name = driver.find_element(By.CSS_SELECTOR,"form > div:nth-child(2) > div > div:nth-child(1) > div > div:nth-child(2) > div > div > input")
    ctl_name.send_keys(emp_name)
    time.sleep(2)
    ctl_name.send_keys(Keys.ARROW_DOWN+Keys.RETURN)

    dd = driver.find_element(By.XPATH,"(//div[@class='oxd-select-text-input'])[1]")
    time.sleep(2)
    dd.send_keys(Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.RETURN)
    driver.find_element(By.CSS_SELECTOR, ".oxd-button--medium.oxd-button--secondary.orangehrm-left-space").click()
    time.sleep(2)
    print(driver.current_url)
    element = WebDriverWait(driver, 10).until(presence_of_element_located((By.XPATH, "//div[@class='orangehrm-header-container']/span")))
    print(element.text)
    driver.save_screenshot("validate.png")

# if the dd was a select box then use the below code
# def click_select_option(driver, option_value):
#     # print("in functions_class - perform_click")
#     try:
#         cbox = Select(driver.find_element(By.XPATH,"(//div[@class='oxd-select-text-input'])[1]"))
#         options = cbox.options
#         for i in range(0, len(cbox.options)):
#             print(cbox.options[i].text, " = ", option_value)
#             if cbox.options[i].text == option_value:
#                 cbox.select_by_index(i)
#                 break
#
#         # el = self.get_element(driver)
#         # el.click()
#         print("Click performed.")
#         time.sleep(2)
#     except:
#         print("Click NOT performed!!!")


