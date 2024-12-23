class Student:
    def __init__(self, student_id, name, dob):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob

    # Getters
    def get_student_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    # Method to input student information
    @staticmethod
    def input_student():
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student Date of Birth (YYYY-MM-DD): ")
        return Student(student_id, name, dob)


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

    # Method to input number of students and store them
    def input_students(self):
        num_students = int(input("Enter the number of students in the class: "))
        for _ in range(num_students):
            student = Student.input_student()
            self.students.append(student)

    # Method to input number of courses and store them
    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            course = Course.input_course()
            self.courses.append(course)

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
            if student_id not in self.marks:
                self.marks[student_id] = {}
            self.marks[student_id][course_id] = mark

    # Method to list all courses
    def list_courses(self):
        if not self.courses:
            print("No courses available.")
        else:
            print("\nList of Courses:")
            for course in self.courses:
                print(f"Course ID: {course.get_course_id()}, Course Name: {course.get_name()}")

    # Method to list all students
    def list_students(self):
        if not self.students:
            print("No students available.")
        else:
            print("\nList of Students:")
            for student in self.students:
                print(f"Student ID: {student.get_student_id()}, Name: {student.get_name()}, Date of Birth: {student.get_dob()}")

    # Method to show student marks for a given course
    def show_student_marks(self):
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")

        if student_id in self.marks and course_id in self.marks[student_id]:
            print(f"Marks for student {student_id} in course {course_id}: {self.marks[student_id][course_id]}")
        else:
            print(f"No marks found for student {student_id} in course {course_id}.")

    # Main function to run the program
    def main(self):
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
                self.input_students()
            elif choice == '2':
                self.input_courses()
            elif choice == '3':
                self.input_marks()
            elif choice == '4':
                self.list_students()
            elif choice == '5':
                self.list_courses()
            elif choice == '6':
                self.show_student_marks()
            elif choice == '7':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")


# Run the system
if __name__ == "__main__":
    system = StudentMarkManagementSystem()
    system.main()