

def customers_order():
    MENU_ITEMS = ["burger", "fries", "milkshake"]
    order_in_progress = True
    order_items = []
    while order_in_progress:
        user_order = input(f"Please order an item from our menue:\n {MENU_ITEMS}\n What would you like to order? ")
        while user_order not in MENU_ITEMS:
            user_order = input("Sorry, we don't have that time on our menu. Please enter an item on our menu. ")
        order_items.append(user_order)
        if order_in_progress == "done":
            break
    return order_items    
        
def total_calculation(order_items):   
    total = 0
    for item in order_items:
        if item =='fries':
            total += 2.50
        elif item == 'milkshake':
            total += 4.25
        elif item == 'burger':
            total += 5.25
    return total


def report(order_items):
    
    print(" *** Welcome to Best Burger ***")
    print("Order Items:")
    for item in order_items:
        print(item)
        
    print(total_calculation())

report()