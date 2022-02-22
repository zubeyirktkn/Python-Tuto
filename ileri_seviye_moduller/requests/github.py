import requests
import json
class Github:
    def __init__(self):
        self.api_url="https://api.github.com"
        self.token="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"
    def getUser(self,username):
        response=requests.get(self.api_url+"/users/"+username)
        return response.json()

    def getRepos(self,username):
        response=requests.get(self.api_url+'/users/'+username+'/repos')
        return response.json()

    def createRepo(self,name):
        response=requests.post(self.api_url+"/user/repos?access_token="+self.token,json={
            "name":name,
            "description":"This is your first repository",
            "homepage":"https://github.com",
            "private":False,
            "has_issues":True,
            "has_projects":True,
            "has_wiki":True
        })
        return response.json()


github = Github()

while True:
    secim=input("1-Find User\n2-Get Repos\n3-Create Repo\n4-Exit\nChoice:")
    
    if secim=="4":
        break
    else:
        if secim == "1":
            username=input("Username:")
            result=github.getUser(username)
            #print(result)
            print(f"name:{result['name']}\npublic repos:{result['public_repos']}\nfollower : {result['followers']}")
        elif secim == "2":
            username=input("Username:")
            result=github.getRepos(username)
            for repo in result:
                print(repo["name"]) 
        elif secim == "3":
            name=input("Repository name:")
            result=github.createRepo(name)
            print(result)
        else:
            print("Wrong choice.")
        
