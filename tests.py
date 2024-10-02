import secrets
import string

def password():

    lowercase_1 = list(string.ascii_lowercase)
    uppercase_2 = list(string.ascii_uppercase)
    digits_3 = list(string.digits)
    symbols_4 = list(string.punctuation)

    password = ""

    while len(password) < 18:
        list_nums = [1, 2, 3, 4]
        list_pick = secrets.choice(list_nums)

        if list_pick == 1:
            char = secrets.choice(lowercase_1)
            lowercase_1.remove(char)
            password += char

        elif list_pick == 2:
            char = secrets.choice(uppercase_2)
            uppercase_2.remove(char)
            password += char

        elif list_pick == 3:
            char = secrets.choice(digits_3)
            password += char

        else:
            char = secrets.choice(symbols_4)
            symbols_4.remove(char)
            password += char

    lowercase_1 = list(string.ascii_lowercase)
    uppercase_2 = list(string.ascii_uppercase)
    digits_3 = list(string.digits)
    symbols_4 = list(string.punctuation)

    return password

for i in range(1, 10):
    gen = password()
    print(gen)




