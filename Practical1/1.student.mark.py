# 1.student.mark.py

# Student marks management system using tuples, lists, and dictionaries

def input_students():
    """Input student information: id, name, DoB"""
    students = []
    num_students = int(input("Enter the number of students in the class: "))
    
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student Date of Birth (DD-MM-YYYY): ")
        students.append((student_id, name, dob))
    
    return students

def input_courses():
    """Input course information: id, name"""
    courses = []
    num_courses = int(input("Enter the number of courses: "))
    
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        courses.append((course_id, course_name))
    
    return courses

def input_marks(students, courses):
    """Input marks for a selected course for all students"""
    marks = {}  # Key: (course_id), Value: {student_id: mark}
    
    for course_id, course_name in courses:
        print(f"\nInput marks for course: {course_name} (ID: {course_id})")
        course_marks = {}
        
        for student_id, student_name, _ in students:
            mark = float(input(f"Enter marks for {student_name} (ID: {student_id}): "))
            course_marks[student_id] = mark
        
        marks[course_id] = course_marks
    
    return marks

def list_courses(courses):
    """List all courses"""
    print("\nCourses:")
    for course_id, course_name in courses:
        print(f"{course_id}: {course_name}")

def list_students(students):
    """List all students"""
    print("\nStudents:")
    for student_id, student_name, student_dob in students:
        print(f"ID: {student_id}, Name: {student_name}, DoB: {student_dob}")

def show_student_marks(marks, students, course_id):
    """Show student marks for a given course"""
    if course_id not in marks:
        print(f"No marks found for course ID {course_id}.")
        return
    
    course_marks = marks[course_id]
    print(f"\nMarks for Course ID: {course_id}")
    
    for student_id, student_name, _ in students:
        mark = course_marks.get(student_id, "No marks recorded")
        print(f"Student: {student_name}, Marks: {mark}")

def main():
    """Main function to run the program"""
    students = input_students()
    courses = input_courses()
    marks = input_marks(students, courses)
    
    while True:
        print("\nMenu:")
        print("1. List all courses")
        print("2. List all students")
        print("3. Show student marks for a course")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            list_courses(courses)
        elif choice == '2':
            list_students(students)
        elif choice == '3':
            course_id = input("Enter course ID to view marks: ")
            show_student_marks(marks, students, course_id)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()