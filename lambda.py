x=lambda a:a+10
print(x(5))
y=lambda a,b:a*b
print(y(2,4))
z=lambda a,b,c:a+b+c
print(z(2,3,4))

def fun(n):
    return lambda a:a*n
b=fun(2)
print(b(11))

#sort
list=[("apple",15),("orange",10),("cherry",20),("grapes",5)]
t=sorted(list,key=lambda x:x[1])
print(t)


