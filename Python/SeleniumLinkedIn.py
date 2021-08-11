from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import wget

driver = webdriver.Chrome("C:/Users/pulki/Downloads/chromedriver.exe")

driver.get("https://www.linkedin.com/login")

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='session_key']")))
username.clear()
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='session_password']")))
password.clear()

username.send_keys("pulkitsaxena795@gmail.com")
password.send_keys("1lA@11d!!")

button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type='submit']"))).click()

# * To open 'Add a photo and upload it'
# photo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Add a photo')]"))).click()

# upload = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[@class='image-selector__file-upload-label artdeco-button ml1 mv0']"))).click()