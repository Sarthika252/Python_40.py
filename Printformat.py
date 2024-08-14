#By using format
amount=150.752
print("Amount : ${:.2f}".format(amount))

#By using sep
print("DYPCET",end='@\n')
print('C','S','E',sep=' ')
print('25','02','2004',sep='-')

#By using f-string
name="Kranti"
age=21
print(f"Hello , My name is {name} and I am {age} years old")

#By using %operator
num=20
add=num+10
print("The sum is %d"%add)