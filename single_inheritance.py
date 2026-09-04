#single inheritance

class Person:
    def show_name(self, name):
        print("Name:", name)


class Student(Person):
    def study(self, subject):
        print(name, "studies", subject)


name = input("Enter name: ")
subject = input("Enter subject: ")

s = Student()
s.show_name(name)
s.study(subject)