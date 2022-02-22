from instagramUserInfo import id,password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#getFollowingstoList idsi verilen kişinin takip ettiklerini bir listeye al
#sonra o listeyi forla gezerek takip et methoduna gönder

class Instagram:
    def __init__(self,id,password):
        self.browser=webdriver.Chrome()
        self.id=id
        self.password=password

    def signIn(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(id)
        passwordinput=self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")
        passwordinput.send_keys(password)
        passwordinput.send_keys(Keys.ENTER)#enterla da girebilirsin ya da click ile tıklarsın girişe
        #self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]").click()
        
        time.sleep(3)
    
    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{id}/")
        followersButton=self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")
        followersButton.click()
        time.sleep(1)
        
        
        dialog=self.browser.find_element_by_css_selector("div[role=dialog] ul")
        followerCount=len(dialog.find_elements_by_css_selector("li"))
        print(f"first count:{followerCount}")

        action = webdriver.ActionChains(self.browser) #tuş için

        #scrolling
        while True:
            dialog.click()#dialoga clicklemezsek spacele inemiyoruz
            for i in range(0,5):#kaydırrrrr 5 defa space
                action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(1)
            newCount=len(dialog.find_elements_by_css_selector("li"))
            if followerCount!=newCount:
                followerCount=newCount
                print(newCount)
                time.sleep(1)
            else:
                break

        followers=dialog.find_elements_by_css_selector("li")

        followerList=[]

        for user in followers:
            link=user.find_element_by_css_selector("a").get_attribute("href")
            followerList.append(link)
        
        with open ("followers.txt","w",encoding="utf-8") as file:
            for item in followerList:
                file.write(item+"\n")

    def followUser(self,id):
        self.browser.get(id)
        time.sleep(2)
        followButton=self.browser.find_element_by_tag_name("button")
        print(followButton.text)
        if followButton.text=="Takip Et" or followButton=="Follow":
            followButton.click()
        else:
            print("Zaten Takiptesin")

"""
    def getFollowingsList(self,id):
        self.browser.get(f"https://www.instagram.com/{id}/")
        followingsButton=self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a")
        followingsButton.click()
        time.sleep(2)
        
        
        dialog=self.browser.find_element_by_css_selector("div[role=dialog] ul")
        followingCount=len(dialog.find_elements_by_css_selector("li"))
        print(f"first count:{followingCount}")

        action = webdriver.ActionChains(self.browser) #tuş için

        #scrolling
        while True:
            dialog.click()#dialoga clicklemezsek spacele inemiyoruz
            for i in range(0,5):#kaydırrrrr 5 defa space
                action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)
            newCount=len(dialog.find_elements_by_css_selector("li"))
            if followingCount!=newCount:
                followingCount=newCount
                print(newCount)
                time.sleep(2)
            else:
                break

        followings=dialog.find_elements_by_css_selector("li")


        for user in followings:
            link=user.find_element_by_css_selector("a").get_attribute("href")
            
        return followings
"""



ig=Instagram(id,password)
ig.signIn()
time.sleep(5)
ig.getFollowers()

"""
for id in ig.getFollowingsList("sy_diee"):
    link=id.find_element_by_css_selector("a").get_attribute("href")
    ig.followUser(link)
"""
