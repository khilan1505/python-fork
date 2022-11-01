'''
#static methods

sometime we need to define function that doesn't use the self parameter
'''
class Employee():
    @staticmethod
    def greet():
        print("good morning bruuh")

ruturaj = Employee()
ruturaj.greet()