# Imports
import random

# Obtain Random Madlib
with open("blanklibs.txt", "r") as blanklibs:
    allmadlibs = blanklibs.readlines()
    amount_of_lines = int(allmadlibs[-1][:allmadlibs[-1].find(":")])
    random_int = random.randint(0, amount_of_lines - 1)
    madlib_info = allmadlibs[random_int]
    madlib_info = madlib_info[int(madlib_info.find(":")) + 1:]

    madlib_info = madlib_info.split(":")
    title = madlib_info[0]
    notsomadlib = madlib_info[1]

# Recieve User Input
tmp_word = ""
word_reading = False
user_words = []
for char in notsomadlib:
    if char == "]":
        word_reading = False

    if word_reading:
        tmp_word += char
    elif not word_reading and tmp_word != "":
        user_words.append(input("Name a/an " + tmp_word.lower() + ": "))
        tmp_word = ""

    if char == "[":
        word_reading = True

# Fill in the Blank
word_replacing = False
word_being_replaced = ""
user_word = ""
for char in notsomadlib:
    if char == "[":
        word_replacing = True
    
    if word_replacing:
        word_being_replaced += char
    elif not word_replacing and word_being_replaced != "":
        user_word = user_words.pop(0)
        notsomadlib = notsomadlib.replace(word_being_replaced, user_word, 1)
        word_being_replaced = ""
    
    if char == "]":
        word_replacing = False

# Clean Up
notsomadlib = notsomadlib.replace(". ", ".\n")
print("__________________________________________________\n")
print(title.upper() + "\n")
print(notsomadlib)
if random_int == (amount_of_lines - 1):
    print("")