tea_flavor = {"oolong": 4.50 , "jasmine": 4.50 , "silver needle": 5.00}
milk_options = {"none": 0.00 , "dairy": 0.50 , "oat": 0.75 , "soy": 0.50}
boba_options = {"yes": 0.50, "no": 0.00}

def calculate_total(flavor, milk, boba):
    total = tea_flavor[flavor] + milk_options[milk] + boba_options[boba]
    return total

def drink_summary(flavor, milk, boba):
    total = calculate_total(flavor, milk, boba)

    print('*** Drink Summary ***')
    drink_display = flavor.capitalize()
    if milk != 'none' or boba != 'no':
        drink_display = drink_display + ' with '
    if milk != 'none':
        drink_display = drink_display + milk + ' milk'
    if milk != 'none' and boba != 'no':
        drink_display = drink_display + ' and '
    if boba != 'no':
        drink_display = drink_display + 'boba'
    
    print(drink_display)
    print(f'Drink total: {total}')
    
print(calculate_total("jasmine", "dairy", "yes"))