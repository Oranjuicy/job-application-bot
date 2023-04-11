import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import InvalidSelectorException
from selenium.common.exceptions import NoSuchElementException

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3387219415&f_AL=true&f_WT=2&geoId=104035573&keywords=pyhton%20developer&location=South%20Africa&refresh=true"


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(), options=options)

driver.get(URL)
sign_in_button = driver.find_element(By.CLASS_NAME, "cta-modal__primary-btn")
time.sleep(1.5)
sign_in_button.click()
time.sleep(1.5)
name = driver.find_element(By.ID, "username")
name.send_keys("retief.ryke@gmail.com")
surname = driver.find_element(By.ID, "password")
surname.send_keys("Udum-+H?cb3Z#MD")
sign_in = driver.find_element(By.CLASS_NAME, "btn__primary--large")
sign_in.click()
time.sleep(1.5)
for job in driver.find_elements(By.CLASS_NAME, "job-card-container"):
    job.click()
    time.sleep(1)
    try:
        apply_button = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
        apply_button.click()
        phone_input = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
        phone_input.send_keys("0731024346")
        try:
            submit_button = driver.find_element(By.CLASS_NAME, "")
            if submit_button.text == "Submit application":
                submit_button.click()
        except InvalidSelectorException:
            exit_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            exit_button.click()
            discard_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")
            discard_button.click()
            time.sleep(2)
    except NoSuchElementException:
        pass



