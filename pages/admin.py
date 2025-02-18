import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


def admin(driver):
    WebDriverWait(driver, 10).until(element_to_be_clickable(driver.find_element(By.XPATH, "//span[text() = 'Admin']"))).click()
    print(driver.current_url)
    time.sleep(2)
    username = driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > div > div:nth-child(2) > input")
    username.send_keys("tester")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".oxd-button--secondary.orangehrm-left-space").click()
    result = WebDriverWait(driver, 10).until(presence_of_element_located((By.XPATH, "//span[text()='No Records Found']"))).text
    print(result)

def top_navigation(driver):
    navigation = driver.find_elements(By.XPATH, "//nav[@class='oxd-topbar-body-nav']/ul/li")
    print(len(navigation))
    for nav in navigation:
        print(nav.text)
        time.sleep(2)



