# Hybrid Inheritance

class Employee:
    def employee_details(self, name):
        self.name = name

    def display_employee(self):
        print("Employee Name:", self.name)


class Manager(Employee):
    def manager_details(self, department):
        self.department = department

    def display_manager(self):
        print("Department:", self.department)


class Developer(Employee):
    def developer_details(self, language):
        self.language = language

    def display_developer(self):
        print("Programming Language:", self.language)


class TeamLead(Manager, Developer):
    def team_details(self, team):
        self.team = team

    def display_team(self):
        print("Team:", self.team)


name = input("Enter employee name: ")
department = input("Enter department: ")
language = input("Enter programming language: ")
team = input("Enter team name: ")

e = TeamLead()
print("------------------------------------")
e.employee_details(name)
e.manager_details(department)
e.developer_details(language)
e.team_details(team)

e.display_employee()
e.display_manager()
e.display_developer()
e.display_team()
print("------------------------------------")