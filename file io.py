#types of file
#1. text file 2. binary files

#****** Open is built in function of python ******
#it takes 2 parameter 1.filename 2.mode

a = open("readme.txt", "r")
"""
****
r --> open for read
w --> open for writing
a --> open for append
+ --> open for updating

"rb" is open for read for binary file
"""

'''d = a.read()
print(d)'''
#d = a.read(5)  this specify how many character function will read
#print(d)
d=a.readline()
print(d)
d=a.readline()
print(d)
d=a.readline()
print(d)
a.close()

