#this focus on reusablity of program

'''
***class***

---> class is a blueprint for creating object
---> class have information for creating object

'''
#syntax
'''
class username is written in pascalcase
PascalCase --> ClassName (first letter is capital )
camleCase  --> isNumaric, isFloat (first letter is small then is capital)

#example:

Class Name:
    #methods and variables

'''

'''
Modelling a problem in oops

noun        --->class       --->employee
adjective   --->attribute   --->name,age,salary
verbs       --->methods     --->getSalary(),increament()
'''

'''
#class attribute
an attrbute that belongs to the class rather than perticular object.

Example:

    class Employee:
        company = "google" -[specific to each class]
    
    ruturaj=Employee() -[object identiation]
    employee.company="youtube" -[changing class attribute]



'''

class Employee:
    company="google"

ruturaj = Employee()
bihola = Employee()

print(ruturaj.company)
print(bihola.company)

Employee.company="Youtube"

print(ruturaj.company)

'''
#instant attributes
--- an attribute that belongs to instance (object)

***Instance attributes preferred over class attributes during assignment and retreival***
'''

print("this is example of instance attribute")

print(ruturaj.company)
bihola.company="Microsoft" #instance attribute
print(bihola.company)