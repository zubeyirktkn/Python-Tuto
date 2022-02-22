from githubUserInfo import username,password
from selenium import webdriver
import time

class Github:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username=username
        self.password=password
        self.followings=[]


    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        username=self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.username)
        password=self.browser.find_element_by_xpath("//*[@id='password']").send_keys(self.password)

        time.sleep(1)
        
        self.browser.find_element_by_xpath("//*[@id='login']/div[4]/form/div/input[12]").click()#tıklamak

        time.sleep(2)
        #self.browser.close()

    def getFollowings(self):
        self.browser.get(f"https://github.com/{self.username}?tab=following")
        time.sleep(2)

        items=self.browser.find_elements_by_css_selector(".d-table.table-fixed a")
        
        for i in items:
            print(i.text)
        
    def closeBrowser(self):
        self.browser.close()

github=Github(username,password)

github.signIn()
github.getFollowings()
github.closeBrowser()
        