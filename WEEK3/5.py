class Student:
    def set_grade(self, grade):
        self.__grade = grade
    def get_grade(self):
        return self.__grade
n = Student ()
n.set_grade(90)
print(n.get_grade())