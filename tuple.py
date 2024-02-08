z=(1,2,3,4,5)
print(z)
print(len(z))
print(type(z))
print(z[-1])
print(z[1:4])
print(z[3:])
print(z[:3])

if 9 in z:
    print("yes")
else:
    print("not")    
    
print(list(z))  

y=list(z)
print(y)
y[3]=7
print(y)

y.append(10)
print(y)

y.remove(3)
print(y)

print(tuple(y))

del y

#add
a=(9,8,7,6,9)
b=(2,3,4,5)
print(a,b)
print(a+b)

print(b*2)

for i in a:
    print(a)


for i in range(len(a)):
    print(a[i])


i=0
while i<len(a):
    print(a[i])
    i=i+1
a.count(9)
d=a.count(9)
print(d)

e=a.index(9)
print(e)

set