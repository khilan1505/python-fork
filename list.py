# list are container to store a value of any data type...

a = [1,3,15,4,5,17,9]

print(a)

print(a[0])

a[0] = 'Ghost' #inserting string to list (valid)

a[1] = True #inserting boolian to to list (valid)

print(a)

#list slicing

print(a[0:4])

#list shorting
b = [1,3,15,4,5,17,9]
b.sort()
print(b)
# list reversing
a.reverse()
print(a)

#appends at end of the list (add)

a.append(3)
print(a)

#insert at index point

a.insert(6,'i am the')
print(a)

#pop delete remove element

a.pop(5)
print(a)

#remove any specific value from list

a.remove(17)
print(a) 