from services.quiz_service import add_quiz
from services.student_service import (
    add_student,
    show_students,
    find_student,
    delete_student,
)
from services.teacher_service import (
    add_teacher,
    show_teachers,
    find_teacher,
    delete_teacher,
)


def admin_menu():

    print("Welcome ADMIN")
    options = [
        "Add Student",
        "Add Teacher",
        "View Teachers",
        "View Students",
        "Find Teacher",
        "Find Student",
        "Delete Teacher",
        "Delete Student",
    ]

    for n, option in enumerate(options, start=1):
        print(f"{n}. {option}")

    options = {
        "1": add_student,
        "2": add_teacher,
        "3": show_teachers,
        "4": show_students,
        "5": find_teacher,
        "6": find_student,
        "7": delete_teacher,
        "8": delete_student,
    }

    choice = input("Select: ").strip()
    action = options.get(choice)

    if action:
        action()
    else:
        print("Invalid option")
