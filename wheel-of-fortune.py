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

round_number = 0
counters = 0
dictionary = []
turn_text = ""
wheel_list = []
round_word = ""
round_letters = []
blank_word = []
vowels = ("a", "e", "i", "o", "u")
round_status = ""
final_round_text = ""
final_letters = list(enumerate(["R", "S", "T", " L", "N", "E"]))
still_in_turn = True

def beginning():
    print("\nWelcome to the Wheel of Fortune!")
    print("There will be two rounds of play then a final round where someone will try to win the grand prize!")
    print("Let's meet our players!")
    print(("="*100) + "\n")
beginning()

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
    global round_word
    global round_letters
    global blank_word
    # random.choice(dictionary)
    round_word = "Hello"
    round_letters = list(enumerate(round_word))
    blank_word = list("_"*len(round_word))
    print("\n" + ' '.join(blank_word), str(len(blank_word)) + " letters\n")
    return round_word, blank_word, round_letters

def wof_round_setup():
    global players
    global player_number
    global round_number
    for i in range(0,3):
        players[i]["Game Total"] = players[i]["Game Total"] + players[i]["Round Total"]
        players[i]["Round Total"] = 0
    player_number = random.choice(list(players.keys()))
    get_word()
    round_number = round_number + 1
    return player_number, round_number

def spin_wheel(player_number):
    global wheel_list
    global players
    global vowels
    global slices
    global still_in_turn
    
    # Get random value for wheel_list
    slices = random.choice(wheel_list)

    # Check for bankrupcy, and take action.
    if slices == "Bankrupt":
        if player_number == 0:
            print("\nBankrupt, " + players.get(player_number)["Name"] + " lost all money.") 
            players[player_number]["Game Total"] = 0
            player_number = 1
            print("\nNow onto " + players.get(player_number)["Name"] + ".")
        elif player_number == 1:
            print("\nBankrupt, " + players.get(player_number)["Name"] + " lost all money.")
            players[player_number]["Game Total"] = 0
            player_number = 2
            print("\nNow onto " + players.get(player_number)["Name"] + ".")
        elif player_number == 2:
            print("\nBankrupt, " + players.get(player_number)["Name"] + " lost all money.") 
            players[player_number]["Game Total"] = 0
            player_number = 0
            print("\nNow onto " + players.get(player_number)["Name"] + ".")
    
    # Check for lose a turn
    elif slices == "Lose a turn":
        if player_number == 0:
            print("\n" + players.get(player_number)["Name"] + " lost a turn.") 
            player_number = 1
            print("\nNow onto " + players.get(player_number)["Name"] + ".")
        elif player_number == 1:
            print("\n" + players.get(player_number)["Name"] + " lost a turn.")
            player_number = 2
            print("\nNow onto " + players.get(player_number)["Name"] + ".")
        elif player_number == 2:
            print("\n" + players.get(player_number)["Name"] + " lost a turn.") 
            player_number = 0
            print("\nNow onto " + players.get(player_number)["Name"] + ".")
    
    # Get amount from wheel if not loose turn or bankruptcy
    # Ask user for letter guess
    else:
        print(f"\nThe money amount of the wheel slice is ${slices}.")
        letter = input("What letter would you like to guess? ")
        while letter.isalpha() != True:
            print("\nThat is an incorrect guess, please try again.")
            letter = input("What letter would you like to guess? ")
        while good_guess == True:
            guess_letter(letter, player_number)
    # Use guess_letter function to see if guess is in word, and return count
    # Change player round total if they guess right.     
    return good_guess, player_number

def guess_letter(letter, player_number): 
    global players
    global blank_word
    global counters
    global good_guess

    # parameters: take in a letter guess and player number
    for i in letter:
        if i in round_word:
            good_guess = True
            for index, value in round_letters:
                if letter in value:
                    blank_word.pop(index)
                    blank_word.insert(index, value)
                    counters = counters + 1
            print(' '.join(blank_word))
            players[player_number]["Round Total"] = players[player_number]["Round Total"] + int(slices)*counters
        elif i not in round_word:
            good_guess = False
    # Change position of found letter in blank_word to the letter instead of underscore 
    # return good_guess = true if it was a correct guess
    # return count of letters in word. 
    # ensure letter is a consonate.    
    return good_guess, player_number


def buy_vowel(player_number):
    global players
    global vowels
    if players[player_number]["Round Total"] < vowel_cost:
        print("\nYou do not have enough money to buy a vowel, please guess a consonant.")
        letter = input("What letter would you like to guess? ")
        guess_letter(letter, player_number)
    else:
        letter = input("What letter would you like to guess? ")
        players[player_number]["Round Total"] = players[player_number]["Round Total"] - 250
        while letter not in vowels:
            print("\nThat letter is not a vowel, please try again.")
            letter = input("What letter would you like to guess? ")
        guess_letter(letter, player_number)
    
    # Take in a player number
    # Ensure player has 250 for buying a vowel cost
    # Use guess_letter function to see if the letter is in the file
    # Ensure letter is a vowel
    # If letter is in the file let good_guess = True
    return good_guess

