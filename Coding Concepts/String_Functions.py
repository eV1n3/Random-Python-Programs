# Lists (cont...)
list = ["cartridge", "milk", "pizza", "lightbulb", "clock"]
item = list[3]
print(item)
print("\n")

# Strings are lists!?!
sentence = "Programming is fun!"
print(sentence)
for char in sentence:
    print(char)

# Case Manipulation
sentence = "hello world"
capitalize_sentence = sentence.capitalize()
print(capitalize_sentence)

sentence = "HELLO WORLD"
lowercase_sentence = sentence.lower()
print(lowercase_sentence)

sentence = "hello world"
uppercase_sentence = sentence.upper()
print(uppercase_sentence)

sentence = "hElLo WoRlD"
swapcase_sentence = sentence.swapcase()
print(swapcase_sentence)

# Search & Find
sentence = "Hey, my name is Ethan. I love programming and video games. Building my own stuff with code is really cool."
substring = "my"
substring_count = sentence.count(substring)
print(substring_count)

substring = "love"
substring_find_index = sentence.find(substring)
print(substring_find_index)
substring = "hacking"
substring_find_index = sentence.find(substring)
print(substring_find_index)
# THE CRASH IS INTENTIONAL!!!
substring_find_index = sentence.index(substring)
print(substring_find_index)

substring = "Hey"
startsWithPrefix = sentence.startswith(substring)
print(startsWithPrefix)
substring = "hey"
startsWithPrefix = sentence.startswith(substring)
print(startsWithPrefix)

# Modify & Format
sentence = "I like english"
old_substring = "english"
new_substring = "math"
replaced_sentence = sentence.replace(old_substring, new_substring)
print(replaced_sentence)

sentence = "                       Hello there!                       "
stripped_sentence = sentence.strip()
print(stripped_sentence)
sentence = "00000000000000000000000000000000000000000000000Squished by zeros0000000000000000000000000000000000000000000000000000"
stripped_sentence = sentence.strip("0")
print(stripped_sentence)

sentence = "Eggs, bacon, pancakes, sausage, potatoes o'brien"
separator = ", "
split_sentence = sentence.split(separator)
print(split_sentence)

separator = "\n"
reunited_list = separator.join(split_sentence)
print(reunited_list)

# Modify & Format (Format printing)
print("Hey there! My name is {} and my age is {}.".format("Ethan", 21))
score1 = 4
score2 = 7
print(f"Your first score is {score1} and your second score is {score2}. Your final score is {score1 + score2}!")

# Type Checking
sentence = "T3sTinG d1FF3r3nT Ch4r5"
test_alnum = sentence.isalnum()
print(test_alnum)

sentence = "HELL0 WORLD"
test_alpha = sentence.isalpha()
print(test_alpha)

sentence = "798245897248597098245"
test_digit = sentence.isdigit()
print(test_digit)

sentence = "i gotta whisper for this sentence"
test_lower = sentence.islower()
print(test_lower)

sentence = "I GOTTA YELL FOR THIS SENTENCE"
test_upper = sentence.isupper()
print(test_upper)

sentence = "                                                 "
test_whitespace = sentence.isspace()
print(test_whitespace)

sentence = "Treasure Island"
test_title = sentence.istitle()
print(test_title)

# Miscellaneous
sentence = "Hello, World!"
print(len(sentence))

num_to_str = str(21)
print(type(num_to_str))