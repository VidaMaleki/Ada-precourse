# Your local library needs a program to help folx checkout books online 

# Write a function called check_out_book that has a parameter called num_availalable_copies that is an integer. The function should:
    # check if there is remaining inventory
        # if there are remaining copies then 
            # update the inventory to indicate a copy has been checked out
            # return a string that tells the user their checkout is complete and how many copies are remaining
        # if there are NO remaining copies then
            # return a string that tells the user that there are no available copies right now.

# You will need to write 2 helper functions 

# One helper function can be called update_inventory and should update the number of copies available after a copy has been checked out

# The other helper function can be called check_inventory_availability and should check if there are copies available
    # if there are any available then it will return True 
    # if there are NOT any copies available then it will return false 

def check_out_book(num_availalable_copies): 
    if check_inventory_availability(num_availalable_copies):
        remaining_available_copies = update_inventory(num_availalable_copies)
        return f"Your checkout is complete! There are {remaining_available_copies} copies remaining."
    else:
        return "Sorry, there are no copies available to check out right now."

def update_inventory(book_inventory):
    return book_inventory - 1

def check_inventory_availability(book_inventory):
    if book_inventory >= 1:
        return True
    else: 
        return False

available_copies = 4
print(check_out_book(available_copies))
