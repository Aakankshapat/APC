# Multiple inheritnce

class Father:
    def father_job(self, job):
        print("Father's job:", job)


class Mother:
    def mother_job(self, job):
        print("Mother's job:", job)


class Child(Father, Mother):

    def child_name(self, name):
        self.name = name

    def display(self, father_job, mother_job):
        self.father_job(father_job)
        self.mother_job(mother_job)
        print("Child's name:", self.name)


father_job = input("Enter father's job: ")
mother_job = input("Enter mother's job: ")
name = input("Enter child's name: ")

c = Child()

print("----------------------------------------------")

c.child_name(name)
c.display(father_job, mother_job)