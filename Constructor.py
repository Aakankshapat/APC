# constructor destructor

class Student:

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Constructor is called")
        print("Student Name:", self.name)
        print("Student Age:", self.age)

    # Destructor
    def __del__(self):
        print("Destructor is called")
        print("Object is destroyed")


name = input("Enter student name: ")
age = int(input("Enter student age: "))

s = Student(name, age)

del s