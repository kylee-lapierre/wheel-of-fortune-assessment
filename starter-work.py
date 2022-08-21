import random
from config import dictionary_loc
blank_word = []
file = open(dictionary_loc, 'r')
dictionary = file.read().splitlines()
file.close()
round_word = "hello"
round_letters = list(enumerate(round_word))
blank_word = list("_"*len(round_word))
letter = 'l'

print(round_letters)
for index, value in round_letters:
    if letter in value:
        blank_word.pop(index)
        blank_word.insert(index, value)
print(" ".join(blank_word))