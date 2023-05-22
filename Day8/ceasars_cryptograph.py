import string


def decoded_word(word, shift):
    new_word = ""
    for letter in word:
        pos = string.printable.find(letter)
        pos = pos-shift
        offset = pos // len(string.printable)
        pos -= offset * len(string.printable)
        #while pos >= len(string.printable):
        #    pos -= len(string.printable)
        new_letter = string.printable[pos]
        new_word += new_letter
    return new_word


def encoded_word(word, shift):
    return decoded_word(word, -shift)

