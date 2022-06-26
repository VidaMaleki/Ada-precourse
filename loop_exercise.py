'''
Best Burger Order Summary

Help Best Burger create a program to display a customer order summary. The Best Burger menu includes: $5.25 burger, $2.50 fries, and a $4.25 milkshake. 

Create a function called best_burger_order_summary. This function should have 3 main tasks:
    1) Getting a customer's order
    2) Calculating the total for the customer's order
    3) Displaying the customer's order in the terminal

Task #1: Getting a customer's order:
    - Create a constant variable called MENU_ITEMS that is a list of Best Burger's menu items. 
    - Create a flag variable called `order_in_progress`.
    - Create an empty list called `order_items`, this will hold every item the customer orders.
    - Repeat the process of asking the customer to order an item until they have decided to end their order (hint: a flag variable can come in handy here)
        - Continue to ask the user to enter valid menu items

Task #2: Calculating the total for the customer's order:
    - Store the total in a variable
    - Iterate through order_items and check if each item is either fries, milkshake, or burger. If so, then add the items price to the total

Task #3: Displaying the customer's order in the terminal
    - Use print statements and the a loop to match this expected output:
    *** Welcome to Best Burger ***
    Order Items: 
    fries
    burger
    Total: 7.75

Bonus challenge: Use helpers function! Separate each task into their own helper function
'''

########## SOLUTION #################

def best_burger_order_summary():
    MENU_ITEMS = ["fries", "burger", "milkshake"]

    order_in_progress = True
    order_items = []
    total = 0
    while order_in_progress:
        user_order = input(f"Here is our menu: \n{MENU_ITEMS}. \nWhat would you like to order? ")
        
        while user_order not in MENU_ITEMS:
            user_order = input("Sorry, we don't have that time on our menu. Please enter an item on our menu. ")
        order_items.append(user_order)
        add_to_order = input("Would you like to order anything else? Enter 'y' or 'n' ")

        while add_to_order != 'y' and add_to_order != 'n':
            add_to_order = input("Please enter 'y' or 'n' ")

        if add_to_order == 'n':
            order_in_progress = False
        

    for item in order_items:
        if item == 'fries':
            total += 2.50
        elif item == 'milkshake':
            total += 4.25
        elif item == 'burger':
            total += 5.25

    print("Order Summary: ")
    for item in order_items:
        print(item)
    print(f"Grand Total: {total}")

best_burger_order_summary()


######## HELPER FUNCTION SOLUTION #################

def calculate_total(order_items):
    total = 0
    for item in order_items:
        if item == 'fries':
            total += 2.50
        elif item == 'milkshake':
            total += 4.25
        elif item == 'burger':
            total += 5.25
    return total 

def customer_order_summary(order_items):
    total = calculate_total(order_items)
    
    print("Order Summary: ")
    for item in order_items:
        print(item)
    print(f"Grand Total: {total}")


def get_customer_order():
    MENU_ITEMS = ["fries", "burger", "milkshake"]

    order_in_progress = True
    order_items = []
    while order_in_progress:
        user_order = input(f"Here is our menu: \n{MENU_ITEMS}. \nWhat would you like to order? ")
        
        while user_order not in MENU_ITEMS:
            user_order = input("Sorry, we don't have that time on our menu. Please enter an item on our menu. ")
        order_items.append(user_order)
        add_to_order = input("Would you like to order anything else? Enter y or n. ")
        while (add_to_order != "y") and (add_to_order != "n"):
            add_to_order = input("Please enter y or n. Would you like to order anything else? ")

        if add_to_order == "n":
            order_in_progress = False

    return order_items


def best_burger_order_summary_refactored():
    print("*** Welcome to Best Burger ***")
    order_items = get_customer_order()
    customer_order_summary(order_items)

# best_burger_order_summary_refactored()