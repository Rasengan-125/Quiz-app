import os
import json
from models import Grade


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
            return json.load(f)
    else:
        return []


def save_score(data):
    with open("data/grades.json", "w") as f:
        json.dump(data, f, indent=2)


def add_scores(matric, subject, score):
    grades = load_grades()
    matric_nums = [g["matric"] for g in grades]
    index = matric_nums.index(matric) if matric in matric_nums else -1

    if index == -1:
        y = Grade(matric, {subject: score})
        grades.append(y.__dict__)
    else:
        x = grades[index]["grades"]
        x[subject] = score

    save_score(grades)
