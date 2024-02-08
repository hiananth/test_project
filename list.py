frds=["rahul","arun","surya","vipin","kiran","jomy"]
frds4=["athulliya","neethu","athira"]
frds2=["anu","binu","sanu"]
print(frds)
print(len(frds))
print(type(frds))
print(frds[1])
print(frds[-1])
print(frds[1:4])
print(frds[:4])
print(frds[4:])

if"arun" in frds:
    print("yes")
else:
    print("no")    
#frds[1]="vinu"  
print(frds)

frds[1:4]="akash","athulliya"
print(frds)

frds[1:4]=["kumar"]
print(frds)

frds.insert(2,"kuku")
print(frds)

frds.insert(2,"sheeba")
print(frds)

frds.insert(5,"kripa") 
print(frds)

frds.append("sabari")
print(frds)

#frds.extend(frds1) #extend
print(frds)

frds.remove("kuku") #remove
print(frds)

frds.pop(0) #pop
print(frds)

frds.pop()
print(frds)

del frds[-1]
print(frds)

frds.clear()
print(frds)

del frds
#print(frds)

fruits=["onion","chilly","tomato"]
veg=["apple","grape","orange"]

num=[1,2,3]
num1=fruits+num
print(num1)
fruits.extend(veg)
print(fruits)
num2=num.copy()
print(num2)
fruits.sort(reverse=True)
print(fruits)

num.sort(reverse=2)
print(num)