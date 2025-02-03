# output.py

import curses

def list_courses(stdscr, courses):
    """List all courses"""
    stdscr.clear()
    stdscr.addstr("\nCourses:\n")
    for course_id, course_name, credits in courses:
        stdscr.addstr(f"{course_id}: {course_name} (Credits: {credits})\n")
    stdscr.refresh()

def list_students(stdscr, students):
    """List all students"""
    stdscr.clear()
    stdscr.addstr("\nStudents:\n")
    for student_id, student_name, student_dob in students:
        stdscr.addstr(f"ID: {student_id}, Name: {student_name}, DoB: {student_dob}\n")
    stdscr.refresh()

def show_student_marks(stdscr, students, marks, course_id):
    """Show student marks for a given course"""
    course_found = False
    for course_id, course_name, credits in courses:
        if course_id == course_id:
            course_found = True
            stdscr.clear()
            stdscr.addstr(f"\nMarks for Course ID: {course_id} - {course_name}\n")
            for student_id, student_name, _ in students:
                mark = marks.get(course_id, {}).get(student_id, "No marks recorded")
                stdscr.addstr(f"Student: {student_name}, Marks: {mark}\n")
            stdscr.refresh()
            break
    if not course_found:
        stdscr.addstr(f"No course found with ID {course_id}.\n")
        stdscr.refresh()

def display_gpas(stdscr, students):
    """Display sorted students by GPA"""
    stdscr.clear()
    stdscr.addstr("\nSorted Students by GPA (Descending Order):\n")
    for student in students:
        stdscr.addstr(f"ID: {student.student_id}, Name: {student.name}, GPA: {student.gpa:.2f}\n")
    stdscr.refresh()
