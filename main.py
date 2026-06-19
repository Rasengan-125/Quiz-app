from menus.admin import admin_menu
from menus.student import student_menu
from menus.teacher import teacher_menu


def start():
    while True:
        print("\n-----------------------------------------------")
        q1 = input("Are you a (T)eacaher or (S)tudent? (Q)uit ").strip().upper()
        if q1 == "T":
            teacher_menu()
        elif q1 == "S":
            student_menu()
        elif q1 == "ADMIN":
            admin_menu()
        elif q1 == "Q":
            break
        else:
            print("Invalid input")


start()
