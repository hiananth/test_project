a=[1,2,3,4,5,6]
for i in a:
    print(i)
b="apple"
for i in b:
    print(i)
    
for i in a:
    print(i)
    if i==3:
        break
#continue
for i in a:
    if i==3: 
        continue   
    print(i)
#range   
for i in range(6):
    print(i)
    
for i in range(2,10):
    print(i) 
for i in range(2,10,3):
    print(i)
    
#while
i=0
while i<6:
    print(i)
    i+=1
    
i=0
while i<6:
    print(i)
    if i==3:
      break    
    i+=1
i=0
while i<6:
    i+=1
    if i==3:
        continue
    print(i)
    

