class BMW:
    def fuel_type(self):
        return "Petrol"
    def max_speed(self):
        return 25
class Ferrari:
    def fuel_type(self):
        return "Petrol"
    def max_speed(self):
        return 30
car1=BMW()
car2=Ferrari()
for car in (car1,car2):
    print(car.fuel_type())
    print(car.max_speed())