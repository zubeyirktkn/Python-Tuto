
# for i in range(2,100,11):
#     print(i)

# print(list(range(5,100,10)))

#enumerate

# greeting='Hello There'

# for index,letter in enumerate(greeting):
#     print(f"letter: {letter}, index: {index}")
#     index+=1

#zip
list1 = [1,2,3,4,5]
list2= ['a','b','c','d','e']

print(list(zip(list1,list2)))
for a,b in zip(list1,list2):
    print(a,b)