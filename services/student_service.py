import os
import json
from models import Student


def load_students():
    if os.path.exists("data/students.json"):
        with open("data/students.json", "r") as f:
            return json.load(f)
    else:
        return []


def save_students(data):
    with open("data/students.json", "w") as f:
        json.dump(data, f, indent=4)


def add_student():
    students = load_students()
    matrics = [student["matric"] for student in students]
    name = input("Students Name: ").strip()
    matric = input("Students Matric: ").strip()

    if matric in matrics:
        print("Student already exists.")
        return

    student = Student(name, matric)
    students.append(student.__dict__)
    save_students(students)
    print("Added successfully!!")


def delete_student():
    matric = input("Matric: ").strip()
    students = load_students()
    matrics = [student["matric"] for student in students]
    if matric not in matrics:
        print("Student not found")
        return
    index = matrics.index(matric)
    students[index]["status"] = "Inactive"
    save_students(students)


def show_students():
    students = load_students()
    for n, s in enumerate(students, start=1):
        print(f"""
{n}. {s['name']}
    Matric  : {s['matric']}
    Status  : {s.get('status', 'Active')}
    Scores  : {s['scores']}
""")


def find_student():
    matric = input("Matric: ").strip()
    data = load_students()
    matrics = [s["matric"] for s in data]
    if matric not in matrics:
        print("Student not found")
        return
    index = matrics.index(matric)
    student = data[index]
    print(f"""
{student['name']}
    Matric  : {student['matric']}
    Status  : {student.get('status', 'Active')}
    Scores  : {student['scores']}
""")
