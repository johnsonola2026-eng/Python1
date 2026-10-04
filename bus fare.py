class Vehicle:
	def __init__(self, seating_capacity):
		self.seating_capacity = seating_capacity
	def fare(self):
		self.seating_capacity * 100
class Bus(Vehicle):
    def __init__(self):
        super().__init__(50)
    def fare(self):
	    return 5500