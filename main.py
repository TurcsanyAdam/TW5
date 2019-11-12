import ui
import data_manager
import student
import company
import position
import application
import os


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    main_menu()
    x = int(ui.get_input("Enter a number: "))
    if x == 1:
        student.start_module()
    if x == 2:
        company.start_module()
    if x == 3:
        position.start_module()
    if x == 4:
        application.start_module()
    else:
        os.sys.exit()


def main_menu():
    menu = ["Student", "Company", "Position", "Application", "Exit programme"]
    ui.print_menu(menu)

if __name__ == "__main__":
    main()
