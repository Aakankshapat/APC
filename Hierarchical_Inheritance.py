# Hierarchical Inheritance

class Person:
    def show_name(self, name):
        print("Name:", name)
        


class Student(Person):
    def study(self):
        print("Student is studying")


class Teacher(Person):
    def teach(self):
        print("Teacher is teaching")


name = input("Enter name: ")


s = Student()

print("---------------------------------")
s.show_name(name)
s.study()

t = Teacher()

t.teach()
