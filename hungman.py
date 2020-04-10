import random


def hangman():
    with open('words.txt', 'r') as f:
        secret_words = f.read().splitlines()

    secret_word = random.choice(secret_words)
    guessed_letters = []
    word = ['-' for _ in secret_word]
    attempts = 8

    while attempts > 0:
        print("".join(word))
        char = input('Input a letter: ').casefold()

        if len(char) != 1:
            print('Please, enter one letter')

        else:
            if char in guessed_letters:
                print('You already has this letter')
                continue

            guessed_letters.append(char)

            if char not in secret_word:
                attempts -= 1
                print(f'No such letters in the word, you have {attempts} attempts')
                continue

            for i in range(len(word)):
                if secret_word[i] == char:
                    word[i] = char

            if secret_word == ''.join(word):
                print(f'You win!')
                break
    else:
        print('You are hanged')
    print(f'The word is "{secret_word}"')


if __name__ == '__main__':
    while True:
        choice = input('Type "play" to play the game, "exit" to quit: ').casefold()
        if choice == 'play':
            hangman()
        elif choice == 'exit':
            exit()
        else:
            print('Incorrect choice, please, try again!')
