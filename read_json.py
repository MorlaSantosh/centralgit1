import json
var= open("C:/Users/mssen/Desktop/python/practise/sample4.json")

data= json.load(var)
print(data["people"])
list= data["people"]
print(len(list))

for i in range(len(list)):
    print("first_name:-",list[i].get("firstName"))
    print("last_name:-",list[i].get("lastName"))
    print("gender:-",list[i].get("gender"))
    print("Age:-",list[i].get("age"))
    print("number:-",list[i].get("number"))

    
