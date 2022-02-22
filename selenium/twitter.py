from twitterUserInfo import username,password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Twitter:
    def __init__(self,username,password):
        
        self.browserProfile=webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option("prefs",{"intl.accept_languages":"en,en_US"})
        self.browser=webdriver.Chrome("chromedriver.exe",chrome_options=self.browserProfile)
        self.username=username
        self.password=password

    def signIn(self):
        self.browser.get("https://twitter.com/i/flow/login")
        time.sleep(5)
        usernameInput=self.browser.find_element_by_xpath("//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
        usernameInput.send_keys(self.username)
        usernameInput.send_keys(Keys.ENTER)
        time.sleep(2)
        passwordInput=self.browser.find_element_by_xpath("//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div/input")
        passwordInput.send_keys(self.password)
        #passwordInput.send_keys(Keys.ENTER)
        btnSubmit=self.browser.find_element_by_xpath("//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div")
        btnSubmit.click()
        time.sleep(2)


    def search(self,key):
        searchInput=self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input")
        searchInput.send_keys(key)
        time.sleep(2)
        searchInput.send_keys(Keys.ENTER)
        time.sleep(2)

        list=self.browser.find_element_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]")

        for item in list:
            print(item.text)


        
tw=Twitter(username,password)
tw.signIn()
key="python"
tw.search(key)