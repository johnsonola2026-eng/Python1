from collections import Counter


def check_frequency(text):
    words = text.lower().split()
    return Counter(words)


def main():
    test_dictionary = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'coding': 1}
    print("Sample dictionary:", test_dictionary)

    choice = input("Do you want to check your frequency in the test dictionary? (y/n): ").strip().lower()
    if choice != 'y':
        print("No frequency check was performed.")
        return

    user_text = input("Enter a sentence to count word frequency: ")
    frequency = check_frequency(user_text)

    print("\nWord frequency:")
    for word, count in sorted(frequency.items()):
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
