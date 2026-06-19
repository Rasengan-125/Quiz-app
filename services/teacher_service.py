from models import Teacher
import os
import json
from datetime import datetime
from services.quiz_service import load_quizzes, save_quizzes


def load_teachers():
    if os.path.exists("data/teachers.json"):
        with open("data/teachers.json", "r", encoding="utf-8") as f:
            content = f.read()
            return json.loads(content) if content else []
    else:
        return []


def save_teachers(teachers):
    with open("data/teachers.json", "w", encoding="utf-8") as f:
        json.dump(teachers, f, indent=4)


def add_teacher():
    teachers = load_teachers()
    name = input("Name: ").strip().capitalize()
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
    print(f"\n{name} ADDED SUCCESSFULLY")


def delete_teacher():
    email = input("Email: ").strip()
    teachers = load_teachers()
    emails = [teacher["email"] for teacher in teachers]
    if email not in emails:
        print("Teacher not found")
        return
    index = emails.index(email)
    name = teachers[index]["name"]

    confirm = (
        input(f"Are you sure you want to deactivate {name}? (Y/N): ").strip().upper()
    )
    if confirm != "Y":
        print("Cancelled")
        return

    teachers[index]["status"] = "Inactive"
    teachers[index]["resign"] = datetime.now().strftime("%d %B %Y, %I:%M %p")
    save_teachers(teachers)
    print(f"\n{name} DELETED SUCCESSFULLY")


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
        print("")
        print(f"-----------Welcome {data[index]["name"]}-----------")
    else:
        print("")
        print("WRONG PASSWORD")
    return validate, email


def view_quizzes(email):
    teachers = load_teachers()
    quizzes = load_quizzes()

    emails = [t["email"] for t in teachers]
    if email not in emails:
        print("Teacher not found")
        return

    index = emails.index(email)
    teacher_name = teachers[index]["name"]

    my_quizzes = [q for q in quizzes if q["teacher_name"] == teacher_name]

    if not my_quizzes:
        print("You haven't set any quizzes yet")
        return

    for quiz in my_quizzes:
        print(f"\n=== {quiz['subject']} ===")
        for n, q in enumerate(quiz["questions"], start=1):
            print(f"\n{n}. {q['question']}")
            for option in q["options"]:
                print(f"   {option}")
            print(f"   Answer: {q['answer']}")


def delete_quiz(email):
    teachers = load_teachers()
    quizzes = load_quizzes()
    emails = [t["email"] for t in teachers]
    if email not in emails:
        print("Teacher not found")
        return
    index = emails.index(email)
    teacher_name = teachers[index]["name"]
    my_quizzes = [q for q in quizzes if q["teacher_name"] == teacher_name]
    if not my_quizzes:
        print("You haven't set any quizzes yet")
        return
    for n, quiz in enumerate(my_quizzes, start=1):
        print(f"{n}. {quiz['subject']}")
    choice = input("\nSelect quiz to delete (Q to cancel): ").strip().upper()
    if choice == "Q":
        return
    try:
        choice = int(choice)
        if choice < 1 or choice > len(my_quizzes):
            print("Invalid selection")
            return
    except ValueError:
        print("Invalid selection")
        return

    subject_to_delete = my_quizzes[choice - 1]["subject"]
    confirm = (
        input(f"Are you sure you want to delete {subject_to_delete}? (Y/N): ")
        .strip()
        .upper()
    )
    if confirm != "Y":
        print("Cancelled")
        return

    quizzes = [q for q in quizzes if q["subject"] != subject_to_delete]
    save_quizzes(quizzes)
    print(f"{subject_to_delete} deleted successfully")
