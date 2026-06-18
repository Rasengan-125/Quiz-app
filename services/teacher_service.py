from models import Teacher
import os
import json
from datetime import datetime


def load_teachers():
    if os.path.exists("data/teachers.json"):
        with open("data/teachers.json", "r") as f:
            content = f.read()
            return json.loads(content) if content else []
    else:
        return []


def save_teachers(teachers):
    with open("data/teachers.json", "w") as f:
        json.dump(teachers, f, indent=4)


def add_teacher():
    teachers = load_teachers()
    name = input("Name: ").strip()
    email = input("Email: ").strip()
    password = input("Password: ").strip()
    emails = [teacher["email"] for teacher in teachers]
    if email in emails:
        q1 = input("Teacher exists.\n C = Create New | Q = Quit\n... ").strip().lower()
        if q1 == "q":
            return
        elif q1 == "c":
            name = input("Name: ")
            email = input("Email: ")
            password = input("Password: ")
            if email in emails:
                print("You no dey hear word")
                return
        else:
            print(f"{q1} is not a valid option")
            return

    teachers.append(Teacher(name, email, password).__dict__)
    save_teachers(teachers)


def delete_teacher():
    email = input("Email: ").strip()
    teachers = load_teachers()
    emails = [teacher["email"] for teacher in teachers]
    if email not in emails:
        print("Teacher not found")
        return
    index = emails.index(email)
    teachers[index]["status"] = "Inactive"
    teachers[index]["resign"] = datetime.now().strftime("%d %B %Y, %I:%M %p")
    save_teachers(teachers)


def show_teachers():
    teachers = load_teachers()
    for n, t in enumerate(teachers, start=1):
        print(f"""
{n}. {t['name']}
    Email   : {t['email']}
    Status  : {t['status']}
    Hired   : {t['hired']}
    Resign  : {t['resign']}
""")


def find_teacher():
    email = input("Email: ").strip()
    teachers = load_teachers()
    emails = [teacher["email"] for teacher in teachers]
    if email not in emails:
        print("Teacher not found")
        return
    index = emails.index(email)
    teacher = teachers[index]
    print(f"""
{teacher['name']}
    Email   : {teacher['email']}
    Status  : {teacher['status']}
    Hired   : {teacher['hired']}
    Resign  : {teacher['resign']}
""")


def teacher_auth():
    validate = False
    email = input("Email: ").strip()
    password = input("Password: ").strip()
    data = load_teachers()
    emails = [teachers["email"] for teachers in data]
    if email not in emails:
        print("Teacher not found")
        return
    index = emails.index(email)
    if data[index]["password"] == password:
        validate = True
        print(f"Welcome {data[index]["name"]}")
    else:
        print("Wrong password")
    return validate
