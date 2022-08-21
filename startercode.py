import random
from config import dictionary_loc
from config import turn_text_loc
from config import wheel_text_loc
from config import max_rounds
from config import vowel_cost
from config import round_status_loc
from config import final_prize
from config import final_round_text_loc

players = {0:{"Round Total":0,"Game Total":0,"Name":""},
         1:{"Round Total":0,"Game Total":0,"Name":""},
         2:{"Round Total":0,"Game Total":0,"Name":""}}

# VARIABLES
round_number = 0
counters = 0
dictionary = []
turn_text = ""
wheel_list = []
round_word = ""
round_letters = []
blank_word = []
vowels = {"a", "e", "i", "o", "u"}
round_status = ""
final_round_text = ""

def read_dictionary_file():
    global dictionary
    file = open(dictionary_loc, 'r')
    dictionary = file.read().splitlines()
    file.close()

def read_turn_Txt_file():
    global turn_text   
    #read in turn intial turn status "message" from file
    file = open(turn_text_loc, 'r')
    turn_text = file.read().splitlines()
    file.close()

def read_final_round_Txt_file():
    global final_round_text   
    #read in turn intial turn status "message" from file
    file = open(final_round_text_loc, 'r')
    final_round_text = file.read().splitlines()
    file.close()

def read_round_status_Txt_file():
    global round_status 
    file = open(round_status_loc, 'r')
    round_status = file.read().splitlines()
    file.close()

def read_wheel_Txt_file():
    global wheel_list
    file = open(wheel_text_loc)
    wheel_list = file.read().splitlines()
    file.close()

def get_player_info():
    global players
    players[0]["Name"] = input("Name for the first player? ")
    players[1]["Name"] = input("Name for the second player? ")
    players[2]["Name"] = input("Name for the third player? ")

def game_setup():
    global turn_text
    global dictionary    
    read_dictionary_file()
    read_turn_Txt_file()
    read_wheel_Txt_file()
    get_player_info()
    read_round_status_Txt_file()
    read_final_round_Txt_file() 

def get_word():
    global dictionary
    round_word = random.choice(dictionary)
    round_letters = list(round_word)
    blank_word = list("_"*len(round_word))
    return round_word, blank_word, round_letters

def wof_round_setup():
    global players
    global round_word
    global blank_word
    for i in range(0,3):
        players[i]["Round Total"] = 0
    player_number = random.choice(list(players.keys()))
    get_word()
    return player_number

def spin_wheel(player_number):
    global wheel_list
    global players
    global vowels
    # Get random value for wheel_list
    slices = random.choice(wheel_list)
    # Check for bankrupcy, and take action.
    if slices == "Bankrupt":
        if player_number == 0:
            print("Bankrupt, " + players.get(player_number)["Name"] + " lost all money.") 
            players[player_number]["Game Total"] = 0
            player_number = 1
            print("Now onto " + players.get(player_number)["Name"] + ".")
        elif player_number == 1:
            print("Bankrupt, " + players.get(player_number)["Name"] + " lost all money.")
            players[player_number]["Game Total"] = 0
            player_number = 2
            print("Now onto " + players.get(player_number)["Name"] + ".")
        elif player_number == 2:
            print("Bankrupt, " + players.get(player_number)["Name"] + " lost all money.") 
            players[player_number]["Game Total"] = 0
            player_number = 0
            print("Now onto " + players.get(player_number)["Name"] + ".")
    # Check for lose a turn
    elif slices == "Lose a turn":
        if player_number == 0:
            print(players.get(player_number)["Name"] + " lost a turn.") 
            player_number = 1
            print("Now onto " + players.get(player_number)["Name"] + ".")
        elif player_number == 1:
            print(players.get(player_number)["Name"] + " lost a turn.")
            player_number = 2
            print("Now onto " + players.get(player_number)["Name"] + ".")
        elif player_number == 2:
            print(players.get(player_number)["Name"] + " lost a turn.") 
            player_number = 0
            print("Now onto " + players.get(player_number)["Name"] + ".")
    # Get amount from wheel if not loose turn or bankruptcy
    # Ask user for letter guess
    else:
        letter = input("What letter would you like to guess? ")
        while letter.isalpha() != True:
            print("That is an incorrect guess, please try again.")
            letter = input("What letter would you like to guess? ")
        guess_letter(letter, player_number)
    # Use guessletter function to see if guess is in word, and return count
    # Change player round total if they guess right.     
    return still_in_turn


