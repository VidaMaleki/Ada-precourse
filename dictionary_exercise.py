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

def most_commonly_used_letter(string_to_analyze):
    word_dict = {}
    for letter in string_to_analyze:
        if letter in word_dict:
            word_dict[letter] += 1
        else:
            word_dict[letter] = 1

    max_value = 0
    max_letter = ""
    for key, value in word_dict.items():
        if value > max_value:
            max_value = value
            max_letter = key

    print(f"{max_letter} was used {max_value} times.")

most_commonly_used_letter("elephant")
most_commonly_used_letter("kangaroo")

# Most commonly used letter follow up: 
# What helper functions could you create 
# to divide up the work in "most_commonly_used_letter"?
# Refactor your code to use at least one helper function.


# Create Squares Dictionary
# Write a function "create_squares_dict" that takes an integer 
# parameter "max_square", and returns a dictionary with keys 
# 1 through max_square and their values being the squares of 
# the keys.
# For example, if we pass 5 as "max_square", then our output  
# should be {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

def create_squares_dict(max_square):
    dict = {}
    for index in range(1, max_square + 1):
        dict[index] = index * index
    return dict

squares_dict = create_squares_dict(5)
print(squares_dict)

# Create Sum of Squares
# Write a function that takes a dictionary parameter 
# "squared_numbers" like the dictionary returned by 
# create_squares_dict, and returns an integer that is 
# the sum of all of the dictionary values. 
# For example, if we pass {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} 
# as our parameter "squared_numbers", then our output  
# should be 55 (the value of 1 + 4 + 9 + 16 + 25)

def sum_of_squares(squared_numbers):
    sum = 0
    for square in squared_numbers.values():
        sum += square
    return sum

print(sum_of_squares(squares_dict))

