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
round_word = "Hello"
round_status = ""
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
final_round_text = ""
final_letters = list(enumerate(["R", "S", "T", " L", "N", "E"]))


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

    slices = random.choice(wheel_list)

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
    else:
        print(f"\nThe money amount of the wheel slice is ${slices}.")
        letter = input("What letter would you like to guess? ")
        while letter.isalpha() != True:
            print("\nThat is an incorrect guess, please try again.")
            letter = input("What letter would you like to guess? ")
        guess_letter(letter, player_number)

def guess_letter(letter, player_number):
    global players
    global blank_word
    global counters
    global good_guess

    for i in letter:
        if i in round_word:
            good_guess = True
            for index, value in round_letters:
                if letter in value:
                    blank_word.pop(index)
                    blank_word.insert(index, value)
                    counters = counters + 1
            print(" ".join(blank_word))
        elif i not in round_word:
            good_guess = False
    return good_guess, player_number, blank_word

wof_round_setup()

def buy_vowel(player_number):
    global players
    global vowels
    global letter

    letter = input("What letter would you like to guess? ")
    if letter in vowels and players[player_number]["Round Total"] < vowel_cost:
        print("\nYou do not have enough money to buy a vowel, please guess a consonant.")
        letter = input("What letter would you like to guess? ")
        while letter in vowels:
            print("You cannot afford a vowel, please try again.")
            letter = input("What letter would you like to guess? ")
    else:
        letter = input("What letter would you like to guess? ")
        players[player_number]["Round Total"] = players[player_number]["Round Total"] - 250
        while letter not in vowels:
            print("\nThat letter is not a vowel, please try again.")
            letter = input("What letter would you like to guess? ")
    guess_letter(letter, player_number)


buy_vowel(player_number)