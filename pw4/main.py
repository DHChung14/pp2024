# main.py

import curses
from input import input_students, input_courses, input_marks
from output import list_courses, list_students, show_student_marks, display_gpas
from domains.student_mark_system import StudentMarkSystem

def main(stdscr):
    """Main function to run the program"""
    curses.curs_set(0)  # Hide cursor
    system = StudentMarkSystem()
    
    # Input data
    system.students = input_students()
    system.courses = input_courses()
    system.marks = input_marks(system.students, system.courses)
    
    # Calculate GPA
    system.calculate_gpas()
    
    while True:
        stdscr.clear()
        stdscr.addstr("Menu:\n")
        stdscr.addstr("1. List all courses\n")
        stdscr.addstr("2. List all students\n")
        stdscr.addstr("3. Show student marks for a course\n")
        stdscr.addstr("4. Display students sorted by GPA\n")
        stdscr.addstr("5. Exit\n")
        stdscr.refresh()
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            list_courses(stdscr, system.courses)
        elif choice == '2':
            list_students(stdscr, system.students)
        elif choice == '3':
            course_id = input("Enter course ID to view marks: ")
            show_student_marks(stdscr, system.students, system.marks, course_id)
        elif choice == '4':
            system.sort_students_by_gpa()
            display_gpas(stdscr, system.students)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    curses.wrapper(main)
