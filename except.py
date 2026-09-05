try:
    number = int(input("Enter a number: "))
    print("the number you entered is:",number)
except ValueError as ex:
    print("exception:", ex)