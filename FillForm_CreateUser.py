from login_to_intranet_v1 import driver
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

lastName = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/div/div[2]/div/div/form/div[3]/div[2]/label[2]/div/div[1]/div[1]/input')
lastName.click()
lastName.send_keys("\ue004'")

driver.implicitly_wait(60)
WebDriverWait(driver, 10)

country = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/div/div[2]/div/div/form/div[3]/div[3]/label[1]/div/div[1]')
country.send_keys("\ue015")

time.sleep(60)

#status
print("Elements found")
print("Application title is ",driver.title)
print("Application url is ", driver.current_url)

print("Test Passed.")