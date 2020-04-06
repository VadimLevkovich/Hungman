import random
import string
import sys
from msvcrt import getch


def hangman():
    secret_words = ('python', 'java', 'window', 'sofa', 'chair', 'table', 'pillow', 'bathroom', 'garage', 'corona')
    secret_word = random.choice(secret_words)
    guessed_letters = []
    word = ['-' for _ in secret_word]
    print("".join(word))
    attempts = 8
    while attempts > 0:
        char = input(getch().decode('utf-8'))
        if len(char) == 1 and char in string.ascii_lowercase:
            if char in guessed_letters:
                print(f"You already has this letter")
            else:
                if char in secret_word:
                    for i in range(len(word)):
                        if secret_word[i] == char:
                            word[i] = char
                            if secret_word == "".join(word):
                                print("You win!")
                                menu()
                else:
                    attempts -= 1
                    print(f"No such letters in the word, you have {attempts} attempts")
                guessed_letters.append(char)
        else:
            print("Please, enter one letter in lowercase")
        print("".join(word))
    else:
        print("You are hanged")
        menu()


def menu():
    choice = input("Type 'play' to play the game, 'exit' to quit: ")
    if choice == 'play':
        hangman()
    elif choice == 'exit':
        sys.exit()
    else:
        print("Incorrect choice, please, try again!")
        menu()


if __name__ == '__main__':
    menu()
