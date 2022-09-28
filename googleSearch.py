import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By

# File path for drivers # TODO: Add Firefox
chromeDriverFilePath = os.getcwd() + "/drivers/chromedriver.exe"

# Instanciate driver and set website to open
chromeDriver = webdriver.Chrome(chromeDriverFilePath)
chromeDriver.get("https://www.google.com")

# Enter "heatwave temperature" in the google search bar
googleInputSearch = chromeDriver.find_element(By.NAME, "q")
googleInputSearch.send_keys("heatwave temperature")

# Wait for keyboard input to finish
time.sleep(3)

# Click search and go to next page
googleSearchButton = chromeDriver.find_element(By.NAME, "btnK")
googleSearchButton.click()