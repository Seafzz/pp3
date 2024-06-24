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
    #Get the height and width of the screen
    sh, sw = s.getmaxyx()
    # Create a window using the screen height and width given
    w = curses.newwin(sh, sw, 0, 0)
    # Accept keypad input 
    w.keypad(1)
    #Refresh the screen every 100 milliseconds / 1 second
    w.timeout(100)

    #Create the snake and the start cordinates for the snake
    snk_x = sw //4
    snk_y = sw //2
    snake = [
        [snk_y, snk_x],
        [snk_y, snk_x -1],
        [snk_y, snk_x -2]
    ]
#Create the food
food = sh[sh//2, sw//2]
w.addch(int(food[0])), int(food[1]), curses.ACS_PI)