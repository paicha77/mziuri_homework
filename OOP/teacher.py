class Teacher:
    def __init__(self, name, subject, salary):
        self.name = name
        self.subject = subject
        self.salary = salary

    def teacher_info(self):
        print(self.name, self.subject, self.salary)


t1 = Teacher("Giorgi", "Math", 1500)
t1.teacher_info()