import random


def guessing_number():
    num_rand = random.randint(0, 100)
    base = random.randint(2, 16)
    tries = 3

    while True:

        if tries == 0:
            print("You didn't guess in time.")
            break
        if tries == 1:
            print(f'You have {tries} chance')
        else:
            print(f'You have {tries} chances')
        
        try:
            guessing_user = int(input(f'Guess the number. Enter a number in base {base}:'), base)
            tries -= 1
        except ValueError:
            continue             

        if guessing_user == num_rand:
            print('Just right!')
            break
        if guessing_user < num_rand:
            print('Too low')
        else:
            print('Too high')

def guessing_word():
    words = ["ant", "apple", "bear", "cat", "dog", "mango", "zebra"]
    rand_word = random.choice(words)
    tries = 3

    while True:

        if tries == 0:
            print("You didn't guess in time.")
            break
        if tries == 1:
            print(f'You have {tries} chance')
        else:
            print(f'You have {tries} chances')
        
        guessing_user = input(f'Guess the word:')
        tries -= 1

        if guessing_user == rand_word:
            print('Just right!')
            break
        if guessing_user < rand_word:
            print('Try a later word.')
        else:
            print('Try an earlier word.')
    

def guessing_game():
    
    selected_game = input('Select a game "1" to guessing a number or "2" for guessing a word')

    match selected_game:
        case "1":
            guessing_number()
        case "2":
            guessing_word()
        case _:
            print('Invalid option')



if __name__ == "__main__":
    guessing_game()
