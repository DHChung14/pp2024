# output.py

import curses

def list_courses(stdscr, courses):
    stdscr.clear()
    stdscr.addstr("List of Courses:\n")
    if not courses:
        stdscr.addstr("No courses available.\n")
    else:
        for course in courses:
            stdscr.addstr(f"Course ID: {course.get_course_id()}, Course Name: {course.get_name()}\n")
    stdscr.refresh()

def list_students(stdscr, students):
    stdscr.clear()
    stdscr.addstr("List of Students:\n")
    if not students:
        stdscr.addstr("No students available.\n")
    else:
        for student in students:
            stdscr.addstr(f"Student ID: {student.get_student_id()}, Name: {student.get_name()}, Date of Birth: {student.get_dob()}\n")
    stdscr.refresh()

def show_student_marks(stdscr, students):
    student_id = input("Enter student ID: ")
    course_id = input("Enter course ID: ")

    student = next((s for s in students if s.get_student_id() == student_id), None)
    if student and course_id in student.get_marks():
        stdscr.clear()
        stdscr.addstr(f"Marks for student {student_id} in course {course_id}: {student.get_marks()[course_id]}\n")
    else:
        stdscr.addstr(f"No marks found for student {student_id} in course {course_id}.\n")
    stdscr.refresh()

def show_gpa(stdscr, students):
    stdscr.clear()
    students.sort(key=lambda s: s.get_gpa(), reverse=True)
    for student in students:
        stdscr.addstr(f"Student ID: {student.get_student_id()}, GPA: {student.get_gpa()}\n")
    stdscr.refresh()