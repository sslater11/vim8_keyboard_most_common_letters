#!/bin/env python3

# Toggle between a detailed or simple view of the similar letters table.
are_similar_letters_simple_view = False

# really lazy way to align lol.
def get_spacing( num ):
    spacing = ""

    if num   >= 10000:
        spacing = "     - "

    elif num >= 1000:
        spacing = "      - "

    elif num >= 100:
        spacing = "       - "

    elif num >= 10:
        spacing = "        - "

    elif num >= 0:
        spacing = "         - "

    return spacing

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


# Find similar letter pairs like "en,  ne" or "de, ed"
# Add thier frequency together and see if they are really common.
similar_letter_pairs = {}
for letter_pair in letter_pairs:
    letter_pair_reversed = letter_pair[::-1]
    if letter_pair_reversed in letter_pairs:
        if letter_pair == letter_pair_reversed:
            # ignore if it's a double letter like 'zz' or 'll'
            continue
        # add it to our new list if it's not already in there.
        if (letter_pair not in similar_letter_pairs) and (letter_pair_reversed not in similar_letter_pairs):
            # Add their frequencies together and add it to the dictionary.
            similar_letter_pairs[ letter_pair ] = letter_pairs[ letter_pair ] + letter_pairs[ letter_pair_reversed ]


# Move the most common letter pairs to the top of the list.
sorted_similar_letter_pairs = sorted(similar_letter_pairs.items(), key=lambda x: x[1], reverse=True)

if are_similar_letters_simple_view:
    print()
    print()
    print( " ----------------------------")
    print( " --- Similar letter pairs ---")
    print( " ----------------------------")
    print("letters |    percent   | total")
else:
    print()
    print()
    print( "-----------------------------------------------------------------------------------")
    print( "------------------------------- Similar letter pairs ------------------------------")
    print( "-----------------------------------------------------------------------------------")
    print("letters - frequency - percent | letters - frequency - percent | total - total percent")

for letter_pair in sorted_similar_letter_pairs:
    occurance_percent = (letter_pair[FREQUENCY] / total_letter_pairs_counted) * 100

    # Get the text "en", get it in reverse and make the string "en, ne"
    letter_pair_reversed = letter_pair[LETTERS][::-1]

    first_letter_pair = letter_pair[LETTERS]
    second_letter_pair = letter_pair[LETTERS][::-1] # reverse the string

    first_letter_pair_frequency  = letter_pairs[ first_letter_pair  ]
    second_letter_pair_frequency = letter_pairs[ second_letter_pair ]
    total_frequency              = first_letter_pair_frequency + second_letter_pair_frequency

    first_letter_pair_percent  = ( letter_pairs[first_letter_pair ] / total_letter_pairs_counted ) * 100
    second_letter_pair_percent = ( letter_pairs[second_letter_pair] / total_letter_pairs_counted ) * 100
    total_percent              = first_letter_pair_percent + second_letter_pair_percent


    # Make our strings with spacing and print.
    str_first_letter_pair_frequency  = str( first_letter_pair_frequency ) + get_spacing( first_letter_pair_frequency  )
    str_second_letter_pair_frequency = str( second_letter_pair_frequency) + get_spacing( second_letter_pair_frequency )
    str_total_frequency              = str( total_frequency )             + get_spacing( total_frequency )[4:]


    if are_similar_letters_simple_view:
        # A less detailed output
        str_first_letter_pair_percent  = str( format(first_letter_pair_percent,  '.2f') ) + "%"
        str_second_letter_pair_percent = str( format(second_letter_pair_percent, '.2f') ) + "% | "
        str_total_percent              = str( format(total_percent,              '.2f'))  + "%"
        print( first_letter_pair + ", " + second_letter_pair + "  | " + str_first_letter_pair_percent + ", " + str_second_letter_pair_percent + str_total_percent )
    else:
        str_first_letter_pair_percent  = str( format(first_letter_pair_percent,  '.2f') ) + "%   | "
        str_second_letter_pair_percent = str( format(second_letter_pair_percent, '.2f') ) + "%   | "
        str_total_percent              = str( format(total_percent,              '.2f'))  + "%"
        print( first_letter_pair + "      - " + str_first_letter_pair_frequency  + str_first_letter_pair_percent +
              second_letter_pair + "      - " + str_second_letter_pair_frequency + str_second_letter_pair_percent +
              str_total_frequency + str_total_percent)


