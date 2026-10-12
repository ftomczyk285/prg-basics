###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print('Title in capital letters: ', movie.upper())

# print title in small letters
print('Title in small letters: ', movie.lower())

# print how many times the vowel "e" appears in the title
print(f'Vovel "e" appears {movie.count("e")} in the title')

# print where in the text is the word "Lord"
print(f'The word "Lord" is located on index {movie.find("Lord")}')

# print where in the text is the word "dragon"
dragon_location = movie.find("dragon")
if dragon_location > -1:
    print(f'The word "dragon" is located on index {dragon_location}')
else:
    print('The word "dragon" is not present in the title')