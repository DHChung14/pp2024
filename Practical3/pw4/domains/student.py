# student.py

import math

class Student:
    def __init__(self, student_id, name, dob):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob
        self.__marks = {}
        self.__gpa = None

    # Getters
    def get_student_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def get_marks(self):
        return self.__marks

    def set_marks(self, course_id, mark):
        self.__marks[course_id] = mark

    def set_gpa(self, gpa):
        self.__gpa = gpa

    def get_gpa(self):
        return self.__gpa

    # Method to calculate GPA using weighted sum (credits and marks)
    def calculate_gpa(self, courses, marks, credits):
        total_credits = 0
        weighted_sum = 0
        for course_id, mark in self.__marks.items():
            course = next(c for c in courses if c.get_course_id() == course_id)
            course_credits = credits[course_id]
            total_credits += course_credits
            weighted_sum += mark * course_credits
        if total_credits > 0:
            self.__gpa = round(weighted_sum / total_credits, 1)
        else:
            self.__gpa = 0.0