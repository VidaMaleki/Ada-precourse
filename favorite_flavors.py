def favorite_flavors():
    icecream_flavors = []
    flavor = ""
    while not flavor == "done": # this loop will run until the 
                                # user types in the word "done"
        flavor = input("What is an icecream flavor that you like? ")
        icecream_flavors.append(flavor) # when we append something to a list,
                                        # we add it to the end of the list
    
    for flavor in icecream_flavors: # this loop will iterate over each element 
                                    # in the list, and store them one at a time 
                                    # in the variable flavor
        print(f"{flavor} is a great ice cream flavor!")

    return icecream_flavors

favorite_flavors()