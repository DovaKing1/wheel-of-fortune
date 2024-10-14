
################################################################################
#                                                                              #
#   Author: Dr. Scott Barlowe                                                  #
#   Authors: Prashreet Poudel and Elijah McCray                                #
#                                                                              #
#   Program that simulates the popular TV game show Wheel of Fortune           #
#                                                                              #
#   Date: March 03, 2023                                                       #
#                                                                              #
################################################################################

################################################################################
#                                                                              #
#   You MUST use the following variables. You may change the value             #
#   of PLAY_STRING for testing if you wish.                                    #
#                                                                              #
################################################################################

import random

PLAY_STRING = "go cats" # String storing the puzzle to be solved
VOWEL_COST = -250       # Amount to be added to the score when a vowel is
                        #   purchased

# Named constants for vowels
A = 'a'
E = 'e'
I = 'i'
O = 'o'
U = 'u'

puzzle_display   = []   # List storing the display version of the puzzle
previous_guesses = []   # List tracking what letters have been previously used
shuffled_wheel   = []   # Shuffled version of the dollar amounts

                        # List of dollar amounts to be placed on the wheel
dollar_amounts   = [-1, 200, 200, 250, 500, 500, 1000, 1500, 5000]

################################################################################
#                                                                              #
#     Place your functions below                                               #
#                                                                              #
################################################################################


def there_not_there(player_number, true_or_false):
    """This function checks if the user choose a vowl or a consonant. 

    Args: 
    player_number: Holds the player number.
    true_or_false: Holds if the users choose of a  vowl or a consonant

    Return: 
        Returns a number of charcters of the users guess is in the mystery word.
    
    """
    # Checks if the varable is a vowl or consonant.
    if true_or_false:
        data_type = "vowel"
    else:
        data_type = "consonants"

    # Gets the users guess.
    u_i = str.lower(input("\nPlayer " +str(player_number)+"-Enter a guess: "))
    
    # Checks if the users guess is a vowl or consonant.
    if u_i == A or u_i == E or u_i == I or u_i == O or u_i == U:
                                                                   
        guessed_data = "vowel"
    else:
        guessed_data = "consonants"

    # Setting varables to zero.
    cnt = 0
    loop_cnt = 0

    # Checks if the users guess and the user choice is the same.
    if guessed_data == data_type:

        # Call function to "choose_letter"
        letter = choose_letter(player_number, u_i )

        if letter == A or letter == E or letter == I or letter == O or \
              letter == U:
                                                                   
            letter_data = "vowel"
        else:
            letter_data = "consonants"

        if letter_data == guessed_data:




            # Loops though checking how many characters of the users guess is 
            # in the mystery word 
            while loop_cnt < len(PLAY_STRING):
                string_to_check = PLAY_STRING[loop_cnt]
                if letter == string_to_check:
                    cnt =+ 1
                loop_cnt += 1
            print("\nThere are "+ str(cnt)+ " " + letter +"'s")

            # Loops though the mystery word to see if any of it 
            # matchs the users guess.
            for i in range(len(PLAY_STRING)):
                if PLAY_STRING[i] == letter:
                    puzzle_display[i] = letter

        else: # prints if the letter chosen again by user is wrong type.
            print("\nGuess Type Mismatch!")
            previous_guesses.pop()

    else: # prints if the users guess does not match what the user is choosing.
        print("\nGuess Type Mismatch!")
        #print("There are "+ str(cnt)+ " " + u_i +"'s")

    # Returns the number of characters in the mystery word.
    return cnt


def build_wheel():
    """This function makes a copy of the list of values and makes a shuffled 
            wheel of values.

    Args:
        None

    Return: 
        None 
    
    """
    global dollar_amounts, shuffled_wheel

    import copy

    # Makes a copy of the list of values.
    copied_dollar_amount = copy.copy(dollar_amounts)
    
    # loop to make a chuffled wheel.
    while len(copied_dollar_amount)!= 0:
        index= get_next_amt(copied_dollar_amount)
        shuffled_wheel.append(copied_dollar_amount.pop(index))
    

def get_next_amt(copied_list):
    """This function selects a random number between two values.

    Args:
        copied_list: Holds the coppied list of values.

    Return: 
        Returns the number that was selected from the random number genorator.
    
    """
    # Gets a random number between two values.
    index= random.randint(0,len(copied_list)-1)

    # Returns the random number.
    return index



def choose_letter(player_num, guess):
    """This function checks if the users guess has been tried before or not. 
            If it has it will ask for the user to input another guess. If 
            the guess has not been used it gets added to the used list.

    Args: 
        player_num: hold the players number.
        guess: Holds the users guess.

    Return: 
        Returns the users guess.
    
    """
    cnt = 0
    while cnt < (len(previous_guesses)):
        # Checks if the users guess has been tryed before or not.
        if previous_guesses[cnt] == guess:
            print("Player " + str(player_num) + 
                  "-Guess Already Used, Try Another: " , end="")
            guess = input("enter a new guess: ").lower()
            cnt = 0
        else:
            cnt+=1

    # Adds the users guess to a list of previsously tryed guesses. 
    previous_guesses.append(guess)

    # Returns the users guess.
    return guess    


def spin_wheel():
    """This function shows that the wheel is spinning and gets a random number 
            between two values. Then returns the value returned from the 
            function call.

    Args: 
        None

    Return: 
        Returns the result of the function call from "shuffled_wheel".
    
    """
    # Prints to show the wheel is spining.
    print("\nspinning...", end="")

    # Gets a random number between two values.
    spin_wheel_index =  random.randint(0, len(shuffled_wheel)-1)

    # returns the result of the function call to "shuffled_wheel".
    return shuffled_wheel[spin_wheel_index]


