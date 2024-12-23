# course.py

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