class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hi, my name is {self.name}.")

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def show_student_id(self):
        print(f"My student ID is {self.student_id}.")

class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

    def show_employee_id(self):
        print(f"My employee ID is {self.employee_id}.")

class TeachingAssistant(Student, Employee):
    def __init__(self, name, student_id, employee_id):
        Student.__init__(self, name, student_id)
        Employee.__init__(self, name, employee_id)

    def teach(self):
        print(f"{self.name} is teaching.")

my_ta = TeachingAssistant("Alice", "12345", "7890")
my_ta.introduce()  # Hi, my name is Alice.
my_ta.show_student_id()  # My student ID is 12345.
my_ta.show_employee_id()  # My employee ID is 7890.
my_ta.teach()  # Alice is teaching.
