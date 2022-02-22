from selenium import webdriver
import time


driver = webdriver.Chrome()

url="http://instagram.com"
driver.get(url)

time.sleep(2)#bekle
driver.maximize_window()
#print(driver.title)
driver.save_screenshot("instagram.com-homepage.png")

url="http://youtube.com"
driver.get(url)

if "youtube" in driver.title:
    driver.save_screenshot("youtube.png")

time.sleep(2)#bekle

driver.back()

time.sleep(2)#bekle

driver.close()