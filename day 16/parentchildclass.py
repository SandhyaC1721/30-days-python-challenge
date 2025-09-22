# Parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Child class
class Student(Person):
    # Make sure _init_ accepts 3 arguments
    def _init_(self, fname, lname, student_id):
        super()._init_(fname, lname)  # Call parent constructor
        self.student_id = student_id

    def print_student_info(self):
        print(f"Name: {self.firstname} {self.lastname}, Student ID: {self.student_id}")

# Correctly create object with 3 arguments
y = Student("Alice", "Smith", "S12345")

# Call methods
y.printname()             # inherited method
y.print_student_info()    # child method