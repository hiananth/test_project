dict1={"name":"arun","age":12,"place":"kollam"}
print(dict1)
print(dict1["name"])
print(len(dict1))
print(type(dict1))
a=dict1.get("age")
print(a)
#key
b=dict1.keys()
print(b)
#values
c=dict1.values()
print(c)
#items
e=dict1.items()
print(e)
#values change
dict1["age"]=23
print(dict1)
#update
dict1.update({"name":"sarith"})
print(dict1)
#update
dict1.update({"number":23456789})
print(dict1)
#del
dict1.pop("number")
print(dict1)
#del last one
dict1.popitem()
print(dict1)
#del
del dict1["age"]
print(dict1)
#copy
dict2=dict1.copy()
print(dict2)
#clr
dict1.clear()


dict3={"name":"ravi"}
for i in dict3:
    #print(i)
    print(dict3[i])
for i in dict3.values():
    print(i)
for i in dict3.keys():
    print(i)
for i,j in dict3.items():
    print(i,j)    
#nested dict
myfam={
    "child1":{"name":"baby","age":12},
    "child2":{"name":"cia","age":5},
    "child3":{"name":"kaku","age":10}
} 
print(myfam)      

print(myfam["child1"]["age"])