# Python program to read
# json fil
import json
# Opening JSON file
f = open('C:/Users/mssen/Desktop/python/practise/sample2.json','r')

# returns JSON object ase
# a dictionary
data = json.load(f)

data['firstName']
data['lastName']
data['gender']
data['age']
data['address']
data['phoneNumbers']

#print(len(["phoneNumbers"]))


print('=======================')
list1=data["address"]
#print(len(list))

# Iterating through the json
for i in range(len(list1)):
    print("StreetAdd:-",list1[i].get("streetAddress"))
    print("City:-",list1[i].get("city"))
    print("State",list1[i].get("state"))
    #print(list[i].get("age"))
    #print(list[i].get("address"))

list2=data["phoneNumbers"]
for j in range(len(list2)):
    print("Type:-",list2[j].get("type"))
    print("Number:-",list2[j].get("number"))

    
# Closing file
f.close()