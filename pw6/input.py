# input.py

import os
import gzip
import pickle

def input_students():
    """Input student information: id, name, DoB"""
    num_students = int(input("Enter the number of students in the class: "))
    students = []
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student Date of Birth (DD-MM-YYYY): ")
        students.append((student_id, name, dob))
    return students

def input_courses():
    """Input course information: id, name, credits"""
    num_courses = int(input("Enter the number of courses: "))
    courses = []
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        credits = int(input("Enter course credits: "))
        courses.append((course_id, course_name, credits))
    return courses

def input_marks(students, courses):
    """Input marks for a selected course for all students"""
    marks = {}  # Key: (course_id), Value: {student_id: mark}
    for course_id, course_name, credits in courses:
        print(f"\nInput marks for course: {course_name} (ID: {course_id})")
        course_marks = {}
        for student_id, student_name, _ in students:
            mark = float(input(f"Enter marks for {student_name} (ID: {student_id}): "))
            rounded_mark = round(mark, 1)  # Round to 1 decimal point
            course_marks[student_id] = rounded_mark
        marks[course_id] = course_marks
    return marks

def compress_data(students, courses, marks):
    """Compress and pickle data into students.dat"""
    with gzip.open('students.dat', 'wb') as f:
        pickle.dump((students, courses, marks), f)

def decompress_data():
    """Decompress and load data from students.dat"""
    if os.path.exists('students.dat'):
        with gzip.open('students.dat', 'rb') as f:
            return pickle.load(f)
    else:
        return None