def guess_letter(letter, player_number): 
    global players
    global blank_word
    # parameters:  take in a letter guess and player number
    if players[player_number]["Round Total"] < 250:
        letter = input("What letter would you like to guess?")
        while letter in ('a', 'e', 'i', 'o', 'u'):
            print("That letter is a vowel, you do not have enough money to buy a vowel. Please try again.")
            letter = input("What letter would you like to guess?")
        if letter in round_word:
            good_guess = True
            for index, value in round_letters:
                if letter in value:
                    blank_word.pop(index)
                    blank_word.insert(index, value)
                    count = count + 1
        elif letter not in round_word:
            good_guess = False
            print('change')
    elif players[player_number]["Round Total"] >= 250:
        letter = input("What letter would you like to guess?")
        while letter not in ('a', 'e', 'i', 'o', 'u'):
            print("That letter is not a vowel ")
    # Change position of found letter in blank_word to the letter instead of underscore 
    # return good_guess = true if it was a correct guess
    # return count of letters in word. 
    # ensure letter is a consonate.    
    return good_guess, count

def buy_vowel(player_number):
    global players
    global vowels
    if players[player_number]["Round Total"] < 250:
        print("You do not have enough money to buy a vowel, please guess a consonant.")
        guess_letter()
    else:
        guess_letter()
    # Take in a player number
    # Ensure player has 250 for buying a vowel cost
    # Use guess_letter function to see if the letter is in the file
    # Ensure letter is a vowel
    # If letter is in the file let goodGuess = True
    
    return good_guess      
        
def guess_word(player_number):
    global players
    global blank_word
    global round_word
    
    # Take in player number
    # Ask for input of the word and check if it is the same as wordguess
    # Fill in blankList with all letters, instead of underscores if correct 
    # return False ( to indicate the turn will finish)  
    
    return False
    
    
def wof_turn(player_number):  
    global round_word
    global blank_word
    global turn_text
    global players

    # take in a player number. 
    # use the string.format method to output your status for the round
    print(f"End of round {round_number} status:")
    for i in round_status:
        for j in players.keys():
            print(i.format(players[j]["Name"], players[j]["Round Total"]))
    # and Ask to (s)pin the wheel, (b)uy vowel, or G(uess) the word using
    turn_choice = input("Would you like to spin the wheel (s), buy a vowel (b), or guess the word (g)? [s, b, or g]")
    if turn_choice == 's':
        spin_wheel(player_number)
    elif turn_choice == 'b':
        buy_vowel(player_number)
    elif turn_choice == 'g':
        guess_word(player_number)
    # Keep doing all turn activity for a player until they guess wrong
    # Do all turn related activity including update roundtotal 
    
    still_in_turn = True
    while still_in_turn:
        
        # use the string.format method to output your status for the round
        # Get user input S for spin, B for buy a vowel, G for guess the word
                
        if (choice.strip().upper() == "S"):
            stillinTurn = spin_wheel(player_number)
        elif (choice.strip().upper() == "B"):
            stillinTurn = buy_vowel(player_number)
        elif (choice.upper() == "G"):
            stillinTurn = guess_word(player_number)
        else:
            print("Not a correct option")        
    
    # Check to see if the word is solved, and return false if it is,
    # Or otherwise break the while loop of the turn.     


def wof_round():
    global players
    global round_word
    global blank_word
    global round_status
    init_player = wof_round_setup()
    
    # Keep doing things in a round until the round is done ( word is solved)
        # While still in the round keep rotating through players
        # Use the wofTurn fuction to dive into each players turn until their turn is done.
    
    # Print roundstatus with string.format, tell people the state of the round as you are leaving a round.

def wof_final_round():
    global round_word
    global blank_word
    global final_round_text
    win_player = 0
    amount = 0
    
    # Find highest gametotal player.  They are playing.
    # Print out instructions for that player and who the player is.
    # Use the getWord function to reset the roundWord and the blankWord ( word with the underscores)
    # Use the guessletter function to check for {'R','S','T','L','N','E'}
    # Print out the current blankWord with whats in it after applying {'R','S','T','L','N','E'}
    # Gather 3 consonats and 1 vowel and use the guessletter function to see if they are in the word
    # Print out the current blankWord again
    # Remember guessletter should fill in the letters with the positions in blankWord
    # Get user to guess word
    # If they do, add finalprize and gametotal and print out that the player won 


def main():
    game_setup()    

    for i in range(0,max_rounds):
        if i in [0,1]:
            wof_round()
        else:
            wof_final_round()

if __name__ == "__main__":
    main()