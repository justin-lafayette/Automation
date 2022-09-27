from ast import Try
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")
# sleepyTime = time.sleep(1)

swagLabsLockedMessage = driver.find_element(By.CLASS_NAME, "error-message-container")
# if swagLabsLockedMessage.is_displayed():
#     print("Error not here yet")

# Say what this chunk does
swagLabsUsernameField = driver.find_element(By.ID, "user-name")
swagLabsUsernameField.send_keys("locked_out_user")
# sleepyTime
time.sleep(1)

# Say what this chunk does
swagLabsPasswordField = driver.find_element(By.ID, "password")
swagLabsPasswordField.send_keys("secret_sauce")
# sleepyTime
time.sleep(1)

# Say what this chunk does
swagLabsLogin = driver.find_element(By.ID, "login-button")
swagLabsLogin.click()

# Say what this chunk does
# swagLabsLockedMessage = driver.find_element(By.CLASS_NAME, "error-message-container")
assert "Epic sadface" in swagLabsLockedMessage.text

# if swagLabsLockedMessage.is_displayed():
#     print("Error found")

try:
    swagLabsLockedMessage.is_displayed()
    print("Message found")
except:
    print("An exception")

try:
    swagLabsLockedMessage.ElementNotVisibleException
    print("DOM element not found")
except:
    print("DOM element found")