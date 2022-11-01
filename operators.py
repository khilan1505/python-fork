from ast import operator
import os
from pickle import TRUE
# there are mainly four types of operators in python
'''1 . arithmatic operator
   2 . assignment operator
   3 . comparison operator
   4 . logical operator'''

#arithmatic operators (+,-,*,/,%)
a = 3
b = 4
print(a+b,a*b,a/b,a%b,b%a)

#assignment operator (=,+=,-=,)

a=b
print (a)

a+=1
print (a)

a-=1
print (a)

a *= 2
print (a)

a /= 2
print (a)

#comparison operator (==,>,<,>=,<=,!=)

print(a==b)
print(a>b)
print(a<b)
print(a!=b)
print(a>=b)
print(a<=b)

#logical operator (and , or , not)

print("logical operator")
l = True
k = False
print(l and k)
print(l or k)
print(not k)