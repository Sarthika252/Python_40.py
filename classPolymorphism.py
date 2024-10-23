class India:
    def capital(self):
        print("New Delhi is the capital of India.")
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
obj_ind=India()
obj_usa=USA()
for country in(obj_ind,obj_usa):
    country.capital()