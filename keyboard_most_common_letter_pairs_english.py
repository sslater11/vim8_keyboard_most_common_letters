#!/bin/env python3

letter_pairs = {}

file = open("keyboard_most_common_words.txt", "r")
words=[]
line = file.readline()
while line:
    if line[0] == "#":
        # Skip commented lines in the text file.
        pass
    else:
        word, frequency = line.split("\t")
        words += [word.lower()] * int(frequency)

    line = file.readline()

file.close()


# Make the letter_pairs as a python dictionary, and increment it's value every time we find the pair.
for word in words:
    for i in range( len(word)-1 ):
        letters = word[i] + word[i+1]

        if letters in letter_pairs:
            # Increment the counter for that pair.
            letter_pairs[ letters ] = letter_pairs[ letters ] + 1
        else:
            # Add the letter pair as a new dictionary key.
            letter_pairs[ letters ] = 1


# Move the most common letter pairs to the top of the list.
sorted_letter_pairs = sorted(letter_pairs.items(), key=lambda x: x[1], reverse=True)


LETTERS   = 0
FREQUENCY = 1

total_letter_pairs_counted = 0
for i in sorted_letter_pairs:
    total_letter_pairs_counted += i[FREQUENCY]

print("letters - frequency - percent")
for letter_pair in sorted_letter_pairs:
    occurance_percent = (letter_pair[FREQUENCY] / total_letter_pairs_counted) * 100

    if letter_pair[FREQUENCY]   >= 10000:
        spacing = "     - "
    elif letter_pair[FREQUENCY] >= 1000:
        spacing = "      - "
    elif letter_pair[FREQUENCY] >= 100:
        spacing = "       - "
    elif letter_pair[FREQUENCY] >= 10:
        spacing = "        - "
    elif letter_pair[FREQUENCY] >= 1:
        spacing = "         - "

    print( letter_pair[LETTERS] + "      - " + str(letter_pair[FREQUENCY]) + spacing + str(round(occurance_percent,2)) + "%" )

