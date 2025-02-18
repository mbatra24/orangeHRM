import time

from selenium.webdriver.common.by import By


def left_menu(driver):
    menu = driver.find_elements(By.XPATH, "//ul[@class= 'oxd-main-menu']/li")
    print(len(menu))
    for items in menu:
        print(items.text)
        time.sleep(2)
    