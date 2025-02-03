import tkinter as tk
from tkinter import messagebox, simpledialog
from input import input_students, input_courses, input_marks, decompress_data, save_data_periodically
from output import list_courses, list_students, show_student_marks, display_gpas
from domains.student_mark_system import StudentMarkSystem
import threading

# Shared data
students_data = None
courses_data = None
marks_data = None

# Function to start the background saving thread
def start_background_saving_thread():
    """Start a background thread to save data periodically."""
    save_thread = threading.Thread(target=save_data_periodically, daemon=True)
    save_thread.start()

# GUI callback to input students
def input_students_gui():
    global students_data
    students_data = input_students()
    messagebox.showinfo("Info", "Students input successful.")

# GUI callback to input courses
def input_courses_gui():
    global courses_data
    courses_data = input_courses()
    messagebox.showinfo("Info", "Courses input successful.")

# GUI callback to input marks
def input_marks_gui():
    global marks_data
    if students_data and courses_data:
        marks_data = input_marks(students_data, courses_data)
        messagebox.showinfo("Info", "Marks input successful.")
    else:
        messagebox.showerror("Error", "Please input students and courses first.")

# GUI callback to show students list
def show_students_gui():
    if students_data:
        list_students_gui()
    else:
        messagebox.showerror("Error", "No student data available.")

# Function to list students in the GUI
def list_students_gui():
    student_window = tk.Toplevel(root)
    student_window.title("Students List")
    
    student_listbox = tk.Listbox(student_window)
    for student in students_data:
        student_listbox.insert(tk.END, f"{student[1]} (ID: {student[0]})")
    
    student_listbox.pack(fill=tk.BOTH, expand=True)

# GUI callback to show courses list
def show_courses_gui():
    if courses_data:
        list_courses_gui()
    else:
        messagebox.showerror("Error", "No course data available.")

# Function to list courses in the GUI
def list_courses_gui():
    course_window = tk.Toplevel(root)
    course_window.title("Courses List")
    
    course_listbox = tk.Listbox(course_window)
    for course in courses_data:
        course_listbox.insert(tk.END, f"{course[1]} (ID: {course[0]})")
    
    course_listbox.pack(fill=tk.BOTH, expand=True)

# GUI callback to show marks for a course
def show_marks_gui():
    if marks_data:
        course_id = simpledialog.askstring("Course ID", "Enter course ID to view marks:")
        show_student_marks_gui(course_id)
    else:
        messagebox.showerror("Error", "No marks data available.")

# Function to show student marks for a given course
def show_student_marks_gui(course_id):
    marks_window = tk.Toplevel(root)
    marks_window.title(f"Marks for Course {course_id}")

    marks_listbox = tk.Listbox(marks_window)
    
    if course_id in marks_data:
        for student_id, mark in marks_data[course_id].items():
            marks_listbox.insert(tk.END, f"Student ID: {student_id}, Marks: {mark}")
    else:
        marks_listbox.insert(tk.END, "No marks found for this course.")
    
    marks_listbox.pack(fill=tk.BOTH, expand=True)

# GUI callback to show GPA of students
def show_gpas_gui():
    if students_data:
        system = StudentMarkSystem(students=students_data, courses=courses_data, marks=marks_data)
        system.calculate_gpas()
        display_gpas_gui(system.students)
    else:
        messagebox.showerror("Error", "No student data available.")

# Function to display students' GPAs
def display_gpas_gui(students):
    gpa_window = tk.Toplevel(root)
    gpa_window.title("Students GPA")
    
    gpa_listbox = tk.Listbox(gpa_window)
    for student in students:
        gpa_listbox.insert(tk.END, f"{student[1]} (ID: {student[0]}), GPA: {student.gpa}")
    
    gpa_listbox.pack(fill=tk.BOTH, expand=True)

# Main window setup
root = tk.Tk()
root.title("Student Mark Management System")

# Load data if exists
data = decompress_data()
if data:
    students_data, courses_data, marks_data = data
else:
    messagebox.showinfo("Info", "No existing data found. Please input new data.")

# Start background saving thread
start_background_saving_thread()

# Buttons to input data and display info
tk.Button(root, text="Input Students", command=input_students_gui).pack(fill=tk.X)
tk.Button(root, text="Input Courses", command=input_courses_gui).pack(fill=tk.X)
tk.Button(root, text="Input Marks", command=input_marks_gui).pack(fill=tk.X)
tk.Button(root, text="Show Students", command=show_students_gui).pack(fill=tk.X)
tk.Button(root, text="Show Courses", command=show_courses_gui).pack(fill=tk.X)
tk.Button(root, text="Show Marks", command=show_marks_gui).pack(fill=tk.X)
tk.Button(root, text="Show GPAs", command=show_gpas_gui).pack(fill=tk.X)

# Exit Button
tk.Button(root, text="Exit", command=root.quit).pack(fill=tk.X)

# Start Tkinter main loop
root.mainloop()
