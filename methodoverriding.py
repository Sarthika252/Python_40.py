class Bird:
    def flight(self):
        print("Most of the birds can fly but some cannot")
class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")

obj_spr=sparrow()
obj_spr.flight()