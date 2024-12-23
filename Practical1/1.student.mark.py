# Student Mark Management System

# Data storage
students = []  # List to store students info
courses = []  # List to store course info
marks = {}  # Dictionary to store student marks for each course

# Function to input number of students
def input_students():
    num_students = int(input("Enter the number of students in the class: "))
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student Date of Birth (YYYY-MM-DD): ")
        students.append((student_id, student_name, student_dob))  # Add student as tuple

# Function to input number of courses
def input_courses():
    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        courses.append((course_id, course_name))  # Add course as tuple

# Function to input marks for a specific student in a specific course
def input_marks():
    student_id = input("Enter student ID: ")
    course_id = input("Enter course ID: ")
    
    # Check if the student exists
    student_found = False
    for student in students:
        if student[0] == student_id:
            student_found = True
            break
    
    # Check if the course exists
    course_found = False
    for course in courses:
        if course[0] == course_id:
            course_found = True
            break
    
    if not student_found:
        print(f"Student with ID {student_id} not found.")
    elif not course_found:
        print(f"Course with ID {course_id} not found.")
    else:
        mark = float(input(f"Enter marks for student {student_id} in course {course_id}: "))
        if student_id not in marks:
            marks[student_id] = {}
        marks[student_id][course_id] = mark

# Function to list all courses
def list_courses():
    if not courses:
        print("No courses available.")
    else:
        print("\nList of Courses:")
        for course in courses:
            print(f"Course ID: {course[0]}, Course Name: {course[1]}")

# Function to list all students
def list_students():
    if not students:
        print("No students available.")
    else:
        print("\nList of Students:")
        for student in students:
            print(f"Student ID: {student[0]}, Name: {student[1]}, Date of Birth: {student[2]}")

# Function to show marks for a specific student in a given course
def show_student_marks():
    student_id = input("Enter student ID: ")
    course_id = input("Enter course ID: ")
    
    if student_id in marks and course_id in marks[student_id]:
        print(f"Marks for student {student_id} in course {course_id}: {marks[student_id][course_id]}")
    else:
        print(f"No marks found for student {student_id} in course {course_id}.")

# Main function to run the program
def main():
    while True:
        print("\nStudent Mark Management System")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks")
        print("4. List students")
        print("5. List courses")
        print("6. Show student marks")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            input_students()
        elif choice == '2':
            input_courses()
        elif choice == '3':
            input_marks()
        elif choice == '4':
            list_students()
        elif choice == '5':
            list_courses()
        elif choice == '6':
            show_student_marks()
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()