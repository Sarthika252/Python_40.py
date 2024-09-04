with open('example.txt','r') as file:
    file.seek(6)
    content=file.read()
    print(content)