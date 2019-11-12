def print_menu(menu):
    i = 1
    for line in menu:
        print("(" + str(i) + ") " + line)
        i += 1


def get_input(user_input):
    x = input(user_input)
    return x

