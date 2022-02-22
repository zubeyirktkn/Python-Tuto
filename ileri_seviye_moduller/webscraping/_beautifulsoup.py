html_doc="""

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>İlk Web Sayfam</title>
</head>
<body>
    <h1 id="header">
        Zübeyir's Restourant
    </h1>

    <div class="group1">

        <h2>
            Ana Yemek
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
            <button>
                Ben butonum bas bana
            </button>
        </ul>
    </div>

    <div class="group2">
        <h2>
            Ara Sıcak
    </h2>

        <ul>
            <li>Menü 3</li>
            <li>Menü 4</li>
            <li>Menü 5</li>
            <button>
                Ben butonum bas bana
            </button>
    </ul>
    </div>   

    <img src="fred.jpg" alt="">

    [<a class="sister" href="http://example1.com/elsie" id="link1">Elsie</a>
    [<a class="sister" href="http://example2.com/elsie" id="link2">Elsie</a>
    [<a class="sister" href="http://example3.com/elsie" id="link3">Elsie</a>

</body>
</html>

"""

from bs4 import BeautifulSoup

soup=BeautifulSoup(html_doc,"html.parser")

result=soup.prettify()
result=soup.title
result=soup.head
result=soup.title.string
result=soup.h1.string
result=soup.h2.string
result=soup.find_all("h2")
result=soup.find_all("h2")[0]
result=soup.find_all("h2")[1]
result=soup.div
result=soup.find_all("div")[1]
result=soup.find_all("div")[1].ul.find_all("li")

result=soup.div.findChildren()

result=soup.div.findNextSibling()

result=soup.find_all("a")

for link in result:
    print(link.get("href"))

