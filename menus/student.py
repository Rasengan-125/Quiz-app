from services.quiz_service import take_quiz
from services.student_service import view_my_grades


def student_menu():
    options = ["Take Quiz", "View My Grades"]
    for n, option in enumerate(options, start=1):
        print(f"{n}. {option}")

    actions = {
        "1": take_quiz,
        "2": view_my_grades,
    }

    while True:
        choice = input("\nSelect an option (Q to quit): ").strip().upper()
        if choice == "Q":
            return
        action = actions.get(choice)
        if action:
            action()
            break
        print("Invalid option")
