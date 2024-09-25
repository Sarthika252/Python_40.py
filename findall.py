import re
String="Hello my Number is 123456789 and my friend's number is 987654321"
regex='\d+'
match=re.findall(regex,String)
print(match)
name='\D'
m1=re.findall(name,String)
print(m1)
s1='\s'
m2=re.findall(s1,String)
print(m2)