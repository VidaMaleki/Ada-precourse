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
