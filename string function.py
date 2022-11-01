# string function

a = 'i am the ghost'

print(len(a)) # lenght of string

print(a.endswith('st')) # names  says check it ends with xyz or not

print(a.count('t')) # to count specific charater of string capital and small letter are count differently

print(a.count('the')) #it can also work on word and strings

print(a.capitalize()) # it capitalize first letter of string

print(a.find('the'),a.find('hello')) 
'''it find word or letter in string and locate it(only first occurence),
if there is no match it return -1'''

a = 'i am the ghost the best ghost of all time'

print(a.find('ghost')) #only find fisrt occurence

print(a.replace('the','a')) #it changes all occurence in entire string

####
#######
#escape-sequences
######
####

print('i am the\' ghost \n the\t best ghost of all time\\')

#\' to print ' (single quote)
#\n to insert a new line
#\t to insert a tab
#\\ to print \ (backslash)

