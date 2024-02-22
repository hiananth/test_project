import re
x="rain in spain"
y=re.findall("in",x)#find
print(y)
a=re.search("s",x)#serch
print(a)
print(a.start())
p=re.split("\s",x)#split
print(p)
q=re.split("\s",x,1)#split
print(q)
r=re.sub("\s","4",x)#replace space 
print(r)