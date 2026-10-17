class roman:
    def __init__(self):
        self.roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    def translate(self,roman_string):
        total = 0
        prev_value = 0
        for char in reversed(roman_string):
            value = self.roman_numerals[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total
input_string = input("Enter a Roman numeral:")
translator = roman()
print(translator.translate(input_string))