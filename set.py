e={"apple","orange","cherry","apple"}
t={"onion","chilly"}
print(e)
print(len(e))
print(type(e))
for i in e:
    print(i)
print("apple" in e)

e.add ("banana")#add
print(e)

e.update (t)
print(e)

e.remove ("banana")
print(e)

#e.remove("banana")
#print(e)

e.discard("chilly")
print(e)

e.discard("chilly")
print(e)

r=e.pop()
print(r)

print(e)

#difference
set1={1,2,3,4,5,14,26,56,89,90,23,10,55}
set2={89,90,23,10,55}
#set3=set1.difference(set2)
#print(set3)
#set2.difference_update(set1)
#print(set2)

set4=set2.intersection(set1)
print(set4)

set5=set2.issubset(set1)
print(set5)

set6=set1.issuperset(set2)
print(set6)

set7=set1.issubset(set1)
print(set7)



