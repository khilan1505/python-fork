'''
"self" parameter
--- it automatic passed with a function call from object


'''

class Employee:
        company="google"
        def getSalary(self):
            print(f"Salary of in {self.company} is {self.salary}")
ruturaj=Employee()
ruturaj.salary = 10000
ruturaj.getSalary() #Employee.getSalary(ruturaj)