#!/bin/env python3

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    ".",
    ","
]

letters_count = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0
]

# Put the most common letters at the start of the list.
def sort_letters():
    for i in range(len(letters)):
        for k in range(i, len(letters)):
            if letters_count[k] > letters_count[i]:
                temp_letter = letters[i]
                temp_count  = letters_count[i]

                letters[i]       = letters[k]
                letters_count[i] = letters_count[k]

                letters[k]       = temp_letter
                letters_count[k] = temp_count


file = open("keyboard_most_common_words.txt", "r")
words=""
line = file.readline()
while line:
    if line[0] == "#":
        # Skip commented lines in the text file.
        pass
    else:
        word, frequency = line.split("\t")
        # Add the word to the list as many times as it's frequency number says in the file.
        words += word.lower() * int(frequency)


    line = file.readline()

file.close()


# Increment the relevant letters_count[] element for every time we find a letter in the list.
for ch in words:
    for k in range(len(letters)):
        if letters[k] == ch:
            letters_count[k] += 1
            break


sort_letters()


total_letters_counted = 0
for i in letters_count:
    total_letters_counted += i


for i in range(len(letters)):
    occurance_percent = (letters_count[i] / total_letters_counted) * 100
    if letters_count[i] >= 10000:
        spacing = " - "
    elif letters_count[i] >= 1000:
        spacing = "  - "
    elif letters_count[i] >= 100:
        spacing = "   - "
    elif letters_count[i] >= 10:
        spacing = "    - "
    elif letters_count[i] >= 1:
        spacing = "     - "
    print( letters[i] + ": " + str(letters_count[i]) + spacing + str(round(occurance_percent,2)) + "%" )