def guess_word(player_number):
    global players
    global blank_word
    global round_word
    global word_guess
    global final_word_guess
    # Take in player number
    # Ask for input of the word and check if it is the same as wordguess
    word_guess = input("\nWhat word would you like to guess? ")
    if word_guess == round_word:
        for index, value in round_letters:
            blank_word.pop(index)
            blank_word.insert(index, value)
        if round_number == 3:
            final_word_guess = True
    # Fill in blankList with all letters, instead of underscores if correct 
    # return False (to indicate the turn will finish)  
    return False

def wof_turn(player_number):  
    global round_word
    global blank_word
    global turn_text
    global players
    global still_in_turn
    # take in a player number. 
    # use the string.format method to output your status for the round
    # and Ask to (s)pin the wheel, (b)uy vowel, or G(uess) the word using
    # Keep doing all turn activity for a player until they guess wrong
    # Do all turn related activity including update round_total 
    while still_in_turn == True:
        # use the string.format method to output your status for the round
        print("\n" + turn_text[0].format(players[player_number]["Name"]))
        # Get user input S for spin, B for buy a vowel, G for guess the word
        choice = input("Would you like to spin the wheel (S), buy a vowel (B), or guess the word (G)? [S, B, or G] ")
        if (choice.strip().upper() == "S"):
            still_in_turn = spin_wheel(player_number)
        elif (choice.strip().upper() == "B"):
            still_in_turn = buy_vowel(player_number)
        elif (choice.upper() == "G"):
            still_in_turn = guess_word(player_number)
        else:
            print("\nNot a correct option, please try again.")
    if good_guess == False:
        if player_number == 0:
            player_number = 1
            print("\nThat letter is not in the word.")
        elif player_number == 1:
            player_number = 2
            print("\nThat letter is not in the word.")
        elif player_number == 2:
            player_number = 0
            print("\nThat letter is not in the word.")
    # Check to see if the word is solved, and return false if it is    
    elif round_word == blank_word:
        return False

def wof_round():
    global players
    global round_word
    global blank_word
    global round_status
    wof_round_setup()
    
    # Keep doing things in a round until the round is done (word is solved)
        # While still in the round keep rotating through players
        # Use the wofTurn fuction to dive into each players turn until their turn is done.
    while still_in_turn == True:
            wof_turn(player_number)
    # Print roundstatus with string.format, tell people the state of the round as you are leaving a round.
    if round_number == 1:
        print(f"\nEnd of round {round_number} status:")
        for i in round_status:
            for j in players.keys():
                print(i.format(players[j]["Name"], players[j]["Round Total"]))
    elif round_number == 2:
        print(f"\nEnd of round {round_number} status:")
        for i in round_status:
            for j in players.keys():
                print(i.format(players[j]["Name"], players[j]["Round Total"]))

def wof_final_round():
    global round_word
    global blank_word
    global final_round_text

    game_totals = []
    final_player = []
    # Find highest game_total player.  They are playing.
    for i in players.keys():
        game_totals.append(players[i]["Game Total"])
    highest_total = max(game_totals)
    for i in players.keys():
        if players[i]["Game Total"] == highest_total:
            final_player.append(players[i]["Name"])
            final_player.append(players[i]["Game Total"])
            final_player.append(i)
    # Print out instructions for that player and who the player is.
    print("\n")
    for i in final_round_text:
        print(i.format(final_player[1], final_player[0], final_prize))
    # Use the get_word function to reset the round_word and the blank_word (word with the underscores)
    get_word()
    # Use the guess_letter function to check for {'R','S','T','L','N','E'}
    guess_letter(final_letters, final_player[2])
    # Print out the current blankWord with whats in it after applying {'R','S','T','L','N','E'}
    print(' '.join(blank_word))
    # Gather 3 consonats and 1 vowel and use the guessletter function to see if they are in the word
    first_consonant = str(input("What is the first consonant you would like to pick? "))
    while first_consonant in final_letters:
        print("That letter is within the given letters, please try again.")
        first_consonant = str(input("What is the first consonant you would like to pick? "))
    second_consonant = str(input("What is the second consonant you would like to pick? "))
    while second_consonant in final_letters:
        print("That letter is within the given letters, please try again.")
        second_consonant = str(input("What is the second consonant you would like to pick? "))
    third_consonant = str(input("What is the third consonant you would like to pick? "))
    while third_consonant in final_letters:
        print("That letter is within the given letters, please try again.")
        third_consonant = str(input("What is the third consonant you would like to pick? "))
    only_vowel = str(input("What is the only vowel you would like to pick? "))
    while only_vowel in final_letters:
        print("That letter is within the given letters, please try again.")
        only_vowel = str(input("What is the only vowel you would like to pick? "))
    # Print out the current blankWord again
    # Remember guess_letter should fill in the letters with the positions in blankWord
    guess_letter((first_consonant, second_consonant, third_consonant, only_vowel), final_player[2])
    print("\n" + " ".join(blank_word))
    print("Here is the word for you with the given letters and the letters you chose filled in.")
    # Get user to guess word
    guess_word(players[final_player[2]])
    # If they do, add finalprize and gametotal and print out that the player won 
    if final_word_guess == True:
        print(f"You won! The prize you won is {final_prize} and your game total is ${final_player[1]}.")

def main():
    game_setup()    
    for i in range(0,max_rounds):
        if i in [0,1]:
            wof_round()
        else:
            wof_final_round()

if __name__ == "__main__":
    main()