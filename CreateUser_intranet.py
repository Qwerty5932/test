from login_to_intranet_v1 import driver
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Menu_File_User_CreateUser import navigation

userName = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/div/div[2]/div/div/form/div[3]/div[1]/label/div/div[1]/div[1]/input')
userName.click()
userName.send_keys("qwerty@tyopmail.com")

firstName = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/div/div[2]/div/div/form/div[3]/div[2]/label[1]/div/div[1]/div[1]/input')
firstName.click()
firstName.send_keys("qwerty")

lastName = driver.find_element(by=By.XPATH, value='//html/body/div[1]/div/div/div/div/div[2]/div/div/form/div[3]/div[2]/label[2]/div/div[1]/div[1]/input')
lastName.click()
lastName.send_keys("tag")

time.sleep(60)

#status
print("Elements found")
print("Application title is ",driver.title)
print("Application url is ", driver.current_url)

print("Test Passed.")