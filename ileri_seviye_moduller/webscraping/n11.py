import requests
from bs4 import BeautifulSoup

url="https://www.n11.com/bilgisayar/dizustu-bilgisayar"
html=requests.get(url).content
soup=BeautifulSoup(html,"html.parser")

list=soup.find_all("li",{"class":"column"},limit=1)

for li in list:
    name =li.find("div",{"class":"prodetails"}).title
    link=li.div.a.get("href")
    #oldprice=li.find("div",{"class":"proDetail"}).find_all("a")[0].text.strip().strip("TL")
    #newprice=li.find("div",{"class":"proDetail"}).find_all("a")[1].text.strip().strip("TL")
    
    #print(oldprice)
    #print(newprice)
    print(name)