import os
import json
from models import Grade
from datetime import datetime
from services.student_service import load_students, save_students


def time_formatter(secs):
    seconds = secs % 60
    minutes = int(secs // 60) % 60
    print(f"You have {minutes} minutes {seconds} seconds")


def marker(ans, correct):
    score = 0
    for a, b in zip(ans, correct):
        if a == b:
            score += 1

    percentage = round((score / len(correct)) * 100, 1) if correct else 0
    return percentage


def load_grades():
    if os.path.exists("data/grades.json"):
        with open("data/grades.json", "r") as f:
            grades = f.read()
            return json.loads(grades) if grades else []
    else:
        return []


def save_score(data):
    with open("data/grades.json", "w") as f:
        json.dump(data, f, indent=2)


def add_scores(matric, subject, score):
    grades = load_grades()
    time = datetime.now().strftime("%d %B %Y, %I:%M %p")
    grade = {"matric": matric, subject: score, "time": time}
    grades.append(grade)

    save_score(grades)


def check_students(matric):
    students = load_students()
    matrics = [s["matric"] for s in students]
    if matric in matrics:
        return True
    else:
        return False


def update_score(matric, subject, score):
    data = load_students()
    students = [s["matric"] for s in data]
    index = students.index(matric)
    avg = (sum(data[index]["scores"].values()) + score) / (
        len(data[index]["scores"]) + 1
    )
    data[index]["scores"][subject] = score
    data[index]["average"] = avg
    save_students(data)


def taken(subject, matric):
    data = load_students()
    matrics = [s["matric"] for s in data]
    index = matrics.index(matric)
    subjects = list(data[index]["scores"].keys())
    if subject in subjects:
        print("You have taken this quiz already")
        return True


def admin_auth():
    allowed = False
    password = input("Enter password: ")
    if password == "adminpassword123":
        allowed = True
    return allowed
