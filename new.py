x=open("new.txt","r")
#print(x.read())
#print(x.read(2))
#print(x.readline())
#print(x.readline())
#print(x.readline())
x.close()#close
y=open("new.txt","a")
y.write("\n nice to meet you")
y.close()
z=open("new.txt","r")
#print(z.read())

d=open("new.txt","w")
d.write("hello kochi")
d.close()
e=open("new.txt","r")
print(e.read())

import os
os.remove("new.txt")
