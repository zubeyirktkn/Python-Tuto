#dict
import json

#person_string = {"name":"Ali","languages":["python","C#"]}#dictionary yapısı
person_string = '{"name":"Ali","languages":["python","C#"]}'#json stringi
person_dict = {
    "name":"Ali",
    "languages":["Python","C#"]
}


#JSON string to Dict
#result = json.loads(person_string)
#result = result["name"]

"""
with open("person.json")as f:
    data = json.load(f)
    print(data["name"])
"""
#Dict to JSON string
# result =json.dumps(person_dict)
# with open("person.json","w") as f:
#     json.dump(person_dict,f)

person_dict = json.loads(person_string)

result=json.dumps(person_dict,indent=20,sort_keys=True)#olmadı
print(person_dict)
print(result)





# print(type(result))
# print(result)