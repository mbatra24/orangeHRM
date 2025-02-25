import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from variables.variables import URL, username, password


def app_launch(browserType):
    if browserType.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browserType.lower() == "edge":
        driver = webdriver.Edge()
    elif browserType.lower() == "firefox":
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(URL)
    time.sleep(2)
    return driver

def login(driver):
    # driver = app_launch()
    print(driver.current_url)
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys(username)
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    print(driver.current_url)
    time.sleep(5)
    # return driver

def closedriver(driver):
    driver.quit()

