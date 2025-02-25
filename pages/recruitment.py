import os.path
import time

import pyautogui
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located, \
    presence_of_all_elements_located, element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait


def recruitment(driver):
    driver.find_element(By.XPATH, "//span[text()='Recruitment']").click();
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[text()=' Add ']").click()
    time.sleep(2)
    driver.find_element(By.NAME, 'firstName').send_keys("tester")
    driver.find_element(By.NAME, 'lastName').send_keys("bond")
    driver.find_element(By.XPATH, "//div[@class='oxd-select-text-input']").send_keys("s" + Keys.ARROW_DOWN * 4 + Keys.RETURN)
    driver.find_element(By.XPATH, '(//input[@class = "oxd-input oxd-input--active"])[2]').send_keys("tester.bond@yahoo.com")
    driver.find_element(By.XPATH, "//div[@class='oxd-select-text-input']").send_keys("s" + Keys.ARROW_DOWN * 3 + Keys.RETURN)
    print("finding upload element")
    time.sleep(5)
    upload_input = driver.find_element(By.CSS_SELECTOR, ".oxd-file-button")
    upload_input.click()
    # .send_keys(r'C:\Users\Mannu PC\Documents\Resume\JohnDoe.pdf')
    # file_path = os.path.abspath(r'C:\Users\Mannu PC\Documents\Resume\JohnDoe.pdf')
    # print("file uploading")
    # time.sleep(10)
    # upload_input.send_keys(file_path)
    time.sleep(2)
    pdf_file_path = r"C:\Users\Mannu PC\Documents\xpath_tutorial.txt" #r"C:\Users\Mannu PC\Documents\Resume\JohnDoe.pdf"  # Replace with your actual file path

    pyautogui.write(pdf_file_path)
    pyautogui.press('enter')
    print("file uploaded")
    time.sleep(4)
    print("final print")
    driver.save_screenshot("rec.png")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)
    emp_name = driver.find_element(By.XPATH, "(//p[@class= 'oxd-text oxd-text--p'])[1]").text
    print(emp_name)
    first_nm,last_nm = emp_name.split()
    print(first_nm)
    print(last_nm)
    time.sleep(2)
    # return emp_name
    return first_nm

    # menu = WebDriverWait(driver, 10).until(presence_of_all_elements_located((By.XPATH, "//div[@class='oxd-topbar-body']/nav/ul/li")))
    # print(len(menu))
    # for m in menu:
    #     print(m.text)
    #
    # rows = WebDriverWait(driver, 10).until(presence_of_all_elements_located((By.XPATH, "//div[@class='oxd-table-body']/div")))
    # print(f"Total rows found: {len(rows)}")
    #
    # # to use 2 variables use enumerate
    # for index , row in enumerate(rows):
    #     print(row.text.replace("\n", "|"))
    #     time.sleep(1)
    #     if "Software Engineer" in row.text or "Payroll Administrator" in row.text:
    #         print(f"this is the index: {index}")
    #         driver.find_element(By.XPATH, f"(//i[@class='oxd-icon bi-eye-fill'])[{index+1}]").click()
    #         # driver.find_element(By.XPATH, f"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[{index+1}]/div/div[7]/div/button[1]/i").click()
    #         time.sleep(5)
    #         print(driver.current_url)
    #         break

    # WebDriverWait(driver, 10).until(element_to_be_clickable(driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-eye-fill'][1]"))).click()
    # # driver.save_screenshot("reports/recruitment.png")
    # print(driver.current_url)

def candidates(driver, first_nm):
    driver.find_element(By.LINK_TEXT, 'Candidates').click()
    print("clicked candidates tab")
    time.sleep(3)
    # vac = driver.find_element(By.XPATH, "//div[@class='oxd-select-text-input']").click()
    print("clicked Job title dd")
    time.sleep(3)
    vac = driver.find_element(By.XPATH, "//div[@class='oxd-select-text-input']").send_keys("s"+Keys.ARROW_DOWN*3+Keys.RETURN)
    print("send s letter in job title dd")
    time.sleep(2)
    driver.save_screenshot('job_title.png')

    # below code is to type a name in candidate name field on candidates section
    nm = driver.find_element(By.CSS_SELECTOR, "form > div:nth-child(2) > div > div:nth-child(1) > div > div:nth-child(2) > div > div > input")
    time.sleep(2)
    print("send emp name in name field")
    nm.send_keys(first_nm)
    time.sleep(2)
    nm.send_keys(Keys.ARROW_DOWN+Keys.RETURN)
    time.sleep(2)
    print(" searched by first name in name field and selected")
    driver.save_screenshot("added_name.png")
    # driver.find_element(By.XPATH, "//button[text()='Search']").click()
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(6)
    driver.save_screenshot("emp_searched.png")
    searched_nm = print(driver.find_element(By.CSS_SELECTOR, "div > div.oxd-table-body > div > div > div:nth-child(3) > div").text)
    assert "tester" in first_nm, "employee not added"
    assert "tester" in searched_nm, "employee not added"
    print("Assertion passed!")
    # vac.send_keys("s")
    # time.sleep(2)
    # vac.send_keys(Keys.ARROW_DOWN*3+Keys.RETURN)
    # time.sleep(2)
    # list = driver.find_elements(By.CSS_SELECTOR, "form > div:nth-child(2) > div > div > div > div:nth-child(2) > div > div")
    # time.sleep(2)
    # # list.click()
    # print(len(list))
    # for i in range(1, len(list)+1):
    #     print(f'lst[{i}].text {list[i].text}')
    #     time.sleep(2)
    #     break

