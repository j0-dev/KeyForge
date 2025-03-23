import secrets
import string

# Password generator function
def password_generator(length):

    if length < 8:
        raise ValueError("Password must be at least 8 characters.")
    elif length > 64:
        raise ValueError("Maximum password length is 64 characters.")

    lowercase_1 = list(string.ascii_lowercase)
    uppercase_2 = list(string.ascii_uppercase)
    digits_3 = list(string.digits)
    symbols_4 = list(string.punctuation)

    password = ""

    while len(password) < length:
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

    return password






    