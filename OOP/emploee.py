class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def employee_info(self):
        print(self.name, self.position, self.salary)


e = Employee("Giorgi", "Manager", 2000)
e.employee_info()