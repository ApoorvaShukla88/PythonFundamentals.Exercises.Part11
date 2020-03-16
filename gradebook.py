from enum import Enum
import uuid


class AliveStatus(Enum):
    def __init__(self):
        Deceased = 0
        Alive = 1


class Person:
    def __init__(self, first_name, last_name, dob, alive):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.alive_status = alive

        def update_first_name():
            pass

        def update_last_name():
            pass

        def update_dob():
            pass

        def update_status():
            pass


class Instructor(Person):
    def __init__(self, instructor_id):
        self.instructor_id = instructor_id.uuid.uuid4


class Student(Person):
    def __init__(self, student_id):
        self.student_id = student_id.uuid.uuid4


class ZipCodeStudent(Student):

    





 class Classroom():
    def __init__(self, student, instructor):
        self.student = student
        self.instructor = instructor

        instructors = []
        students = []

    def add_instructor(self, instructor):
        self.instructors.append(instructor)

    def remove_instructor(self, instructor):
        self.instructors.pop(instructor)

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.pop(student)

    def print_instructors(self,instructor):
        print(instructor)

    def print_students(self, student):
        print(student)


