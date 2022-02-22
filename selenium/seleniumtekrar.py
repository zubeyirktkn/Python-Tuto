from typing import KeysView
from selenium import webdriver
import time
time.sleep(2)
driver=webdriver.Chrome()
url="https://www.youtube.com/watch?v=KvM5t74lm0I"
driver.get(url)
elem=driver.find_element_by_xpath("/html/body/ytd-app/yt-player-manager").send_keys(KeysView.SPACE)

time.sleep(10)
driver.close()