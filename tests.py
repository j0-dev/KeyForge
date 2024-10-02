import random
import string


# Generate random number 1-4 (in accordance with list number)

def password():

    lowercase_1 = list(string.ascii_lowercase)
    uppercase_2 = list(string.ascii_uppercase)
    digits_3 = list(string.digits)
    symbols_4 = list(string.punctuation)

    password = ""

    while len(password) < 18:
        list_pick = random.randint(1, 4)

        if list_pick == 1:
            char = random.choice(lowercase_1)
            lowercase_1.remove(char)
            password += char

        elif list_pick == 2:
            char = random.choice(uppercase_2)
            uppercase_2.remove(char)
            password += char

        elif list_pick == 3:
            char = random.choice(digits_3)
            password += char

        else:
            char = random.choice(symbols_4)
            symbols_4.remove(char)
            password += char

    lowercase_1 = list(string.ascii_lowercase)
    uppercase_2 = list(string.ascii_uppercase)
    digits_3 = list(string.digits)
    symbols_4 = list(string.punctuation)

    return password

gen = (password() * 10)
print(gen)




