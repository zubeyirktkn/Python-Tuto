#themoviedb.org => film dizi arşivi
#themoviedb'nin sunduğu apiyi uygulamanızda kullanınız
#anahtar kelimeye göre arama
#en popüler film listesi
#vizyondaki film listesi

import requests


class theMovieDb:
    def __init__(self):
        self.api_url="https://api.themoviedb.org/3"
        self.api_key="1f5dd660685e90327460d9358c91dac5"

    def getPopulars(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()

    def getSearchResults(self,keyword):
        response=requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&page=1")
        return response.json()

    def getNowPlaying(self):
        response=requests.get(f"{self.api_url}/movie/now_playing?api_key={self.api_key}&language=en-US&page=1")
        return response.json()
    

movieApi=theMovieDb()#nesne türetme
while True:
    secim=input("1-Popular Movies\n2-Now Playing Movies\n3-Search Movies by Keywords\n4-Exit\nChoice:")
    if secim=="4":
        break
    else:
        if secim=="1":
            movies=movieApi.getPopulars()
            for movie in movies["results"]:
                print(movie["title"])

        if secim=="3":
            keyword=input("Keyword:")
            movies=movieApi.getSearchResults(keyword)
            for movie in movies['results']:
                print(movie['name'])

        if secim=="2":
            movies=movieApi.getNowPlaying()
            for movie in movies["results"]:
                print(movie["title"])
                