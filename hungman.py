import random
import string
import sys


def hangman():
    secret_words = ('python', 'java', 'window', 'sofa', 'chair', 'table', 'pillow', 'bathroom', 'garage', 'corona')
    secret_word = random.choice(secret_words)
    guessed_letters = []
    word = ['-' for _ in secret_word]
    print("".join(word))
    attempts = 8
    while attempts > 0:
        char = input("Input a letter: ")
        if not (len(char) == 1 and char in string.ascii_lowercase):
            print("Please, enter one letter in lowercase")
        else:
            if char in guessed_letters:
                print("You already has this letter")
                continue
            guessed_letters.append(char)
            if char not in secret_word:
                attempts -= 1
                print(f"No such letters in the word, you have {attempts} attempts")
                continue
            for i in range(len(word)):
                if secret_word[i] == char:
                    word[i] = char
            if secret_word == "".join(word):
                print("You win!")
                break
        print("".join(word))
    else:
        print("You are hanged")


if __name__ == '__main__':
    while True:
        choice = input("Type 'play' to play the game, 'exit' to quit: ")
        if choice == 'play':
            hangman()
        elif choice == 'exit':
            sys.exit()
        else:
            print("Incorrect choice, please, try again!")
