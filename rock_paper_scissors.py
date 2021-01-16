import time
import keyboard
import pyautogui
import random
winner_criteria = {'Rock': 'Scissors', 'Scissors': 'Paper', 'Paper': 'Rock'}


def winner(): # Decides the Winner
    print()
    if player_choice == computer_choice: # If both are same
        print("MATCH TIED")
    elif winner_criteria[player_choice] == computer_choice: #if computer choice is the assigned value you win
        print("YOU WIN")
    else:
        print("COMPUTER WINS") # Rest of the cases will have the computer as the winner
    print("----------")
    print()
    time.sleep(1)


print("RULES-")             # Prints the rules in the beginning
print("""
Press the following keys to play
R - Rock
P - Paper
S - Scissors

Press ESC key to exit program

""")
while True:
    player_choice = None # Currently the user hasn't made a choice
    response = "You : "                 # So that the choice is not printed in the next line
    print(response, end='', flush=True) # Instead prints in the same line after "You : "
    while True:                         
        if keyboard.is_pressed('r'): # Program won't respond unless you press 'r', 'p' or 's' keys
            time.sleep(0.05)         # While loop so that it keeps checking unless correct keys are pressed
            print("Rock") # Prints "Rock" next to "You : "
            player_choice = 'Rock'   # The player_choice variable now stores the item you chose
            break                    # Breaks the loop after the player_choice has been made
        elif keyboard.is_pressed('p'):
            time.sleep(0.05)
            print("Paper")              # Similarly for Paper and Scissors
            player_choice = 'Paper'
            break
        elif keyboard.is_pressed('s'):
            time.sleep(0.05)
            print("Scissors")
            player_choice = 'Scissors'
            break
        elif keyboard.is_pressed('esc'): # Exits the Program if Escape key is pressed
            time.sleep(0.5)
            exit()
    items = ['Rock', 'Paper', 'Scissors'] # List from which the computer will choose an item from
    computer_choice = random.choice(items) # Computer selects a random item from the list above
    # computer_choice variable will be updated to the item it chose
    print(f"Computer : {computer_choice}") # prints the computer's choice
    winner() # Runs the function that will decide the winner and then print the WINNER of the Game
    
