SNOWMAN_MIN_WORD_LENGTH = 5
SNOWMAN_MAX_WORD_LENGTH = 8
SNOWMAN_MAX_WRONG_GUESSES = 7

SNOWMAN_1 = '*   *   *  '
SNOWMAN_2 = ' *   _ *   '
SNOWMAN_3 = '   _[_]_ * '
SNOWMAN_4 = '  * (")    '
SNOWMAN_5 = '  \( : )/ *'
SNOWMAN_6 = '* (_ : _)  '
SNOWMAN_7 = '-----------'

def snowman(snowman_word):
    
    snowman_dict = build_word_dict(snowman_word)
    wrong_guesses_list = []
    while len(wrong_guesses_list) < SNOWMAN_MAX_WRONG_GUESSES:
        user_input = get_letter_from_user(snowman_dict, wrong_guesses_list)
        if user_input in snowman_dict:
            print("You guessed a letter that's in the word!")
            snowman_dict[user_input] = True
            if all(snowman_dict.values()):
                print("Congratulations, you win!")
                break
        else:
            print(f"The letter {user_input} is not in the word")
            wrong_guesses_list.append(user_input)
            if len(wrong_guesses_list) == SNOWMAN_MAX_WRONG_GUESSES:
                print(f"Sorry, you lose! The word was {snowman_word}")
                break
        print_snowman_graphic(len(wrong_guesses_list))
        get_word_progress(snowman_word, snowman_dict)
        wrong_guesses = " ".join(wrong_guesses_list)
        print(f"Wrong guesses: {wrong_guesses}")

# 
def print_snowman_graphic(num_wrong_guesses):
    """This function prints out the appropriate snowman image 
    depending on the number of wrong guesses the player has made.
    """
    
    for i in range(1, num_wrong_guesses + 1):
        if(i == 1):
            print(SNOWMAN_1)
        if(i == 2):
            print(SNOWMAN_2)
        if(i == 3):
            print(SNOWMAN_3)
        if(i == 4):
            print(SNOWMAN_4)
        if(i == 5):
            print(SNOWMAN_5)
        if(i == 6):
            print(SNOWMAN_6)
        if(i == 7):
            print(SNOWMAN_7)

def get_letter_from_user(snowman_word_dict, wrong_guesses_list):
    """This function takes the snowman_word_dict and the list of characters 
    that have been guessed incorrectly (wrong_guesses_list) as input.
    It asks for input from the user of a single character until 
    a valid character is provided and then returns this character.
    """

    valid_input = False
    user_input_string = None
    while not valid_input:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("You must input a letter!")
        elif len(user_input_string) > 1:
            print("You can only input one letter at a time!")
        elif user_input_string in snowman_word_dict and snowman_word_dict[user_input_string]:
            print("You already guessed that letter and it's in the word!")
        elif user_input_string in wrong_guesses_list:
            print("You already guessed that letter and it's not in the word!")
        else:
            valid_input = True

    return user_input_string

def build_word_dict(snowman_word):
    """This function takes snowman_word as input and returns 
    a dictionary with a key-value pair for each letter in 
    snowman_word where the key is the letter and the value is `False`.
    """
    snowman_word_dict = {}
    for letter in snowman_word:
        snowman_word_dict[letter] = False
    return snowman_word_dict

def get_word_progress(snowman_word, snowman_word_dict):
    """
    This function takes the snowman_word and snowman_word_dict as input.
    It prints an output_string that shows the correct letter guess placements 
    as well as the placements for the letters yet to be guessed.
    It returns True if all the letters of the word have been guessed, and False otherwise.
    """
    output_string = ""
    result = True
    for elem in snowman_word:
        if snowman_word_dict[elem]:
            output_string += elem
        else:
            result = False
            output_string += "_"
        output_string += " "
    print(output_string)
    return result