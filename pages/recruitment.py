import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located, \
    presence_of_all_elements_located, element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait


def recruitment(driver):
    driver.find_element(By.XPATH, "//span[text()='Recruitment']").click();
    time.sleep(2)
    print(driver.find_element(By.TAG_NAME, "h5"))
    menu = WebDriverWait(driver, 10).until(presence_of_all_elements_located((By.XPATH, "//div[@class='oxd-topbar-body']/nav/ul/li")))
    print(len(menu))
    for m in menu:
        print(m.text)

    rows = WebDriverWait(driver, 10).until(presence_of_all_elements_located((By.XPATH, "//div[@class='oxd-table-body']/div")))
    print(f"Total rows found: {len(rows)}")

    # to use 2 variables use enumerate
    for index , row in enumerate(rows):
        print(row.text.replace("\n", "|"))
        time.sleep(1)
        if "Software Engineer" in row.text or "Payroll Administrator" in row.text:
            print(f"this is the index: {index}")
            driver.find_element(By.XPATH, f"(//i[@class='oxd-icon bi-eye-fill'])[{index+1}]").click()
            # driver.find_element(By.XPATH, f"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[{index+1}]/div/div[7]/div/button[1]/i").click()
            time.sleep(5)
            print(driver.current_url)
            break

    # WebDriverWait(driver, 10).until(element_to_be_clickable(driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-eye-fill'][1]"))).click()
    # # driver.save_screenshot("reports/recruitment.png")
    # print(driver.current_url)
