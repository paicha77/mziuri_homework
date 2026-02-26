
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_info(self):
        print(f"სტუდენტი: {self.first_name} {self.last_name}")


class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, index):
        if 0 <= index < len(self.students):
            removed = self.students.pop(index)
            print(f"წაიშალა სტუდენტი: {removed.first_name} {removed.last_name}")
        else:
            print("არასწორი ინდექსი!")

    def show_students(self):
        print(f"\nსკოლა: {self.name}")
        print("სტუდენტები:")
        for student in self.students:
            student.get_info()


school = School("თბილისი N112 საჯარო სკიოლა", "თბილისი, საქართველო")

student1 = Student("ნიკოლოზ", "პაიჭაძე", 16)
student2 = Student("გიორგი", "ბერიძე", 17)
student3 = Student("ანა", "კაკაბაძე", 15)

school.add_student(student1)
school.add_student(student2)
school.add_student(student3)

school.show_students()

school.remove_student(1)

school.show_students()
