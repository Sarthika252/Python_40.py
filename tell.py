with open('example.txt','r')as file:
    print(file.tell())
    file.read(10)
    print(file.tell())