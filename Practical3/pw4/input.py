# input.py

import math
from domains.student import Student
from domains.course import Course

def input_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student Date of Birth (YYYY-MM-DD): ")
    return Student(student_id, name, dob)

def input_course():
    course_id = input("Enter course ID: ")
    name = input("Enter course name: ")
    return Course(course_id, name)

def input_marks(students, courses):
    student_id = input("Enter student ID: ")
    course_id = input("Enter course ID: ")

    # Find the student and course objects
    student = next((s for s in students if s.get_student_id() == student_id), None)
    course = next((c for c in courses if c.get_course_id() == course_id), None)

    if not student:
        print(f"Student with ID {student_id} not found.")
    elif not course:
        print(f"Course with ID {course_id} not found.")
    else:
        mark = float(input(f"Enter marks for student {student_id} in course {course_id}: "))
        mark = math.floor(mark * 10) / 10  # Round down to 1 decimal
        student.set_marks(course_id, mark)