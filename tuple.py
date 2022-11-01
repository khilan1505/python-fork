#tuple is immutable data type of python

a = (3,5,7,15,9,3)

print(a)
'''
a = () --> empty tuple
a = (1,) --> tuple with one element add , (coma) to end of value otherwise it takes
            as integer value written in bracket
'''
print(a.count(3)) #count number of value tuple

print(a.index(15)) #print value of that index s

b = 3
b +=2
print(b)