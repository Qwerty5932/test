import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

#Browser chrome
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

#Url intranet QA
driver.get("https://qa-intranet.totalcard.com/")

#insert username login
myUsername = driver.find_element(by=By.XPATH, value='//input[@aria-label="Username"]')
myUsername.send_keys("a@yopmail.com")

#insert password login
myPassword = driver.find_element(by=By.XPATH, value='//input[@aria-label="Password"]')
myPassword.send_keys("1")

#signin button
signIn = driver.find_element(by=By.XPATH, value='//button[@type="submit"]').click()

timeout = 10 # seconds

"""try:
element_present = EC.presence_of_element_located(By.XPATH, value='//div[@class="q-layout q-layout--containerized"]')
WebDriverWait(driver, timeout).until(element_present)
print ("Page is ready!")
except TimeoutException:
print ("Loading took too much time!")
    
time.sleep(60)"""

#find element
driver.implicitly_wait(60)
driver.find_element(by=By.XPATH, value='//div[@class="q-layout q-layout--containerized"]')
time.sleep(10)

driver.find_element(by=By.XPATH, value='//*[@id="q-app"]/div/div/div/div/div[1]/aside/div/div/div[1]/div/div/div/div/div[1]/div[2]/img').click()

driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/div/div[1]/aside/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[2]/div').click()

driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/div/div[1]/aside/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/a/div[2]').click()

WebDriverWait(driver, 10)   

driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div[2]/button/span[2]/span/span').click()

driver.implicitly_wait(60)
WebDriverWait(driver, 10)

driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/div/div[2]/div/div/form/div[3]/div[2]/label[2]/div/div[1]/div[1]/input').click()

driver.implicitly_wait(60)
WebDriverWait(driver, 10)

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



