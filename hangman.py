import random


def main():
    names = ['dog', 'pig', 'elephant', 'police',
             'station', 'computer', 'apple',
             'train', 'python', 'carpet', 'ceiling',
             'bird', 'cow', 'boy', 'girl']

    your_word = list(random.choice(names))
    max_guesses = 6
    letter_number = 0
    correct_guesses = 0
    print(' '.join(your_word))
    hide_text = len(your_word) * ['_']

    while max_guesses != 0:
        print ('You have ' + str(hide_text))
        print('You have: ' + str(max_guesses) + ' to left')
        your_guess = str(input('your letter: '))

        if len(your_guess) != 1 or not your_guess.isalpha():
            print("\nYou can input only single letter and you can't use numbers. Try again! \n")
            max_guesses += 1

        while letter_number < len(your_word):
            if your_word[letter_number] == your_guess:
                hide_text[letter_number] = your_guess
                correct_guesses += 1
                max_guesses += 1
            letter_number += 1

        max_guesses -= 1
        letter_number = 0

        if correct_guesses == len(your_word):
            print('You have ' + str(hide_text))
            print('You won! The secret word: ' + str(''.join(your_word)).upper())
            break

        if max_guesses == 0:
            print('GAME OVER')

if __name__ == '__main__':
    main()




