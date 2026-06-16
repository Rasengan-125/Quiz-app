import os
import json
from models import Quiz


def load_quizzes():
    if os.path.exists("quizzes.json"):
        with open("quizzes.json", "w") as f:
            return json.load(f)
    else:
        return []


def save_quizzes(data):
    with open("data/quizzes.json", "w") as f:
        json.dump(data, f, indent=4)


def add_quiz(data):
    i = 1
    letters = ["A", "B", "C", "D"]
    subject = input("Subject: ").strip()
    teacher = input("Teacher: ").strip()
    time = int(input("How long should the test last in seconds: "))
    questions = []
    num = int(input("How many questions are you setting? "))

    while i <= num:
        print("_______________________________________")
        question = input(f"Question {i}\n")
        options = []
        op = 1
        i += 1
        while op <= 4:
            option = input(f"Option {letters[op-1]}: ").strip().capitalize()
            options.append(f"{letters[op-1]}. {option}")
            op += 1
        answer = input("Answer: ").strip().capitalize()
        questions.append({"question": question, "options": options, "answer": answer})

    quiz = Quiz(subject, teacher, questions, time, answers)
    data.append(quiz.__dict__)
    save_quizzes(data)


def take_quiz(data):
    count = 0
    matric = input("Enter matric number: ")
    for item in data:
        subject = item["subject"]
        print(f"{count}. {subject}\n")
        count += 1
