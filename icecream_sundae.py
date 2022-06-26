flavors = ["vanilla", "chocolate", "strawberry"]
toppings = ["whipped cream", "nuts", "a cherry"]

def icecream_sundae(flavors, toppings):
    icecream_combinations = []
    for flavor in flavors:
        for topping in toppings:
            icecream_combinations.append(f"{flavor} with {topping}")
    return icecream_combinations


print(icecream_sundae(flavors, toppings))


# def icecream_sundae(flavors, toppings):
#     result = []
#     for flavor in flavors:
#         for topping in toppings:
#             pair = flavor + " with " + topping
#             result.append(pair)
#     return result

# def icecream_sundae(flavors, toppings):
#     result = []
#     for flavor_index in range(len(flavors)):
#         for topping_index in range(len(toppings)):
#             pair = flavors[flavor_index] + " with " + toppings[topping_index]
#             result.append(pair)
#     return result

# def icecream_sundae(flavors, toppings):
#     result = []
#     flavor_index = 0
#     topping_index = 0
#     while flavor_index < len(flavors):
#         topping_index = 0
#         while topping_index < len(toppings):
#             pair = flavors[flavor_index] + " with " + toppings[topping_index]
#             result.append(pair)
#             topping_index += 1
#         flavor_index += 1
#     return result
