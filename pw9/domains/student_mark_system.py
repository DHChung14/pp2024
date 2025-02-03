# domains/student_mark_system.py

from .student import Student
from .course import Course

class StudentMarkSystem:
    def __init__(self, students=None, courses=None, marks=None):
        self.students = students or []
        self.courses = courses or []
        self.marks = marks or {}

    def input_students(self):
        """Input student information: id, name, DoB"""
        pass  # Moved to input.py

    def input_courses(self):
        """Input course information: id, name, credits"""
        pass  # Moved to input.py

    def input_marks(self):
        """Input marks for students for each course"""
        pass  # Moved to input.py

    def list_courses(self):
        """List all courses"""
        return [course.list() for course in self.courses]

    def list_students(self):
        """List all students"""
        return [student.list() for student in self.students]

    def calculate_gpas(self):
        """Calculate GPA for each student"""
        for student in self.students:
            student.calculate_gpa(self.courses)

    def sort_students_by_gpa(self):
        """Sort students by GPA in descending order"""
        self.students.sort(key=lambda x: x.gpa, reverse=True)
