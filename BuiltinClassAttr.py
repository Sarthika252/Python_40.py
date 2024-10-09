class Student:
    def __init__(self,name,id,age) :
        self.name=name
        self.id=id
        self.age=age
    def display_details(self):
        print('name: %s,id : %d, age: %d'%(self.name,self.id,self.age))
s=Student("Meera",62,21)
print(s.__doc__)
print(s.__dict__)
print(s.__module__)
