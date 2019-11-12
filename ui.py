import random

def print_menu(menu):
    i = 1
    for line in menu:
        print("(" + str(i) + ") " + line)
        i += 1


def get_input(user_input):
    x = input(user_input)
    return x

def print_table(table, title_list):
    longest_word = 0
    for i in table:
        for word_len in i:
            if longest_word < len(word_len):
                longest_word = len(word_len)



    print("/","-"*(len(title_list*(longest_word+2))), "\\")
    for titles in title_list:

        print("| {1:^{0}}".format(longest_word, titles),end="")
    print("|")
    for elements in table:
        for minus in elements:
            print("| {1:-^{0}}".format(longest_word,""),end=" ")
        print("|")
        for element in elements:
            print("| {1:^{0}}".format(longest_word, element),end=" ")
        print("|")

def generate_random():
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = lowercase.upper()
    symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', '<', '=', '>', '?',
               '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    passw = ""
    while len(passw) != 8:
        passw += (random.choice(uppercase))
        passw += (random.choice(uppercase))
        passw += (random.choice(lowercase))
        passw += (random.choice(lowercase))
        passw += (random.choice(symbols))
        passw += (random.choice(symbols))
        passw += (str(random.choice(numbers)))
        passw += (str(random.choice(numbers)))
    random_id = list(passw)
    random.shuffle(random_id)
    generated = "".join(random_id)
    # your code

    return generated
