# Guess the Animal 
# Write a program that asks the user 3 yes or no 
# questions to get information, then let them try to
# guess the animal.
#
# Steps
# 1. Create a constant to hold the animal the user is guessing.
# 2. Use the `input` function to ask the user 3 questions about 
#    the animal that they can answer with "Y" for yes or "N" 
#    for no.
# 3. For each question, use a conditional to let the  
#    user know if their guess was correct or not.
# 4. Finally, use `input` one more time to let the user try to
#    guess the animal you've stored in your constant from step 1
#    and let them know if they got it right!
#
# TIP: Uppercase letters don't compare to the same value as 
#      lowercase. For example the expression `"YOU" == "you"` 
#      evaluates to `false`. If you want the user to be able to 
#      enter "T" or "t" for `true`, you can use the string 
#      function `.lower()` to change user input to lowercase 
#      before comparing it to the expected answer!
ANIMAL = "Giraffe"
print("***Let's Play Game!***") 
print("Guess the animal! answer with Y \ N " )

question_1 = input("Q1: Is it a mamal? ")
if question_1 == "y":
    print("Your guess is correct.")
else:
    print("Your guess is wrong. ")
question_2 = input("Q2: Does it live in water? ")
if question_2 == "n":
    print("Your guess is wrong")
    question_3 = input("Q3: Is it a carnivorous? ")
    if question_3 == "n":
        print("eee")
    else:
        print("ggg")
else:
    print("You're right! one more to go;)")
    question_3 = input("Q3: Is it a large animal?")
    if question_3 == "y":
        print("mmm")
    else:
        print("uuuu")
        
        
        
        
ANIMAL = "kangaroo"
YES_LETTER_VALUE = "y"
NO_LETTER_VALUE = "n"
CORRECT_MESSAGE = "Correct!"
INCORRECT_MESSAGE = "Incorrect!"
INPUT_ERROR_MESSSAGE = "Sorry, I couldn't understand your guess!"

# Question 1
is_a_mammal = input("Is this animal a mammal? (Y/N) ")
is_a_mammal_lowercase = is_a_mammal.lower()
if is_a_mammal_lowercase == YES_LETTER_VALUE:
    print(CORRECT_MESSAGE)
elif is_a_mammal_lowercase == NO_LETTER_VALUE:
    print(INCORRECT_MESSAGE)
else:
    print(INPUT_ERROR_MESSSAGE)
print("The animal is a mammal.")

# Question 2
has_four_legs = input("Does this creature stand on four legs? (Y/N) ")
has_four_legs_lowercase = has_four_legs.lower()
if has_four_legs_lowercase == YES_LETTER_VALUE:
    print(INCORRECT_MESSAGE) 
elif has_four_legs_lowercase == NO_LETTER_VALUE:
    print(CORRECT_MESSAGE)
else:
    print(INPUT_ERROR_MESSSAGE)
print("This animal stands on two legs.")

# Question 3
has_a_pouch = input("Does this animal have a pouch? (Y/N) ")
has_a_pouch_lowercase = has_a_pouch.lower()
if has_a_pouch_lowercase == YES_LETTER_VALUE:
    print(CORRECT_MESSAGE) 
elif has_a_pouch_lowercase == NO_LETTER_VALUE:
    print(INCORRECT_MESSAGE)
else:
    print(INPUT_ERROR_MESSSAGE)
print("This animal has a pouch.")

# Ask user to guess the animal
animal_guess = input("What animal do you think it is? ")
animal_guess_lowercase = animal_guess.lower()
if animal_guess_lowercase == ANIMAL:
    print("You guessed the animal! Congratulations!")
else:
    print(f"Sorry! The animal was {ANIMAL}!")