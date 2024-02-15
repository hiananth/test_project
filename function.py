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
    