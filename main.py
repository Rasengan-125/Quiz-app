from menus.admin import admin_menu
from menus.student import student_menu
from menus.teacher import teacher_menu


def start():
    q1 = input("Are you a (T)eacher or (S)tudent? ").strip().upper()
    if q1 == "T":
        teacher_menu()
    elif q1 == "S":
        student_menu()
    elif q1 == "ADMIN":
        admin_menu()
    else:
        print("Invalid input")
        return


start()
