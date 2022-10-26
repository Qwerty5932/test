from login_to_intranet_v1 import driver
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

#find element
driver.implicitly_wait(60)
driver.find_element(by=By.XPATH, value='//div[@class="q-layout q-layout--containerized"]')
time.sleep(10)

driver.find_element(by=By.XPATH, value='//*[@id="q-app"]/div/div/div/div/div[1]/aside/div/div/div[1]/div/div/div/div/div[1]/div[2]/img').click()

driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/div/div[1]/aside/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[2]/div').click()

driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/div/div[1]/aside/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div[2]').click()

print("Navigation passed")