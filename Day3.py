dict={"name":"aashish kumar saini","age":22,"city":"alwar"}

print(dict)
print(type(dict))
print("the length of the dictionary",len(dict))
print(dict["name"])
dict["name"]="aashishkumarsaini"
print(dict)
#we can also print the values of key by the help of the get()

print(dict.get("name"))
dict.update({"rollno":"22eldcs003"})
print(dict)
print(dict.keys()) #to print only the keys

print(dict.values()) #to print only values

print(dict.items()) # to print the comeplete keys with the values




#we can store different data types inside of the any dictionary 
# dict2={
#     "name":"aashish",
#     "age":23,
#     "tuple":(1,3,56,4),
#     "set":{'orange',"apple","banana"},
#     "list":["orange","apple","mango"],
#     "dic":{"a":"aashish","s":"sachin"}

# }

# print(type(dict2))


# print(dict2["dic"])
# print(dict.items()) #prints the key with values
# print(dict.values()) #prints the dictitionary values

# print(dict.keys()) #prints the key of the dictionary
# for i in dict:
#     print(i)
# for i in dict:
#     print(dict[i])
# for i in dict: #printing the key with values by the for loop
#     print(i," : ",dict[i])
# for i in dict.items(): 
#     print(i)