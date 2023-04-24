import random
import string


def user_password_input():
    num_letters_str = input("Please select number of letters to use in your password: \n")
    num_letters = int(num_letters_str)
    num_symbols_str = input("Select number of symbols to use in your password: \n")
    num_symbols = int(num_symbols_str)
    num_numbers_str = input("Select number of numbers to use in your password: \n")
    num_numbers = int(num_numbers_str)
    return num_letters, num_symbols, num_numbers


def generate_user_password(num_letters, num_symbols, num_numbers):
    chars_in_password = []
    for _ in range(num_numbers):
        rand_number_id = random.randint(0, 9)
        rand_number = str(rand_number_id)
        chars_in_password.append(rand_number)
    for _ in range(num_symbols):
        rand_symbol_id = random.randrange(0, len(string.punctuation))
        rand_symbol = string.punctuation[rand_symbol_id]
        chars_in_password.append(rand_symbol)
    for _ in range(num_letters):
        rand_letter_id = random.randrange(0, len(string.ascii_letters))
        rand_letter = string.ascii_letters[rand_letter_id]
        chars_in_password.append(rand_letter)
    random.shuffle(chars_in_password)
    return "".join(chars_in_password)


if __name__ == "__main__":
    num_letters, num_symbols, num_numbers = user_password_input()
    password = generate_user_password(num_letters, num_symbols, num_numbers)
    print(f"Here is your password: {password}")
