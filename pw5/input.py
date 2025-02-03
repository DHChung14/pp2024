# input.py

import os
import zipfile
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
    
    # Write student data to students.txt
    with open("students.txt", "w") as f:
        for student in students:
            f.write(f"{student[0]},{student[1]},{student[2]}\n")
    
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
    
    # Write course data to courses.txt
    with open("courses.txt", "w") as f:
        for course in courses:
            f.write(f"{course[0]},{course[1]},{course[2]}\n")
    
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
    
    # Write marks data to marks.txt
    with open("marks.txt", "w") as f:
        for course_id, course_marks in marks.items():
            for student_id, mark in course_marks.items():
                f.write(f"{course_id},{student_id},{mark}\n")
    
    return marks

def compress_files():
    """Compress the student, course, and marks data into students.dat"""
    with zipfile.ZipFile('students.dat', 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write('students.txt')
        zipf.write('courses.txt')
        zipf.write('marks.txt')
    
    # Clean up the original text files after compression
    os.remove('students.txt')
    os.remove('courses.txt')
    os.remove('marks.txt')

def decompress_files():
    """Decompress students.dat and load the data"""
    with zipfile.ZipFile('students.dat', 'r') as zipf:
        zipf.extract('students.txt')
        zipf.extract('courses.txt')
        zipf.extract('marks.txt')

def load_data_from_files():
    """Load data from the decompressed text files"""
    students = []
    courses = []
    marks = {}

    # Load students from students.txt
    with open("students.txt", "r") as f:
        for line in f:
            student_id, name, dob = line.strip().split(",")
            students.append((student_id, name, dob))
    
    # Load courses from courses.txt
    with open("courses.txt", "r") as f:
        for line in f:
            course_id, course_name, credits = line.strip().split(",")
            courses.append((course_id, course_name, int(credits)))
    
    # Load marks from marks.txt
    with open("marks.txt", "r") as f:
        for line in f:
            course_id, student_id, mark = line.strip().split(",")
            if course_id not in marks:
                marks[course_id] = {}
            marks[course_id][student_id] = float(mark)
    
    return students, courses, marks