def adjust_player_total(player_list, player_num, amount, bankrupt):
    """This function checks if the user has anymoney or not. If the user 
            does not it prints "BANKRUUUUUPPPTTT!". If the user does the 
            program correct it self.

    Args: 
        player_list: list of plays.
        player_num: play's number.
        amount: Amount of money the user has.
        bankrupt: Holds if the user is backrupt or not.

    Return: 
        Returns a varable holding the list of players.
    
    """
    # Checks if the users amount of money is zero
    if bankrupt:
        player_list[player_num] = amount
        print("BANKRUUUUUPPPTTT!")

    else:
        player_list[player_num] = player_list[player_num] + amount

    # Returns the amount of money.
    return player_list


def load_string():
    """This function builds a string holding under scores for unawnsered 
        characters if awnsered correctly awnered will show the replace 
        it with the character.

    Args: 
        None

    Return: 
        None 
    
    """
    # Builds a representation of the mystery word.
    for i in range(len(PLAY_STRING)):
        if PLAY_STRING[i] == " ":
            puzzle_display.append(" ")
        else:
            puzzle_display.append("_") 


def is_game_over(player_list, boolean_flag):
    """This function

    Args: 
        player_list: 
        boolean_flag: 

    Return: 
        Returns a boolean if the user is correct or not.
    """

    result = True
    if boolean_flag == False:
        # loops to see if any of the mystery word has not been answered.
        for i in range(len(puzzle_display)):
            if puzzle_display[i]=="_":
                result =  False

    # Check if the varable "result" does or not hold False or True.
    if result != False:
        winner = 0
        Highest_Score = player_list[0]

        # Loops until has the highest score of the game.
        for i in range(1, len(player_list)):
            if player_list[i] > Highest_Score:
                Highest_Score = player_list[i]
                winner = i
            result = True
        
        # Prints when a player wins. 
        print("\nWinner: " + "Player " + str(winner))

    # Returns if the user is correct or not.
    return result


def to_solve():
    """This function has a if statement to see if the users guess of the word 
        is correct.

    Args: 
        None:

    Return: 
        Returns a string showing if the ueser is correct or not.
    
    """
    # Gets the user input to solve the puzzle.
    user_input_solve = input("Enter a string to solve the puzzle : ")

    # If statement to see if the user is correct or not.
    if user_input_solve == PLAY_STRING:
        print("CORRECT!")
        output = True
    else:
        print("WRONG!")
        output = False

    # Returns a varable holding if the user is correct or not.
    return output


def show_phrase_score(player_scores):
    """This function builds a string holding the player scores and the
            mystery word.

    Args: 
        player_scores: This hold the score for the players.

    Return: 
        Returns a string holding the player scores and the mystery word.
    
    """
    result = " " # empty string


    # builds a score out put for all of the players.
    for i in range(len(player_scores)):
        result += "\nPlayer " + str(i) + ": "+ str(player_scores[i]) + " "
    
    puzzle_display_str = "" # empty string

    #   
    for letter in puzzle_display:
        puzzle_display_str += "" + letter + " "
    
    # Returns the string
    return ("\n=======================\nPUZZLE:\n" + puzzle_display_str +
            "\n\nSCORE:"+ result)


################################################################################
#                                                                              #
#     DO NOT ALTER THE CODE BELOW                                              #
#                                                                              #
################################################################################

def game_loop():
    """Game loop for wheel-of-fortune

    Main loop responsible for running and managing the wheel-of-fortune game.
    """

    # Initialize player scores, load the puzzle, and build the wheel
    players = []

    many_players = int(input("Enter the number of players: "))

    j = 0
    while j < many_players:
        players.append(0)
        j += 1

    load_string()
    build_wheel()

    i = 0
    play_num = 0
    is_over = False
    solved = False

    # Play the game
    while not is_over:

        print(show_phrase_score(players))

        # Prompt players for enter a guess or solve
        vow_let_sol = int(input("\nPlayer " + str(play_num) +
            ": Buy Vowel(0), Guess Letter(1), or Solve(2)? "))
        lose_turn = False

        # Player chooses to buy a vowel
        if vow_let_sol == 0:

            if players[play_num] + VOWEL_COST >= 0:
                t_n_t = there_not_there(play_num, True)
                players = adjust_player_total(players, play_num, VOWEL_COST,
                    False)

                if t_n_t == 0:
                    lose_turn = True

            # Player has insufficient funds to buy a vowel
            else:
                print("\nInsufficient Funds to Buy a Vowel")
                lose_turn = True

        #Player chooses to guess a non-vowel letter
        elif vow_let_sol == 1:
            spin = input("\nPlayer " + str(play_num) +
                ": Press Enter to Spin ")
            value = spin_wheel()

            # If does not land on bankrupt, player chooses letter
            #     and score is adjusted
            if value != -1:
                print(str(value) + " per letter")
                t_n_t = there_not_there(play_num, False)
                players = adjust_player_total(players, play_num, value*t_n_t,
                    False)

                # Player guesses letter not in puzzle
                if t_n_t == 0:
                    lose_turn = True

            # Adjust score for bankrupt
            else:
                players = adjust_player_total(players, play_num, 0, True)
                lose_turn = True

        # Player chooses to solve the puzzle
        else:
            solved = to_solve()

            # Player did not guess correctly
            if not solved:
                lose_turn = True

        # Player loses turn if guess is incorrect
        if lose_turn == True:
            i = i + 1
            play_num = i % len(players)
            print("\nSORRY...Turn Goes To Player " + str(play_num))

        # Detect if the game is over
        is_over = is_game_over(players, solved)

if __name__ == "__main__":
    game_loop() 