def input(n1,n2):
    print("number 1 is: ",n1)
    print("number 2 is: ",n2)
print("Call to function")
input(25,20)

def function(a1,a2=20):
    print("First number is : ",a1)
    print("Second number is : ",a2)

print("Passing only one argument:")
function(40)
print("Passing two arguments:")
function(70,21)