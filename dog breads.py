class dog:
    species = "dogs"

    def __init__(self, name, age):
        self.name = name
        self.age = age

William = dog("William", 15)
Max = dog("Max", 17)

print(f"William is {William.age} years old.")
print(f"Max is {Max.age} years old.")