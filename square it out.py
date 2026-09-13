def print_square_values(beginning, end):
	"""Print the square values in the inclusive range, grouped by parity."""
list1=[]
list2=[]

for number in range('beginning','end'+ 1):
		square = number ** 2
		if square % 2 == 0:
			list1.append(square)
else:
			list2.append(square)
print("Even squares:", list1)
print("Odd squares:", list2)