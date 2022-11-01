''' string is sequence of character in quotes'''

a = 'hello,'
b = 'world'

print(a + b)

print(a[0], a[5])

# a[0] == "R" --> does not work you cant assign character of string

#string slicing

print(a[0:4]) #last digit not include

print(a[1:4])

#negative indices

print(a[-1],a[-6])

print(a[-4:-1])

#slicing with skip value

a = 'imtheghost'

print(a[0::2]) #skip value is  2
