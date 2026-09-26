import random
import string


def getrandompassword(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    print("printing random password")
    print(password)
    return password


getrandompassword()