import keyboard
import os
import random
import time


def ask_username():
    while True:
        username = input("Enter Your Username: ")  # Asks for a Name from the user
        if username.isalnum():  # If username has only alphabets and numbers
            print()
            print(f"Welcome to Rock Paper Scissors, {username}")
            print()
            # program has now stored your username
            break
        elif username == "":  # If the username is blank, prompt to type it again
            print("Please enter a username")
            print()
        else:
            print("Please ensure your username only contains alphabets and numbers")
            print()
    # since this is a function, it needs to return the username variable
    # for other functions to use
    return username


def clear():
    # Clears the Console Output Screen completely
    os.system('cls')


def rules():  # Prints the rules to play the game
    print(("=" * 42))
    print("~ RULES ~".center(42))
    print("""Press the following keys to play the game:
         R      :  Rock
         P      :  Paper
         S      :  Scissors
     SPACE-BAR  :  New Game
        ESC     :  Quit Game""".center(42))
    print(("=" * 42))


def difficulty():  # function that will decide the difficulty
    game_difficulty = None  # Difficulty not chosen yet
    print("""Which Difficulty would you like to play on? (Press the keys B, N, I or ESC)
    B   - Baby
    N   - Normal
    I   - Impossible
    
    ESC - Quit Game
    """)
    # While loop to check for the input of the particular keyboard keys
    while True:
        # Different keys will set the difficulty for the game, defined by a string (e.g. "easy")
        if keyboard.is_pressed('n'):
            game_difficulty = "normal"
            # Computer will make a random choice thus giving 3 possibilities
            # Either a draw, win or loss
            break
        elif keyboard.is_pressed('b'):
            game_difficulty = 'baby'
            # Computer will lose everytime
            break
        elif keyboard.is_pressed('i'):
            game_difficulty = "impossible"
            # Computer will win everytime
            break
        elif keyboard.is_pressed('esc'):  # ESC key ends the program immediately
            quit()
    # returns the difficulty string for other functions to use
    return game_difficulty


def game():  # Starts a new game
    # New Game is basically a new series of matches
    print(game_difficulty.upper().center(33, "-"))
    match_count = 0  # represents the number of matches that have been played
    computer_wins = 0  # number of wins of the computer
    player_wins = 0  # number of wins of the user
    while True:
        print()
        print(f"Match - {match_count + 1}".center(33))  # Prints the current match number being played
        print()
        print(f"{username} : ", end='', flush=True)  # Shows the user what they've chosen (e.g. User : Rock)
        player_choice = None  # Player yet to make a choice
        computer_choice = None  # Computer yet to make a choice
        game_restarted = False  # New game is not to be started by default (while loop will run repeatedly by default)
        while True:
            if keyboard.is_pressed('r'):  # To choose a rock press R, similarly for paper and scissor
                time.sleep(0.05)
                print("Rock")
                player_choice = 'Rock'  # Player choice is updated to string "Rock", similarly for the others
                break
            elif keyboard.is_pressed('p'):
                time.sleep(0.05)
                print("Paper")
                player_choice = 'Paper'
                break
            elif keyboard.is_pressed('s'):
                time.sleep(0.05)
                print("Scissors")
                player_choice = 'Scissors'
                break
            elif keyboard.is_pressed('space'):  # To start a new game, press space-bar
                print('\r', end='')  # Overwrites the "User : " printed on the console
                game_restarted = True  # The player has chosen to start a new game by pressing space-bar
                break
            elif keyboard.is_pressed('esc'):  # Program ends after 0.5 seconds when ESC pressed
                time.sleep(0.5)
                exit()
        if not game_restarted:  # If the space-bar hasn't been pressed, by default game_restarted is False
            match_count += 1
            # player made a choice and the computer will do so too
            # Hence the first match will be completed soon. Program updates match_count already

            items = ['Rock', 'Paper', 'Scissors']
            # List from which computer will choose an item

            winner_criteria = {'Rock': 'Scissors', 'Scissors': 'Paper', 'Paper': 'Rock'}
            # Stores the information about which item beats which item

            if game_difficulty == 'normal':  # Random Choice, 3 Equally likely Possibilities
                computer_choice = random.choice(items)
                # Computer makes a random choice from the Items list

            elif game_difficulty == 'baby':  # Computer loses everytime
                computer_choice = winner_criteria[player_choice]
                # The computer simply chooses an item that will make the user win
                # The user has already made a choice so the computer knows how to lose

            elif game_difficulty == 'impossible':  # Computer wins everytime
                for winning_item, losing_item in winner_criteria.items():
                    # Checks the criteria (dictionary) to select the item that will beat the user
                    if losing_item == player_choice:
                        computer_choice = winning_item  # Chooses the item that beats the user
            print(f"Computer : {computer_choice}")  # Prints computer's choice
            print()

            winner_output = None
            # No one has won yet, the program has to yet calculate that

            # This part of code decides the winner
            if player_choice == computer_choice:  # If the items chosen by both are same
                # Only for Normal Possibilities

                winner_output = "~ MATCH TIED ~"  # Sets the result for the current match

            elif winner_criteria[player_choice] == computer_choice:  # If user's item beats computer's item
                # Only for Normal and Baby Difficulties

                winner_output = f"~ {username.upper()} WINS ~"  # Sets user as the winner for current match
                player_wins += 1  # User's wins are updated since user won

            else:  # Computer's item beats User's item
                # Only for Normal and Impossible Difficulties

                winner_output = "~ COMPUTER WINS ~"  # Sets Computer as the winner for current match
                computer_wins += 1  # Computer's wins are updated since it won

            print(winner_output.center(33))  # Prints the winner of current match

            # This prints the current score of the series
            print(f"{username}'s Wins: {str(player_wins)}".ljust(16) + f"Computer's Wins: {str(computer_wins)}".rjust(20))

            print()
            print(" =" * 16)  # Separates every match output to avoid confusion
            print()
            time.sleep(0.5)
        else:  # If the player chose to restart the game (basically reset the difficulty)
            break  # Simply breaks out of the loop which asks for User's input

    # At some point, the user has to start a new game, therefore when the user does so
    # the Function returns the number of wins of both sides as well as the number of matches played
    # for other functions to use
    return player_wins, computer_wins, match_count


