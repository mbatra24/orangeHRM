import time

from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait



def assign_leave(driver):
    driver.find_element(By.XPATH, "//span[text()='Leave']").click()
    element = WebDriverWait(driver, 10).until(element_to_be_clickable((By.LINK_TEXT, "Assign Leave")))
    element.click()
    print(driver.current_url)
    # time.sleep(3)
    wait = WebDriverWait(driver, 10)
    name = wait.until(presence_of_element_located((By.CSS_SELECTOR, "form > div:nth-child(1) > div > div > div > div:nth-child(2) > div > div > input")))
    # name = driver.find_element(By.CSS_SELECTOR, "form > div:nth-child(1) > div > div > div > div:nth-child(2) > div > div > input")
    # time.sleep(2)
    name.send_keys("tester")
    time.sleep(2)
    name.send_keys(Keys.ARROW_DOWN+Keys.RETURN)
    dd = wait.until(presence_of_element_located((By.XPATH, "//div[@class='oxd-select-text-input']")))
    # dd = driver.find_element(By.XPATH, "//div[@class='oxd-select-text-input']")
    dd.send_keys(Keys.ARROW_DOWN+Keys.ARROW_DOWN+Keys.ARROW_DOWN+Keys.ARROW_DOWN+Keys.ARROW_DOWN+Keys.RETURN)
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
    end_date.send_keys(Keys.BACK_SPACE*10)
    time.sleep(3)
    end_date.send_keys("2025-22-02")
    time.sleep(2)
    driver.save_screenshot("enddate.png")







# names = ["James", "tester"]
#
# def leave_menu(driver):
#     driver.find_element(By.XPATH, "//span[text()='Leave']").click()
#     time.sleep(2)
#     # ctl_name = driver.find_element(By.CSS_SELECTOR, "form > div:nth-child(2) > div > div:nth-child(1) > div > div:nth-child(2) > div > div > input")
#     for name in names:
#         ctl_name = driver.find_element(By.CSS_SELECTOR,"form > div:nth-child(2) > div > div:nth-child(1) > div > div:nth-child(2) > div > div > input")
#         ctl_name.send_keys(name)
#         time.sleep(2)
#         ctl_name.send_keys(Keys.ARROW_DOWN + Keys.RETURN)
#         time.sleep(2)
#         print(ctl_name.get_attribute("value"))
#         # in the below I was storing the click in dd variable but wanted to only store element
#         # dd = WebDriverWait(driver, 10).until(element_to_be_clickable((By.XPATH, "(//div[@class='oxd-select-text-input'])[1]"))).click()
#         dd = WebDriverWait(driver, 10).until(element_to_be_clickable((By.XPATH, "(//div[@class='oxd-select-text-input'])[1]")))
#         dd.click()
#         time.sleep(2)
#         print(f"dd = {dd}")
#         dd.send_keys(Keys.ARROW_DOWN+Keys.ARROW_DOWN+Keys.ARROW_DOWN+Keys.ARROW_DOWN+Keys.RETURN)
#         # driver.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])[1]").send_keys(Keys.ARROW_DOWN+Keys.ARROW_DOWN+Keys.ARROW_DOWN+Keys.ARROW_DOWN+Keys.RETURN)
#         time.sleep(2)
#         driver.find_element(By.CSS_SELECTOR, ".oxd-button--medium.oxd-button--secondary.orangehrm-left-space").click()
#         time.sleep(2)
#         print(driver.current_url)
#         time.sleep(2)
#         # print(driver.find_element(By.XPATH, "//div[@class='orangehrm-header-container']/span").text)
#         element = WebDriverWait(driver, 10).until(presence_of_element_located((By.XPATH, "//div[@class='orangehrm-header-container']/span")))
#         print(element.text)
#         driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewLeaveList")
#         time.sleep(3)

