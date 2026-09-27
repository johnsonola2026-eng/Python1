class parrot:
    species="bird"
    def __init__(self, name, age):
         self.name=name
         self.age=age
Blu=parrot("Blu",10)
Woo=parrot("Woo",15)
print("blu is a {}".format(Blu.species))
print("Woo is also a {}".format(Woo.species))