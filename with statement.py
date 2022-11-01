#best way to open and close file automatically

from base64 import b16decode

with open('append.txt','r') as a:
    b=a.read()
print(b)

with open('append.txt','a') as a:
    b=a.write("this is new line")
print(b) #this will not read and print file