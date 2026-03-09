class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def get_info(self):
        return f"{self.name} {self.surname}, {self.age}"


s1 = Student("Nika", "Beridze", 16)
print(s1.get_info())

# N2

class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def get_info(self):
        return f"{self.name} {self.surname} {self.age}"


class School:
    def __init__(self, school_name):
        self.school_name = school_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_students(self):
        for s in self.students:
            print(s.get_info())


s1 = Student("Nika", "Beridze", 16)
s2 = Student("Luka", "Giorgadze", 17)

school = School("Public School")
school.add_student(s1)
school.add_student(s2)

school.show_students()

# N3

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def student_info(self):
        print(self.name, self.age, self.grade)


s = Student("Nika", 16, "10th")
s.introduce()
s.student_info()
