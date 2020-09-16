"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking:
 File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random
import pickle


def start_game():
    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.

    random_number = random.randint(1, 15)
    count = 1

    name = input("What is your first name.  ")
    # try to open file. If file exists, use it as variable. If exception, create it.
    # How to: Check if file exist https://linuxize.com/post/python-check-if-file-exists/
    try:
        file = open("scoreFile.txt", "rb")
        # How to use Pickle to store variables reading sources:
        # https://www.knowledgehut.com/tutorials/python-tutorial/python-object-serialization
        # https://www.tutorialspoint.com/object_oriented_python/object_oriented_python_serialization.htm#
        # https://docs.python.org/3/library/pickle.html
        # https://wiki.python.org/moin/UsingPickle
        # https://www.datacamp.com/community/tutorials/pickle-python-tutorial
        # https://realpython.com/python-pickle-module/
        # https://www.geeksforgeeks.org/understanding-python-pickling-example/
        # https://www.journaldev.com/15638/python-pickle-example
        score = pickle.load(file)
    except FileNotFoundError:
        file = open("scoreFile.txt", "wb")
        score = 0
        pickle.dump(score, file)
        file.close()
    print("Greetings {}, and welcome to the Guessing Game!\nHigh score to beat: {}".format(name, score))
    while True:
        try:
            guess = int(input('Pick a number from 1 - 15.  '))
            if guess not in range(1, 16, 1):
                print('Number must be within the range of 1 to 15')
                count += 1
                score -= 10
                continue
            elif guess == random_number:
                print('You ARE CORRECT!!!')
                score += 1000
                break
            elif guess < random_number:
                print('Try a higher number...  ')
                count += 1
                score -= 10
            elif guess > random_number:
                print('Try a lower number...  ')
                count += 1
                score -= 10
        except ValueError:
            print('Must enter numeric values.')
            count += 1
            score -= 10
    # Open file to dump new score into.
    file = open("scoreFile.txt", "wb")
    new_score = score
    pickle.dump(new_score, file)
    file.close()
    # Open file to load updated score. Probably can use a better method. Seems a little "DRY"-ish
    file = open("scoreFile.txt", "rb")
    final_score = pickle.load(file)
    file.close()
    replay = input('''
        It took {} attempt(s) to guess the correct number.
        Your total score is: {}
        Would you like to play again? Y/N  '''.format(count, final_score))
    replay = replay.upper()
    if replay == 'Y':

        start_game()
    else:
        print('Thank you for playing The Guessing Game, {}.\n\nEnd of Game.'.format(name))

# Kick off the program by calling the start_game function.
# With Pickle method I used, score will continue to climb until game is ended.
# At start of game, high score is last score on previous game.


start_game()
