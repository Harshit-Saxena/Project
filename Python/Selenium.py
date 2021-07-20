from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import wget

driver = webdriver.Chrome('C:/Users/pulki/Downloads/chromedriver.exe')

# * open the webpage

driver.get("http://www.instagram.com")

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='username']")))
username.clear()
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='password']")))
password.clear()

# * Sending the username and password to be entered

username.send_keys("_pulkit_saxena_")
password.send_keys("akkuakku")

# * Auto clicking login button

button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

# * Pop up 1
not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Not Now')]"))).click()

# * Pop up 2

not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Not Now')]"))).click()

# * Auto clicking search box

searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()

# * search for the hashtag cat

keyword = "#dog"
searchbox.send_keys(keyword)

# * Fixing the double enter prob

link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/" + keyword[1:] + "/')]")))
link.click()

time.sleep(5)
driver.execute_script("window.scrollTo(0,4000);")

time.sleep(5)
images = driver.find_elements_by_tag_name('img')
images = [image.get_attribute('src') for image in images]

path = os.getcwd()
path = os.path.join(path, keyword[1:] + "s")

os.mkdir(path)
path

counter = 0 
for image in images:
    save_as = os.path.join(path, keyword[1:] + str(counter) + ".jpg")
    wget.download(image, save_as)
    counter += 1