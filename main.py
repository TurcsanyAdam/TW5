import ui
import data_manager
import student
import company
import position
import application
import os


def main():
    main_menu()
    x = int(data_manager.get_input())
    if x == 1:
        student.main()
    if x == 2:
        student.main()
    if x == 3:
        student.main()
    if x == 4:
        student.main()
    else:
        os.sys.exit()


def main_menu():
    menu = ["Student", "Company", "Position", "Application", "Exit programme"]
    ui.print_menu(menu)

if __name__ == "__main__":
    main()