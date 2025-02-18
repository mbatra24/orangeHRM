import time

from selenium.webdriver.common.by import By


def pim_page(driver):
    driver.find_element(By.XPATH, "//span[text()='PIM']").click()
    time.sleep(2)
    print(driver.current_url)
    # driver.find_element(By.CSS_SELECTOR,"div > div:nth-child(1) > div > div:nth-child(2) > div > div > input").send_keys("Amelia Brown")
    # driver.find_element(By.CSS_SELECTOR,"div.oxd-form-row > div > div:nth-child(5) > div > div:nth-child(2) > div > div > input").send_keys("Jack Ass")
    # driver.find_element(By.CSS_SELECTOR,"div.oxd-table-filter-area > form > div.oxd-form-row > div > div:nth-child(2) > div > div:nth-child(2) > input").send_keys("01715")
    # driver.find_elements(By.CSS_SELECTOR, "div.oxd-select-text-input")[0].send_keys(keys.Keys.ARROW_DOWN+keys.Keys.RETURN)
    # time.sleep(2)
    # driver.find_elements(By.CSS_SELECTOR, "div.oxd-select-text-input")[1].send_keys(keys.Keys.ARROW_DOWN+keys.Keys.ARROW_DOWN+keys.Keys.RETURN)
    # time.sleep(2)
    # driver.find_elements(By.CSS_SELECTOR, "div.oxd-select-text-input")[2].send_keys(keys.Keys.ARROW_DOWN+keys.Keys.ARROW_DOWN+keys.Keys.RETURN)
    # time.sleep(2)
    # driver.find_elements(By.CSS_SELECTOR, "div.oxd-select-text-input")[3].send_keys(keys.Keys.ARROW_DOWN+keys.Keys.ARROW_DOWN+keys.Keys.RETURN)
    # time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,"button.oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space").click()
    time.sleep(3)
    print(driver.find_element(By.CSS_SELECTOR, "div.orangehrm-paper-container > div:nth-child(2) > div > span").text)
