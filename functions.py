#function is group of statement for specific task
"""
****** 2 types of function ******
1. Built in function
2. User define function
"""
#factorial function

'''def fectorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n * fectorial(n-1)

a=int(input("enter value"))
print(fectorial(a))'''

#maximum value function

def maxx(l):
    list.sort(l)
    return l[-1]
a=int(input("enter first value"))
b=int(input("enter second value"))
c=int(input("enter third value"))
d=int(input("enter forth value"))
l=[a,b,c,d]

print(maxx(l))