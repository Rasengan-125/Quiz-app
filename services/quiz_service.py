import os
import json
import time
from models import Quiz
from services.helpers import (
    time_formatter,
    marker,
    add_scores,
    check_students,
    update_score,
    taken,
)


def load_quizzes():
    if os.path.exists("data/quizzes.json"):
        with open("data/quizzes.json", "r") as f:
            content = f.read()
            return json.loads(content) if content else []
    else:
        return []


def save_quizzes(quizzes):
    with open("data/quizzes.json", "w") as f:
        json.dump(quizzes, f, indent=4)


# -----------------------ADD QUIZ---------------------------
def add_quiz():
    data = load_quizzes()
    letters = ["A", "B", "C", "D"]

    subject = input("Subject: ").strip().upper()
    subs = [quiz["subject"] for quiz in data]

    # ----------------IF BLOCK----------------
    if subject in subs:
        q1 = input("Subject exists.\n R = Replace | Q = Quit\n... ").strip().lower()
        if q1 == "q":
            return
        elif q1 != "r":
            print(f"{q1} is not a valid option")
            return
        index = subs.index(subject)
    #  ---------------------------------INPUTS--------------------------------------
    teacher = input("Teacher: ").strip().capitalize()
    while True:
        try:
            quiz_time = int(input("Time in seconds: "))
            break
        except ValueError:
            print("Please enter a valid number")

    while True:
        try:
            num = int(input("Number of questions: "))
            break
        except ValueError:
            print("Please enter a valid number")

    questions = []
    for i in range(1, num + 1):
        print("_______________________________________")
        question = input(f"Question {i}\n")
        options = []
        for j in range(4):
            option = input(f"Option {letters[j]}: ").strip().capitalize()
            options.append(f"{letters[j]}. {option}")
        answer = input("Answer: ").strip().upper()
        questions.append({"question": question, "options": options, "answer": answer})

    quiz = Quiz(subject, teacher, quiz_time, questions).__dict__

    if subject in subs:
        data[index] = quiz
    else:
        data.append(quiz)

    save_quizzes(data)
    print("\nQUIZ CREATED")


# ------------------- TAKE QUIZZ------------------------------------
def take_quiz():
    data = load_quizzes()
    matric = input("Enter matric number: ").strip()

    student = check_students(matric)
    if student == False:
        print("Matric number not found. You are not a registered student")
        return

    for n, item in enumerate(data, start=1):
        subject = item["subject"]
        print(f"{n}. {subject}")  # Quiz list

    while True:
        try:
            course = int(input("Select the course you want to take by number: "))
            if course < 1 or course > len(data):
                print("Invalid quiz number")
                continue
            break
        except ValueError:
            print("Please enter a valid number")

    quiz = data[course - 1]
    sub = quiz["subject"]

    if taken(sub, matric):
        return  # ----------------------Taken or Not

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

    # Update grades.JSON
    add_scores(matric, sub, score)

    # Update student.json
    update_score(matric, sub, score)

    print("\nQuiz Finished")
    print(f"SCORE: {score}")
