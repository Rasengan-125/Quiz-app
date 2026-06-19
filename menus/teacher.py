from services.quiz_service import add_quiz
from services.student_service import show_students, find_student
from services.teacher_service import teacher_auth, view_quizzes, delete_quiz


def teacher_menu():
    for attempt in range(3):
        result, email = teacher_auth()
        if result:
            break
        print(f"{2 - attempt} attempts remaining")
    else:
        print("Access denied")
        return
    while True:
        options = {
            "1": add_quiz,
            "2": show_students,
            "3": find_student,
            "4": lambda: view_quizzes(email),
            "5": lambda: delete_quiz(email),
        }
        print("")
        print("========================")

        for n, option in enumerate(
            [
                "Create Quiz",
                "Show Students",
                "Find Student",
                "View Quizzes",
                "Delete Quiz",
            ],
            start=1,
        ):
            print(f"{n}. {option}")
        choice = input("\nSelect an option (Q to quit): ").strip().upper()
        print("")
        if choice == "Q":
            break
        action = options.get(choice)

        if action:
            action()
        else:
            print("Invalid option")
