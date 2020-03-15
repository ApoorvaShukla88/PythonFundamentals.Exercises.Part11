from enum import Enum


class AliveStatus(Enum, enum ):



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
        self.instructor_id = instructor_id


class Student(Person):
    def __init__(self, student_id):
        self.student_id = student_id


class ZipCodeStudent(Student):

class Classroom:

    def add_instructor(self):
        pass
    def remove_instructor(self):
        pass
    def add_student(self):
        pass
    def remove_student(self):
        pass
    def print_instructors(self):
        pass
    def print_students(self):
        pass
    