# main.py

import curses
from input import input_student, input_course, input_marks
from output import list_courses, list_students, show_student_marks, show_gpa
from domains.student import Student
from domains.course import Course

class StudentMarkManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.course_credits = {}

    def input_students(self):
        num_students = int(input("Enter the number of students in the class: "))
        for _ in range(num_students):
            student = input_student()
            self.students.append(student)

    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            course = input_course()
            self.courses.append(course)
            # Ask for credits for each course
            credits = int(input(f"Enter credits for course {course.get_name()} (ID: {course.get_course_id()}): "))
            self.course_credits[course.get_course_id()] = credits

    def input_marks(self):
        input_marks(self.students, self.courses)

    def calculate_and_sort_gpas(self):
        for student in self.students:
            student.calculate_gpa(self.courses, self.course_credits)
        self.students.sort(key=lambda s: s.get_gpa(), reverse=True)

    def main(self, stdscr):
        while True:
            stdscr.clear()
            stdscr.addstr("Student Mark Management System\n")
            stdscr.addstr("1. Input students\n")
            stdscr.addstr("2. Input courses\n")
            stdscr.addstr("3. Input marks\n")
            stdscr.addstr("4. List students\n")
            stdscr.addstr("5. List courses\n")
            stdscr.addstr("6. Show student marks\n")
            stdscr.addstr("7. Show GPA and sort by GPA\n")
            stdscr.addstr("8. Exit\n")
            stdscr.addstr("Enter your choice: ")
            stdscr.refresh()

            choice = stdscr.getstr().decode('utf-8')

            if choice == '1':
                self.input_students()
            elif choice == '2':
                self.input_courses()
            elif choice == '3':
                self.input_marks()
            elif choice == '4':
                list_students(stdscr, self.students)
            elif choice == '5':
                list_courses(stdscr, self.courses)
            elif choice == '6':
                show_student_marks(stdscr, self.students)
            elif choice == '7':
                self.calculate_and_sort_gpas()
                show_gpa(stdscr, self.students)
            elif choice == '8':
                break
            else:
                stdscr.addstr("Invalid choice. Please try again.\n")
                stdscr.refresh()
                stdscr.getch()

# Run the system with curses
if __name__ == "__main__":
    system = StudentMarkManagementSystem()
    curses.wrapper(system.main)