def series_winner():  # This Function prints the summary of the current series before restarting the game
    # It uses the values returned by the previous function i.e. game()

    print("*CANCELLED*".center(33))
    # Since the match number is still displayed on the console
    # and the player chose to stop the game during that match, this prints CANCELLED below it
    # this clarifies (only for the user) the current match isn't to be counted as "played"

    print()
    time.sleep(0.8)
    diff_output = f"Difficulty: {game_difficulty.title()}"  # output that showing the difficulty of the current series
    time.sleep(0.8)
    winner = None  # Computer has to yet calculate the Winner of the SERIES (Not that match)
    score = str(player_wins) + "-" + str(computer_wins)  # defines the default total score output (Player - Computer)
    if player_wins > computer_wins:  # If user has more wins than computer
        winner = f"{username}"  # winner is updated to user
    elif player_wins < computer_wins:  # If computer has more wins than user
        winner = "Computer"  # Winner updated to computer
        score = str(computer_wins) + "-" + str(player_wins)  # score output redefined to (Computer - Player)
    else:
        winner = "DRAW"  # Winner is updated to "DRAW"

    series_details_output = f"Series {series_count} // Total Matches: {match_count}"
    # Details about the number of current series and total matches played in that particular series

    series_winner_output = f"Winner: {winner} [{score}]"
    # the winner and the score that is to be printed

    print("=" * len(series_details_output))  # Final Summary of Series Separator
    print(diff_output.center(len(series_details_output)))  # Prints the difficulty of the series
    print(series_details_output)  # Prints the details about the series
    print(series_winner_output.center(len(series_details_output)))  # Prints the winner and score variable
    print("=" * len(series_details_output))  # Final Summary of Series Separator
    print()
    print("Please Start a New Game by Pressing SPACE BAR")
    print("Press ESCAPE key to quit game")


def next_game_trigger():  # To start a new game
    while True:  # While loop checks for input whether
        if keyboard.is_pressed('space'):
            # Breaks this loop when space is pressed to restart the main loop (at the end)
            break
        elif keyboard.is_pressed('esc'):  # Quits game after 2 seconds if ESC pressed
            print()
            print("Quitting Game....")
            time.sleep(2)
            quit()


# MAIN PART OF THE CODE
# Uses all the functions together to complete and run the game

# Function asks for the user's name and then stores it in "username" variable used throughout the program
username = ask_username()

# Number of Series that have been started
series_count = 0

while True:  # Main Loop
    # The current number of series is updated everytime the loop starts
    series_count += 1

    # Prints the rules on the screen
    rules()

    # Stores the difficulty chosen by user in the "game_difficulty" variable
    game_difficulty = difficulty()

    # Clears the console output once difficulty chosen
    clear()

    # Prints the rules again on the top since all the output was cleared
    rules()

    print()
    print(f"SERIES - {series_count}".center(33))
    # Prints the Current Series Number on Screen before running game() function
    print()

    
    # The game() function is a while loop, so it will keep running unless SPACE-BAR is pressed
    # It keeps printing the match details (points and winner of every match)
    # When user presses SPACE-BAR, while loop inside the function breaks (The Current Series ends)
    # Now the game() function will give three values
    player_wins, computer_wins, match_count = game()
    # It Stores the three values from the game() function as seen above

    # This function prints the Series Summary and also decides the winner of the particular series
    series_winner()
    # The player can view the summary and see the stats of the series... the program will not move further

    # it waits for the user
    # to either exit the game or restart the game
    # restarting the game basically means resetting difficulty and start a new series
    # if the previous series was (Series x) then the new series will be (Series x + 1)
    next_game_trigger()

    # If the user chooses to restart, the output screen will be cleared
    # this makes space for the next series
    clear()
