import os
with open('sample.txt','w')as file:
    file.write("This is a sample file.")
os.remove('sample.txt')
print("File 'sample.txt' deleted")