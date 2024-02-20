def sum():
    print("hello world")
sum()
def name(firstname , secondname):
    print(firstname+"  "+secondname)
name("ananth","krishnan")

#arbitary argument
def myfunction(*child):
    print("hello"+child[0])
myfunction("athulliya","akash","ananth")
#ketword argument
def our(kid1,kid2,kid3):
    print("hello"+kid2)
our(kid1="arun",kid2="varun",kid3="vinu")


#arbitary keyword argument
def new(**kid):
    print("hello"+kid["lastname"])
new(firstname="arun",lastname="kumar")

fruits=["apple","orange","cherry"]
def food(sweets):
    for i in sweets:
        print(i)
food(fruits)






def mul(i):
    return 5*i
print(mul(3))

def sum(a,b):
    return a+b
a=int(input("enter a:"))
b=int(input("enter b:"))
print(sum(a,b)) 

  

numbers=[1,2,3,4,5]
def sum(num):
    sum=0
    for i in num:
        sum=sum+i
    print(sum)
sum(numbers)





#20/02/2024   
lis1=[1,2,3,2,4,3,5]
def num(n):
    lis2=[]
    for i in n:
        if i not in lis2:
           lis2.append(i) 
    return lis2
print (num(lis1))







c="i love my country"
def vou(v):
    lel=["a","A","e","E","i","I","o","O","u","U"]
    x=0
    y=0
    for i in v:
        if i in lel:
            x=x+1
        else:
            y=y+1
    print(x)
    print(y)
vou(c)



#factorial
def fact(f):
    if f==1:
        return 1 
    else:
        return(f*fact(f-1))
v=int(input("enter the number:"))
print(fact(v))

str="I Love My CounTrY"
def wrd(l):
    for i in str:
        if i in 


        
    

 
            
    

