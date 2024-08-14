#By using break statement
for string in "Python Loops":
    if string=='L':
        break
    print("current letter: ",string)

#By using continue statement
for string in "Python Loops":
    if string=="o" or string=="p" or string=="t":
        continue
    print("current letter: ",string)

#By using pass statement
def pass_example():
    for i in range(0,10):
        pass
print("Good Bye!")
pass_example()