# 2.student.mark.oop.py

class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name
        self.marks = {}

    def input_marks(self, students):
        """Input marks for a selected course for all students"""
        print(f"\nInput marks for course: {self.course_name} (ID: {self.course_id})")
        for student in students:
            mark = float(input(f"Enter marks for {student.name} (ID: {student.student_id}): "))
            self.marks[student.student_id] = mark

    def list(self):
        """Display course details"""
        print(f"{self.course_id}: {self.course_name}")


class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

    def list(self):
        """Display student details"""
        print(f"ID: {self.student_id}, Name: {self.name}, DoB: {self.dob}")


class StudentMarkSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

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
        """Input course information: id, name"""
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            course = Course(course_id, course_name)
            self.courses.append(course)

    def input_marks(self):
        """Input marks for students for each course"""
        for course in self.courses:
            course.input_marks(self.students)

    def list_courses(self):
        """List all courses"""
        print("\nCourses:")
        for course in self.courses:
            course.list()

    def list_students(self):
        """List all students"""
        print("\nStudents:")
        for student in self.students:
            student.list()

    def show_student_marks(self, course_id):
        """Show student marks for a given course"""
        course_found = False
        for course in self.courses:
            if course.course_id == course_id:
                course_found = True
                print(f"\nMarks for Course ID: {course.course_id} - {course.course_name}")
                for student in self.students:
                    mark = course.marks.get(student.student_id, "No marks recorded")
                    print(f"Student: {student.name}, Marks: {mark}")
                break

        if not course_found:
            print(f"No course found with ID {course_id}.")


def main():
    """Main function to run the program"""
    system = StudentMarkSystem()
    
    system.input_students()
    system.input_courses()
    system.input_marks()
    
    while True:
        print("\nMenu:")
        print("1. List all courses")
        print("2. List all students")
        print("3. Show student marks for a course")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            system.list_courses()
        elif choice == '2':
            system.list_students()
        elif choice == '3':
            course_id = input("Enter course ID to view marks: ")
            system.show_student_marks(course_id)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()