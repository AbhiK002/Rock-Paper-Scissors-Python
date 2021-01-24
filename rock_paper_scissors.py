import keyboard
import os
import random
import time


def ask_username():
    # Asks and Stores your username
    # it should contain only alphabets and numbers
    while True:
        username = input("Enter Your Username: ")
        if username.isalnum():
            print('\n' + f"Welcome to Rock Paper Scissors, {username}" + '\n')
            break
        elif username == "":  
            print("Please enter a username" + '\n')
        else:
            print("Please ensure your username only contains alphabets and numbers" + '\n')
    # Returns the username for future use
    return username


def clear():
    # Clears the Output Screen in Console to make the game output neat
    # Separates Series of Matches to avoid confusion
    os.system('cls')


def rules():
    # Prints all the rules of the game
    print(("=" * 42))
    print("~ RULES ~".center(42))
    print("""Press the following keys to play the game:
         R      :  Rock
         P      :  Paper
         S      :  Scissors
     SPACE-BAR  :  New Game
        ESC     :  Quit Game""".center(42))
    print(("=" * 42))


def difficulty():
    game_difficulty = "normal"  # Difficulty by default is random (normal)
    print("""Which Difficulty would you like to play on? (Press the keys B, N, I or ESC)
    B   - Baby
    N   - Normal
    I   - Impossible
    
    ESC - Quit Game
    """)
    while True:
        # Keeps checking for key presses until valid keys pressed
        if keyboard.is_pressed('n'):
            # by default difficulty is always normal
            # normal difficulty has equally likely win, loss or draw for the user
            break
        elif keyboard.is_pressed('b'):
            game_difficulty = 'baby'
            # player always wins in this difficulty
            break
        elif keyboard.is_pressed('i'):
            game_difficulty = "impossible"
            # player always loses in this difficulty
            break
        elif keyboard.is_pressed('esc'):
            # program quits instantly if esc pressed
            quit()
    # returns difficulty for future use
    return game_difficulty


def game():
    # function which contains the main game
    # including series, difficulty and matches details
    print(game_difficulty.upper().center(33, "-"))
    # this parts marks the beginning of a new series
    # number of wins and matches played are set to zero
    match_count = 0  
    computer_wins = 0  
    player_wins = 0 
    while True:
        # this loop marks every match in a series
        print('\n' + f"Match - {match_count + 1}".center(33) + '\n')
        print(f"{username} : ", end='', flush=True)
        player_choice = None  
        computer_choice = None 
        game_restarted = False  # by default series is supposed to continue
        while True:
            # Loop to check for user input to select item
            if keyboard.is_pressed('r'):  
                time.sleep(0.05)
                print("Rock")
                player_choice = 'Rock' 
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
            elif keyboard.is_pressed('space'):
                # To end the current series and start a new one with a new difficulty
                print('\r', end='')  
                game_restarted = True 
                break
            elif keyboard.is_pressed('esc'): 
                time.sleep(0.5)
                exit()
        if not game_restarted:  # if the user doesn't press space bar, series will continue
            match_count += 1
            items = ['Rock', 'Paper', 'Scissors']
            winner_criteria = {'Rock': 'Scissors', 'Scissors': 'Paper', 'Paper': 'Rock'}

            # This part decides the choice of computer depending upon difficulty
            if game_difficulty == 'normal': 
                computer_choice = random.choice(items)
            elif game_difficulty == 'baby': 
                computer_choice = winner_criteria[player_choice]
            elif game_difficulty == 'impossible':
                # Makes sure player always loses
                for winning_item, losing_item in winner_criteria.items():
                    if losing_item == player_choice:
                        computer_choice = winning_item  
            print(f"Computer : {computer_choice}" + '\n')

            # This part decides the winner/draw
            winner_output = None
            if player_choice == computer_choice: 
                winner_output = "~ MATCH TIED ~"  
            elif winner_criteria[player_choice] == computer_choice: 
                winner_output = f"~ {username.upper()} WINS ~"  
                player_wins += 1 
            else: 
                winner_output = "~ COMPUTER WINS ~"  
                computer_wins += 1 
            print(winner_output.center(33))
            # Prints the current score after every match
            print(f"{username}'s Wins: {str(player_wins)}".ljust(16) + f"Computer's Wins: {str(computer_wins)}".rjust(20))
            print('\n' + " =" * 16 + '\n')
            time.sleep(0.5)
        else:
            print("*CANCELLED*".center(33) + '\n')  # to avoid confusion
            time.sleep(0.8)
            # if the user ended the series by pressing space bar
            break
    # the three variables returned for future use if user decides to end series
    return player_wins, computer_wins, match_count


def series_winner():
    # Before starting next series, this function prints the winner and other details about the current series
    # Basically a summary (number of matches, overall winner, etc) of the current series are printed
    diff_output = f"Difficulty: {game_difficulty.title()}"  
    time.sleep(0.8)
    winner = None  # Overall Winner not decided yet
    score = str(player_wins) + "-" + str(computer_wins) 
    if player_wins > computer_wins: 
        winner = f"{username}"  
    elif player_wins < computer_wins:  
        winner = "Computer" 
        score = str(computer_wins) + "-" + str(player_wins)
    else:
        winner = "DRAW"

    # The Series Details are printed
    series_details_output = f"Series {series_count} // Total Matches: {match_count}"
    series_winner_output = f"Winner: {winner} [{score}]"
    print("=" * len(series_details_output))  
    print(diff_output.center(len(series_details_output)))  
    print(series_details_output) 
    print(series_winner_output.center(len(series_details_output)))
    print("=" * len(series_details_output) + '\n')
    print("Please Start a New Game by Pressing SPACE BAR")
    print("Press ESCAPE key to quit game")


def next_game_trigger():
    # Program won't abruptly start a new series after printing summary
    # instead this function will wait for the user (to press spacebar or esc)
    while True: 
        if keyboard.is_pressed('space'):
            break
        elif keyboard.is_pressed('esc'): 
            print('\n'+"Quitting Game...."+'\n')
            time.sleep(2)
            quit()


def main_loop():
    # Main loop that runs the whole game
    global username
    username = ask_username()
    global series_count
    series_count = 0
    while True:
        # Everytime this loop repeats (series ended)
        # Series number increases by 1
        series_count += 1
        rules()
        global game_difficulty
        game_difficulty = difficulty()
        clear()
        rules()
        print('\n' + f"SERIES - {series_count}".center(33) + '\n')
        global player_wins
        global computer_wins
        global match_count
        player_wins, computer_wins, match_count = game()
        series_winner()
        next_game_trigger()
        clear()


if __name__ == '__main__':
    main_loop()
