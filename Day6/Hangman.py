def input_letter():
    letter = input("Enter Letter: ")
    if len(letter) != 1:
        print("guess just one letter")
        return input_letter()
    return letter


if __name__ == "__main__":
    word = "peer"
    guessed_word = "_"*len(word)
    hangman_count = 0

    while True:
        letter = input_letter()
        if letter in word:
            pos = word.find(letter)
            while pos >= 0:
                guessed_word = guessed_word[:pos] + letter + guessed_word[pos +1:]
                pos = word.find(letter, pos+1)
            print(guessed_word)
            if guessed_word == word:
                print("won")
                break
        else:
            hangman_count += 1
            print(hangman_count)
            if hangman_count >= 10:
                print("Game Over")
                break

