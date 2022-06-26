# Most commonly used letter
# Write a function "most_commonly_used_letter" that takes a
# string as a parameter then prints out what letter was used
# the most and how many times it was used in the form
# "<letter> was used <number> times."
# If multiple letters have the same count, the first
# value found with that count is returned.
# For example:
# If input is "elephant", the function prints "e was used 2 times.".
# If the input is "kangaroo", the function prints "a was used 2 times.".

def most_commonly_used_letter(string):
    letters = list(string)
    count = 0
    max_letter = letters[0]
    for letter in letters:
        most_common = letters.count(letter)
        if (most_common > count):
            count = most_common
            max_letter = letter
    return max_letter


            
print(most_commonly_used_letter("manam"))
