import random

#result = dir(random) #directoryu icindekileri gösterir

result=random.random()#0.0-1.0
result = random.uniform(10,100)
result = random.randint(1,100)

names = ['ali','yağmur','deniz','cenk']
result = names[random.randint(0,len(names)-1)]

result= random.choice(names)#listeden rastgele seçer

liste = list(range(10))
random.shuffle(liste)#karıştır verilen listeyi

result=liste

liste = range(100)#range 0 dan o rangee kadar olan sayıları tutar
result=random.sample(liste,3)#verilen listeden 3 random sayı alır


print(result)
