import time

from selenium.webdriver.common.by import By


def buzz_menu(driver):
    driver.find_element(By.XPATH, "//span[text()='Buzz']").click()
    print(driver.current_url)
    time.sleep(2)
    input_text = driver.find_element(By.CSS_SELECTOR, ".oxd-buzz-post-input").send_keys("this is mannu test")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)
    post_text = print(driver.find_element(By.XPATH, "(//div[@class='orangehrm-buzz-post-body']/p)[1]").text)
    assert input_text == post_text, "test failed"