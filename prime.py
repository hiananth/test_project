num=int(input("enter the number:"))
if num==1:
    print("NOT PRIME")
elif num>1: 
  for i in range(2,num):
      if (num%i==0):
          print("NOT PRIME")
          break
  else:
    print("PRIME NUMBER")
else:
    print("NOT PRIME")          