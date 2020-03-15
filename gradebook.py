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
    









    # Declare
    # a
    # AliveStatus
    #
    # class .
    #
    # Requirements: This
    #
    # class must inherit from Enum.It must have two possible symbolic names:
    #
    # Deceased - associated
    # with the value 0
    # Alive - associated
    # with the value 1
    # Declare
    # a
    # Person
    #
    # class .
    #
    # Person
    #
    # class must have the following attributes:
    #
    # first_name
    # last_name
    # dob(date
    # of
    # birth)
    # alive(of
    # type
    # AliveStatus)
    # Person
    #
    # class must also have the following methods:
    #
    # update_first_name
    # update_last_name
    # update_dob
    # update_status
    # Declare
    # an
    # Instructor
    #
    # class .
    #
    # This
    #
    # class must inherit from the Person class.
    #
    # This
    #
    # class must have an additional attribute called instructor_id.
    #
    # The
    # instructor_id
    # attribute
    # must
    # start
    # with the string "Instructor_" followed by a UUID value.
    # Hint: Use
    # super
    #
    # class calls.
    #
    # Declare
    # an
    # Student
    #
    # class .
    #
    # This
    #
    # class must inherit from the Person class.
    #
    # This
    #
    # class must have an additional attribute called student_id.
    #
    # The
    # student_id
    # attribute
    # must
    # start
    # with the string "Student_" followed by a UUID value.
    # Declare
    # a
    #
    # class called ZipCodeStudent.
    #
    # This
    #
    # class must inherit from the Student class.
    #
    # Declare
    # another
    # type
    # of
    # student(prek, middle - school, college, etc).
    #
    # This
    #
    # class must inherit from the Student class.
    #
    # Declare
    # a
    #
    # class called Classroom:
    #
    # Classroom
    #
    # class must have the following attributes:
    #
    # students - a
    # container
    # for students
    #     instructors - a
    #     container
    #     for instructors
    #         Classroom
    #
    #     class must also have the following methods:
    #
    # add_instructor
    # remove_instructor
    # add_student
    # remove_student
    # print_instructors
    # print_students
    # As
    # per
    # usual, be
    # sure
    # to
    # always
    # be
    # practicing
    # TDD.