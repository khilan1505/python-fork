'''
### set is collection of non repetitive element
'''
a ={1,2,7,5,2}

print(a)
print(type(a))

b={} #this will be taken as empty dict not a empty set
print(type(b))

#this how to create empty set
c=set()
print(c)
print(type(c))

#add value to set

c.add((1,2,3,3,4,7,5)) #tuple adding to set 
c.add("tom")
print(c)

#can't add list or/and dictnary in sets

#remove any value from set

c.remove("tom")

#print lenght of set

print(len(c))

a.pop() #remove arbitary element from set (random)

print(a) 

#a.clear() #clear set

#print(a)

a=a.union({2,5,9})

print(a)

a=a.intersection({2,5,1})

print(a)
