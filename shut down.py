def shutting_down():
    answer = input("do you want to shutdown device:")
    if answer.lower() == "yes":
        print("shutting down")
    else:
        print("sorry")
shutting_down()