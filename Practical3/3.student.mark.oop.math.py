# 3.student.mark.oop.math.py

import math
import numpy as np
import curses

class Course:
    def __init__(self, course_id, course_name, credits):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits
        self.marks = {}

    def input_marks(self, students, stdscr):
        """Input marks for a selected course for all students"""
        stdscr.clear()
        stdscr.addstr(f"\nInput marks for course: {self.course_name} (ID: {self.course_id})\n")
        stdscr.refresh()
        
        for student in students:
            mark = float(input(f"Enter marks for {student.name} (ID: {student.student_id}): "))
            rounded_mark = math.floor(mark * 10) / 10  # Round down to 1 decimal point
            self.marks[student.student_id] = rounded_mark

    def list(self, stdscr):
        """Display course details"""
        stdscr.addstr(f"{self.course_id}: {self.course_name} (Credits: {self.credits})\n")
        stdscr.refresh()


class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.gpa = 0.0

    def list(self, stdscr):
        """Display student details"""
        stdscr.addstr(f"ID: {self.student_id}, Name: {self.name}, DoB: {self.dob}, GPA: {self.gpa:.2f}\n")
        stdscr.refresh()

    def calculate_gpa(self, courses):
        """Calculate GPA based on weighted marks and course credits"""
        weighted_marks = 0
        total_credits = 0
        for course in courses:
            mark = course.marks.get(self.student_id, 0)
            weighted_marks += mark * course.credits
            total_credits += course.credits
        
        if total_credits > 0:
            self.gpa = weighted_marks / total_credits
        else:
            self.gpa = 0.0


class StudentMarkSystem:
    def __init__(self, stdscr):
        self.students = []
        self.courses = []
        self.stdscr = stdscr

    def input_students(self):
        """Input student information: id, name, DoB"""
        num_students = int(input("Enter the number of students in the class: "))
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student Date of Birth (DD-MM-YYYY): ")
            student = Student(student_id, name, dob)
            self.students.append(student)

    def input_courses(self):
        """Input course information: id, name, credits"""
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            credits = int(input("Enter course credits: "))
            course = Course(course_id, course_name, credits)
            self.courses.append(course)

    def input_marks(self):
        """Input marks for students for each course"""
        for course in self.courses:
            course.input_marks(self.students, self.stdscr)

    def list_courses(self):
        """List all courses"""
        self.stdscr.clear()
        self.stdscr.addstr("\nCourses:\n")
        for course in self.courses:
            course.list(self.stdscr)
        self.stdscr.refresh()

    def list_students(self):
        """List all students"""
        self.stdscr.clear()
        self.stdscr.addstr("\nStudents:\n")
        for student in self.students:
            student.list(self.stdscr)
        self.stdscr.refresh()

    def show_student_marks(self, course_id):
        """Show student marks for a given course"""
        course_found = False
        for course in self.courses:
            if course.course_id == course_id:
                course_found = True
                self.stdscr.clear()
                self.stdscr.addstr(f"\nMarks for Course ID: {course.course_id} - {course.course_name}\n")
                for student in self.students:
                    mark = course.marks.get(student.student_id, "No marks recorded")
                    self.stdscr.addstr(f"Student: {student.name}, Marks: {mark}\n")
                self.stdscr.refresh()
                break

        if not course_found:
            self.stdscr.clear()
            self.stdscr.addstr(f"No course found with ID {course_id}.\n")
            self.stdscr.refresh()

    def calculate_gpas(self):
        """Calculate GPA for each student"""
        for student in self.students:
            student.calculate_gpa(self.courses)

    def sort_students_by_gpa(self):
        """Sort students by GPA in descending order"""
        self.students.sort(key=lambda x: x.gpa, reverse=True)

    def display_gpas(self):
        """Display the list of students with their GPAs"""
        self.stdscr.clear()
        self.stdscr.addstr("\nSorted Students by GPA (Descending Order):\n")
        for student in self.students:
            student.list(self.stdscr)
        self.stdscr.refresh()


def main(stdscr):
    """Main function to run the program"""
    curses.curs_set(0)  # Hide cursor
    system = StudentMarkSystem(stdscr)
    
    system.input_students()
    system.input_courses()
    system.input_marks()
    system.calculate_gpas()
    
    while True:
        system.stdscr.clear()
        system.stdscr.addstr("Menu:\n")
        system.stdscr.addstr("1. List all courses\n")
        system.stdscr.addstr("2. List all students\n")
        system.stdscr.addstr("3. Show student marks for a course\n")
        system.stdscr.addstr("4. Display students sorted by GPA\n")
        system.stdscr.addstr("5. Exit\n")
        system.stdscr.refresh()
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            system.list_courses()
        elif choice == '2':
            system.list_students()
        elif choice == '3':
            course_id = input("Enter course ID to view marks: ")
            system.show_student_marks(course_id)
        elif choice == '4':
            system.sort_students_by_gpa()
            system.display_gpas()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    curses.wrapper(main)