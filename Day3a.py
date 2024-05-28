dict={"name":["aasish"],"age":22,"city":"alwar"}
print(dict.pop("city")) #this funciton returns the popped value of the key
#for removing the key value pair from the dictionary
dict["name"].append(["rahul","sachin"])
print(dict)
print(dict)
print(dict["name"])
dt={"dt1":{"name":"ram","age":22},"dt2":{"name":"aashish","age":22}}
print(dt)
print(dt["dt1"]["name"]) #how to acces the element of the nested dictionary
for x,y in dict.items():
    print(x,y)