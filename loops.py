#loops repeat sets of statement in program
#2 types of loops... --->while loops --->For loops

#1. while loop
a=0

while a<10:
    #print(a)
    a=a+1

#2. for loop

a=[1,2,3,4,5,6,7,8,9]

for item in a:
    print(item)

#Range is used to generate sequence of numbers

for i in range(10): 
    print("for range(10)",i)
else:
    print("next for loop")

for i in range(2,10):
    print("for range (2,10)",i)

for i in range (2,10,2):
    print("for range (2,10,2)",i)

