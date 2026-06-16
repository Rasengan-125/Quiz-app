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


def add_student(data):
    name = input("Students Name: ").strip()
    matric = input("Students Matric: ").strip()

    student = Student(name, matric)
    data.append(student.__dict__)
    save_students(data)
