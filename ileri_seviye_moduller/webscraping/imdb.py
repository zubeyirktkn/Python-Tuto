import requests
from bs4 import BeautifulSoup

url="https://www.imdb.com/chart/top/?ref_=nv_mv_250"

html=requests.get(url).content#request modülüyle urlnin contentini aldık

soup=BeautifulSoup(html,"html.parser")#bs modülüyle htmli kullanılabilir hale getirdik

list=soup.find("tbody",{"class":"lister-list"}).find_all("tr",limit=10)
#tbodyde lister-list adlı sınıfta 10 tane <tr> bulduk bu tr her 250 film için de mevcut
count=1
for tr in list:
    title=tr.find("td",{"class":"titleColumn"}).find("a").text
    year=tr.find("td",{"class":"titleColumn"}).find("span").text.strip("()")
    rating=tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text
    
    print(f"{count}.{title.ljust(50)} {year} {rating}")#ljust sola yaslıyor 50 char yer veriyor
    
    count+=1
    

