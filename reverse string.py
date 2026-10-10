class ReverseString:
    def reverse(self):
        user_input = input("Enter a string to reverse: ")
        return self.__reverse(user_input)
    def __reverse(self, s):
        return s[::-1]
__name__ == "__main__"
string = ReverseString()
print(string.reverse())