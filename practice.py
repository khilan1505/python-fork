'''a=int(input("enter number one"))
b=int(input("enter number two"))
c=int(input("enter number three"))
d=int(input("enter number four"))

e = [a,b,c,d]

list.sort(e)

print(e[-1])

f="is"

g="Ruturaj is here!"

print(f in g)'''

#multiplication table in reverse



a= int(input("enter which number's table you want"))
'''c=9
for b in range(1,11):
   # print(a,"*",b,"=",a*b)
   print(f"{a}*{b+c}={a*(b+c)}")
   c=c-2'''


'''
b=1
while b<=10:
    print(f"{a}*{b}={a*b}")
    b=b+1'''

#prime numbers
'''c = False
for i in range(2,a):
    if(a%i==0):
        c= True

if c == False:
    print("prime")
else:
    print("not prime")
'''
#factorial
'''fact=1
for i in range(1,a+1):
        fact=fact*i
print(f"fact of {a} is ",fact)'''

# star(*) pattern
'''b=0
for i in range(1,a+1):  
    print(" "*(a-i),"*"*(i+b))
    b=b+1'''

# another star (*) pattern

'''for i in range(0,a):
    if i==0 or i==a-1 :
        print("*"*a)
    else:
        print("*"," "*(a-4),"*")'''

import random

z=random.randint(1,10)
print (z)
