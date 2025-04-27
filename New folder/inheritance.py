class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Employee(Person):
    def __init__(self, id, name, salary):
        super().__init__(id, name)
        self.salary = salary

    def printdetails(self):
        print(self.id)
        print(self.name)
        print(self.salary)

e = Employee(325010, "Karan", 45000)
e.printdetails()