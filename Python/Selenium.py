from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import wget

# / TODO:

# * Import chromedriver after downloading by entering its location  (line 16)
# * Specify the url of the site you want to launch. In this case it instagram (line 20)
# * Make variables for username and password and check their html tag name in inspect mode (line 23-26)
# * send_keys using the variables for the data to be entered (line 31-32)
# * Variable created to auto click login button (line 38)
# * Variable created to auto click Not Now on pop ups (line 41-44)
# * Variable to select the searchBox (line 49)
# * Keyword to be entered into the searchBox (line 55)
# * Keyword [0:] to click the 0th index option to be clicked and loaded (line 60)
# * execute_script to scroll down from 0 to X (line 68)
# * Find the elements of tag 'img' (line 71)
# * Get their attribute 'src' (line 72)
# * Create a path and directory (line 74-79)
# * For loop to loop through all the img in images and download them onto system (line 83)




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

# * Search for anything with exact username
keyword = input("Enter the exact username or name to search : ")
searchbox.send_keys(keyword)

# * Fixing the double enter prob
time.sleep(2)
link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/" + keyword[0:] + "/')]"))).click()

# ? keyword [1:] shouldnt be used cz when we put the exact username it will be the 0th index and we skip it by the keywrd[1:]...I did it on my own and figured that it needs to be keyword [0:] to open anyone page if you know the exact username

time.sleep(5)
driver.execute_script("window.scrollTo(0,5000);")

time.sleep(2)
images = driver.find_elements_by_tag_name('img')
images = [image.get_attribute('src') for image in images]

path = os.getcwd()
path = os.path.join(path, keyword[0:] + "-")

# ? It has to be keyword [0:] so that whn it makes the folder it doesnt exclude the 1st letter 

os.mkdir(path)

counter = 0    
for image in images:
    save_as = os.path.join(path, keyword[0:] + str(counter) + ".jpg")  # This is us naming the individual files in the folder like dog 0 dog 1 dog 2....counter needs to be typecasted into str for it to be concatenated 
    wget.download(image, save_as)  # image is each img at every index in images and we want to download every image with the name in save_as
    counter += 1