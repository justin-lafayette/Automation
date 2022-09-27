from multiprocessing.connection import wait
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")

googleInputSearch = driver.find_element(By.NAME, "q")
googleInputSearch.send_keys("heatwave temperature")

time.sleep(3)

googleSearchButton = driver.find_element(By.NAME, "btnK")
googleSearchButton.click()