# domains/student.py

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.gpa = 0.0

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

    def list(self):
        """Display student details"""
        return f"ID: {self.student_id}, Name: {self.name}, DoB: {self.dob}, GPA: {self.gpa:.2f}"
