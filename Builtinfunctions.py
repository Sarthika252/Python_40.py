class Student:
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age
s=Student("Sara",40,21)
print(getattr(s,'name'))
setattr(s,'age',20)
print(getattr(s,'age'))
print(hasattr(s,'id'))
delattr(s,'age')
print(s.age)