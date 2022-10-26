import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

#Browser chrome
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

#Url intranet QA
driver.get("https://dev-intranet.totalcard.com/")

#insert username login
myUsername = driver.find_element(by=By.XPATH, value='//input[@aria-label="Username"]')
myUsername.send_keys("a@yopmail.com")

#insert password login
myPassword = driver.find_element(by=By.XPATH, value='//input[@aria-label="Password"]')
myPassword.send_keys("1")

#signin button
signIn = driver.find_element(by=By.XPATH, value='//button[@type="submit"]').click()

timeout = 10 # seconds

print("Login to intranet passed")

"""try:
element_present = EC.presence_of_element_located(By.XPATH, value='//div[@class="q-layout q-layout--containerized"]')
WebDriverWait(driver, timeout).until(element_present)
print ("Page is ready!")
except TimeoutException:
print ("Loading took too much time!")
    
time.sleep(60)"""







