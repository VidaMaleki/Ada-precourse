import random
from wonderwords import RandomWord
#https://pypi.org/project/wonderwords/

RANGE_LOW = 0
RANGE_HIGH = 100

SNOWMAN_GRAPHIC = [
    '*   *   *  ',
    ' *   _ *   ',
    '   _[_]_ * ',
    '  * (")    ',
    '  \( : )/ *',
    '* (_ : _)  ',
    '-----------'
]

SNOWMAN_WRONG_GUESSES = len(SNOWMAN_GRAPHIC)

SNOWMAN_MAX_WORD_LENGTH = 8
SNOWMAN_MIN_WORD_LENGTH = 5

def guess_the_number():
    random_number = random.randint(RANGE_LOW, RANGE_HIGH)

    correct_guess = False
    while not correct_guess:
        user_input = get_number_from_user()

        if user_input < RANGE_LOW or user_input > RANGE_HIGH:
            print(f"Your guess is out of bounds.")
            print(f"It must be between {RANGE_LOW} and {RANGE_HIGH}")
        elif user_input == random_number:
            print("You guessed the number!  Good job!")
            correct_guess = True
        elif user_input > random_number:
            print("Your guess is too high")
        elif user_input < random_number:
            print("Your guess is too low")

def get_number_from_user():
    valid_input = False
    user_input = None
    while not valid_input:
        user_input_string = input("Guess the number: ")

        if user_input_string.isnumeric():
            user_input = int(user_input_string)
            valid_input = True
        else:
            print("You must input a number!")

    return user_input


# Snowman Section
def snowman(snowman_word):
    """Complete the snowman function
    replace "pass" below with your own code
    It should print 'Congratulations, you win!'
    If the player wins and, 'Sorry, you lose! The word was {snowman_word}' if the player loses
    """
    correct_guesses_list = []
    snowman_dict = build_word_dict(snowman_word)
    wrong_guesses_list = []
    while len(wrong_guesses_list) < SNOWMAN_MAX_WRONG_GUESSES:
        user_input = get_letter_from_user(snowman_dict, wrong_guesses_list)
        if user_input in snowman_dict:
            correct_guesses_list.append(user_input)
            print("You guessed a letter that's in the word!")
            snowman_dict[user_input] = True
            if len(correct_guesses_list) == len(snowman_word):
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



def get_letter_from_user(list1, list2):
    valid_input = False
    user_input_string = None
    while not valid_input:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("You must input a letter!")
        elif len(user_input_string) > 1:
            print("You can only input one letter at a time!")
        elif user_input_string in list1 or user_input_string in list2:
            print("You already guessed that letter")
        else:
            valid_input = True

    return user_input_string


def print_snowman(wrong_guesses_count):
    for i in range(SNOWMAN_WRONG_GUESSES - wrong_guesses_count,
                   SNOWMAN_WRONG_GUESSES):
            print(SNOWMAN_GRAPHIC[i])

def build_word_dict(word):
    word_dict = {}
    for letter in word:
        if not letter in word_dict:
            word_dict[letter] = False
    return word_dict

def get_word_progress(word, word_dict):
    output = []
    result = True
    
    for i in word:
        if word_dict[i] == True:
            output.append(i)
        else:
            result = False
            output.append("_")
    print(" ".join(output))
    return result

#guess_the_number()
snowman()
