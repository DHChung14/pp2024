import math
import numpy as np
import curses

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

    # Method to input student information
    @staticmethod
    def input_student(stdscr):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student Date of Birth (YYYY-MM-DD): ")
        return Student(student_id, name, dob)

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


class Course:
    def __init__(self, course_id, name):
        self.__course_id = course_id
        self.__name = name

    # Getters
    def get_course_id(self):
        return self.__course_id

    def get_name(self):
        return self.__name

    # Method to input course information
    @staticmethod
    def input_course():
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        return Course(course_id, name)


class StudentMarkManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}
        self.course_credits = {}

    # Method to input number of students and store them
    def input_students(self, stdscr):
        num_students = int(input("Enter the number of students in the class: "))
        for _ in range(num_students):
            student = Student.input_student(stdscr)
            self.students.append(student)

    # Method to input number of courses and store them
    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            course = Course.input_course()
            self.courses.append(course)
            # Ask for credits for each course
            credits = int(input(f"Enter credits for course {course.get_name()} (ID: {course.get_course_id()}): "))
            self.course_credits[course.get_course_id()] = credits

    # Method to input marks for a student in a course
    def input_marks(self):
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")

        # Find the student and course objects
        student = next((s for s in self.students if s.get_student_id() == student_id), None)
        course = next((c for c in self.courses if c.get_course_id() == course_id), None)

        if not student:
            print(f"Student with ID {student_id} not found.")
        elif not course:
            print(f"Course with ID {course_id} not found.")
        else:
            mark = float(input(f"Enter marks for student {student_id} in course {course_id}: "))
            mark = math.floor(mark * 10) / 10  # Round down to 1 decimal
            student.set_marks(course_id, mark)

    # Method to list all courses
    def list_courses(self, stdscr):
        stdscr.clear()
        stdscr.addstr("List of Courses:\n")
        if not self.courses:
            stdscr.addstr("No courses available.\n")
        else:
            for course in self.courses:
                stdscr.addstr(f"Course ID: {course.get_course_id()}, Course Name: {course.get_name()}\n")
        stdscr.refresh()

    # Method to list all students
    def list_students(self, stdscr):
        stdscr.clear()
        stdscr.addstr("List of Students:\n")
        if not self.students:
            stdscr.addstr("No students available.\n")
        else:
            for student in self.students:
                stdscr.addstr(f"Student ID: {student.get_student_id()}, Name: {student.get_name()}, Date of Birth: {student.get_dob()}\n")
        stdscr.refresh()

    # Method to show student marks for a given course
    def show_student_marks(self, stdscr):
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")

        student = next((s for s in self.students if s.get_student_id() == student_id), None)
        if student and course_id in student.get_marks():
            stdscr.clear()
            stdscr.addstr(f"Marks for student {student_id} in course {course_id}: {student.get_marks()[course_id]}\n")
        else:
            stdscr.addstr(f"No marks found for student {student_id} in course {course_id}.\n")
        stdscr.refresh()

    # Method to calculate and sort GPA
    def calculate_and_sort_gpas(self):
        for student in self.students:
            student.calculate_gpa(self.courses, self.marks, self.course_credits)
        self.students.sort(key=lambda s: s.get_gpa(), reverse=True)

    # Method to show GPA of students
    def show_gpa(self, stdscr):
        stdscr.clear()
        self.calculate_and_sort_gpas()
        for student in self.students:
            stdscr.addstr(f"Student ID: {student.get_student_id()}, GPA: {student.get_gpa()}\n")
        stdscr.refresh()

    # Main function to run the program
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
                self.input_students(stdscr)
            elif choice == '2':
                self.input_courses()
            elif choice == '3':
                self.input_marks()
            elif choice == '4':
                self.list_students(stdscr)
            elif choice == '5':
                self.list_courses(stdscr)
            elif choice == '6':
                self.show_student_marks(stdscr)
            elif choice == '7':
                self.show_gpa(stdscr)
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