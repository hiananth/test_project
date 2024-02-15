a= "india is our country"
value= ["a","A","e","E","i","I","o","O","u","U"]
x=0
y=0
for i in a:
    if i in value:
        x=x+1
    else:
        y=y+1
print(x)
print(y)


a=input("Enter:")#palindrome
b=a[::-1]
if a==b:
    print("yes")
else:
    print("no")

#patten print
for i in range(6):
    for j in range(i):
     print(i,end="   ") 
    print("  ")

#star print
for i in range(8):
    for j in range(i):
     print("*",end="   ")
    print("   ")
    
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end="  ")
    print(" ")
    
children={"child1":{"name":"arun"},
          "child2":{"name":"kapil"},
          "child3":{"name":"arun"}
         }
print(children)

    
    


