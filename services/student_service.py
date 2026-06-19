import os
import json
from models import Student


def load_students():
    if os.path.exists("data/students.json"):
        with open("data/students.json", "r", encoding="utf-8") as f:
            content = f.read()
            return json.loads(content) if content else []
    else:
        return []


def save_students(data):
    with open("data/students.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def add_student():
    students = load_students()
    matrics = [s["matric"] for s in students]
    name = input("Students Name: ").strip().capitalize()
    matric = input("Students Matric: ").strip()

    if matric in matrics:
        print("Student already exists.")
        return

    student = Student(name, matric)
    students.append(student.__dict__)
    save_students(students)
    print(f"\nSTUDENT ADDED SUCCESSFULLY!!")


def delete_student():
    matric = input("Matric: ").strip()
    students = load_students()
    matrics = [s["matric"] for s in students]
    if matric not in matrics:
        print("Student not found")
        return
    index = matrics.index(matric)

    confirm = (
        input(f"Are you sure you want to deactivate {students[index]['name']}? (Y/N): ")
        .strip()
        .upper()
    )
    if confirm != "Y":
        print("Cancelled")
        return

    students[index]["status"] = "Inactive"
    save_students(students)
    print("Student deactivated")


def show_students():
    data = load_students()
    students = sorted(data, key=lambda x: x.get("average") or 0, reverse=True)

    for n, s in enumerate(students, start=1):
        print(f"""
{n}. {s['name']}
    Matric  : {s['matric']}
    Status  : {s.get('status', 'Active')}
    Scores  : {s['scores']},
    Average : {s.get("average", 0)}
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
    Scores  : {student['scores']},
    Average : {student.get("average", 0)}
""")


def view_my_grades():
    data = load_students()
    while True:
        matric = input("Enter your matric number: ").strip()
        matrics = [s["matric"] for s in data]
        if matric not in matrics:
            print("Student not found")
        else:
            break
    index = matrics.index(matric)
    student = data[index]
    print(f"\nName    : {student['name']}")
    print(f"Matric  : {student['matric']}")
    print(f"Average : {student['average'] or 'No scores yet'}")
    print("\nScores:")
    if student["scores"]:
        for subject, score in student["scores"].items():
            print(f"  {subject} : {score}")
    else:
        print("  No scores yet")
