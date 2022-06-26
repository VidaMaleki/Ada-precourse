item = 3
list_of_items = [1, 3, 3, 6, 2, 3, 9]

def count_item_in_list(item, list_of_items):
    count_item = 0
    for i in range(len(list_of_items)):
        if list_of_items[i] == item:
            count_item += 1
    return count_item
print(count_item_in_list(item, list_of_items))

# EXAMPLE 1
# def count_item_in_list(item, list_of_items):
#     count = 0
#     for current_item in list_of_items:
#         if current_item == item:
#             count += 1
#     return count

# EXAMPLE 2
# def find_index_of_item(item, list_of_items):
#     count = -1
#     index = 0
#     while index < len(list_of_items):
#         if list_of_items[count] == item:
#             count += count
#         index += 1
#     return count
