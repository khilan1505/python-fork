#dictonary is collection of key-value pair

myDict={
    "Ruturaj":"Name",
    "Bihola":"Surname",
    "number":[3,9,2000],
    "parents":{"prakashsinh":"father"}
}

print(myDict['Ruturaj'])
print(myDict['parents']['prakashsinh'])

#dictonary --> properties
'''
-->it is unordered
-->it is mutable
-->it is indexed
--> can not contain duplicate keys
'''

#mutability

myDict["number"]=[6,6]
print(myDict['number'])

#methods of dictonary

#print keys of dict.   *type of output is dict keys

print(myDict.keys())

#print values of dict
#print(myDict.values())

#print values of dict.   --> data type is tuple

print(myDict.items())

#update dict add pair of values
a={
    "friend":"khilan",
    "brother":"divyaraj",
    "number":[3,9,2000]
}

myDict.update(a)

print(myDict)
print(myDict.get("number")) #print value associated with key value
print(myDict.get("number2")) #retuns none as number 2 is not present in dictnary
#print(myDict["number2"]) #return error as number 2 is not present in dictnary

