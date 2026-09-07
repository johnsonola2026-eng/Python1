def circumfrence():
        import turtle
        turtle.Screen().bgcolor("black")
        turtle.color("white")
        turtle.speed(10)
        turtle.circle(100)
        turtle.done()
        if input ("do you understand the circumfrence of a circle:") == "yes":
            print("good")
        else:
            print("try again")
circumfrence()