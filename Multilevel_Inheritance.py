# Multilevel Inheritance

class Employee:
    def employee_details(self, name, salary):
        self.name = name
        self.salary = salary

    def display_employee(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):
    def manager_details(self, department):
        self.department = department

    def display_manager(self):
        print("Department:", self.department)


class SeniorManager(Manager):
    def senior_manager_details(self, experience):
        self.experience = experience

    def display_senior_manager(self):
        print("Experience:", self.experience)


name = input("Enter employee name: ")
salary = input("Enter salary: ")
department = input("Enter department: ")
experience = input("Enter experience: ")

e = SeniorManager()

print("------------------------------------")
e.employee_details(name, salary)
e.manager_details(department)
e.senior_manager_details(experience)

e.display_employee()
e.display_manager()
e.display_senior_manager()
print("------------------------------------")