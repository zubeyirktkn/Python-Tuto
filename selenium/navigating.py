from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()

url="http://github.com"
driver.get(url)


searchInput=driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]")
time.sleep(1)
searchInput.send_keys("python")#klavyeden yazı
time.sleep(1)
searchInput.send_keys(Keys.ENTER)#entera bastırır
time.sleep(2)
#result = driver.page_source #beautiful soup ile yapılabilir

result=driver.find_elements_by_css_selector(".repo-list-item.d-flex p" )

for element in result: 
    print(element.text)

driver.close()