if 9>3:
    print("yes")
else:
    print("not")
num=int(input("enter the number"))
if num>0:
    print("positive")
elif num==0:
    print("zero")
else:
    print("negative")
#and   
s=8
t=4
if s>t and t<2:
    print("hai")
else:
    print("error")

#nestedif
num=float(input("enter the value:"))
if num>=0:
    if num==0:
        print("zero")
    else:
        print("positive")
else:
    print("negative")        