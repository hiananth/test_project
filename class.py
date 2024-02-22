#class & object create
class a:
    x=5
v=a()
print (v.x)



class y:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("hello"+self.name)
z=y("anu",12)
z.display()
print(z.name,z.age)




class person:
    def __init__(self,firstname,secondname):
        self.firstname=firstname
        self.secondname=secondname
    def display(self):
        print(self.firstname,self.secondname)
s=person("Arun","Krishnan")
s.display()
print(s.firstname)

class child(person):
    pass
t=child("Varun","Kiran")
t.display()


        
        
        