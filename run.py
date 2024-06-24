import random
import curses
import _curses

#ASk the user for the user name

player_name = input ("What is your name? ")

#Have you played snake before?
while true:
    played_before = input ("Have you played this game before? (Yes/No)").lower()
    if played_before['y', 'N']:
        break
    else:
        print("Invalid input. Please enter 'Y' or 'N' ")

#If the player has played the game before skip instructions

if played_before == 'no':
    while true:
        controll_the_snake = input("Use the arrow keys to control the snake\
        You can hold down the arrows to make the snake go faster\
        Do not let the snake touch the sides of the game area or eat itself!\
        Press enter to continue. ")
    if controll_the_snake == '':
        break
    else:
        print("Invalid input. Press Enter to continue")

    #Initialize curses mode
    stdsr = curses.initscr()

    try:
        #trying to make the cursor invisible
        curses.curs.set(0)
    except _curses.error:
        #If the terminal dosnt support it, ignore the the error and start anyway
        pass