#!/usr/bin/python3
# Loop through the alphabet using the ASCII values of the characters
for letter in range(ord('a'), ord('z') + 1):
    # Check if the current character is not 'q' or 'e'
    if chr(letter) != 'q' and chr(letter) != 'e':
        # Print the character without a newline at the end
        print(chr(letter), end='')
