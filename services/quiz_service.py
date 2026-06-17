import os
import json
import time
from models import Quiz
from services.helpers import time_formatter, marker, add_scores


def load_quizzes():
    if os.path.exists("data/quizzes.json"):
        with open("data/quizzes.json", "r") as f:
            return json.load(f)
    else:
        return []


def save_quizzes():
    quizes = load_quizzes()
    with open("data/quizzes.json", "w") as f:
        json.dump(quizes, f, indent=4)


def add_quiz():
    data = load_quizzes()
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

    quiz = Quiz(subject, teacher, time, questions)
    data.append(quiz.__dict__)
    save_quizzes()


def take_quiz():
    data = load_quizzes()
    matric = input("Enter matric number: ")
    for n, item in enumerate(data, start=1):
        subject = item["subject"]
        print(f"{n}. {subject}\n")  # Quiz list

    course = (
        int(input("Select the course you want to take by number: ")) - 1
    )  # Quiz selection

    if course < 0 or course > len(data):
        return "Fuck you"

    quiz = data[course]
    sub = quiz["subject"]
    input("Are you ready? (Enter to continue)")
    q_time = int(quiz["time"])
    time_formatter(q_time)

    # Questions time

    start = time.time()
    answers = []
    for n, question in enumerate(quiz["questions"], start=1):
        if time.time() - start >= q_time:
            break
        print("-----------------------------")
        print(f"{n}. {question["question"]}")
        for option in question["options"]:
            print(option)
        print("")
        ans = input("Answer: ").capitalize().strip()
        answers.append(ans)

    # Marker

    quiz_answers = [q["answer"] for q in quiz["questions"]]
    score = marker(answers, quiz_answers)

    # Update JSON
    add_scores(matric, sub, score)
