#Using while loop
i=1
while i<=10:
    print(i,end=' \n')
    i+=1

#Using while-else loop
i=11
while i<=20:
    print(i,end=' \n')
    i+=1
else:
    print("Program ends.\n")

#Using for loop
print("String Itetration")
s="HELLO"
for i in s:
    print(i)

#Using for-else
tuple=(3,4,6,8,9,2,3,8,9,7)
for value in tuple:
    if value%2!=0:
     print(value)
else:
    print("These arte the odd numbers present in the tuple")
