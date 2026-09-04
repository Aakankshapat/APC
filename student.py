class Student:
    _marks = 85
    __password = "1234"

    def _show_marks(self):
        print("Marks:", self._marks)

    def __show_password(self):
        print("Password:", self.__password)

    def show_password(self):
        self.__show_password()


class CollegeStudent(Student):
    def display(self):
        print("College Student")
        print("Protected Marks:", self._marks)
        self._show_marks()


class Result(CollegeStudent):
    def show_result(self):
        print("Result")
        print("Protected Marks:", self._marks)
        self._show_marks()


r = Result()

r.display()
r.show_result()
r.show_password()