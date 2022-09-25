import json

file=open("C:/Users/mssen/Desktop/python/practise/sample4.json")
data = json.load(file)


list=data["people"]
print(len(data["people"]))

for i in range(len(list)):
    print("first Name:-",list[i].get("firstName"))
    print("Last Name:-",list[i].get("lastName"))
    print("gender:-",list[i].get("gender"))
    print("age:-",list[i].get("age"))
    print("number:-",list[i].get("number"))
file.close()


