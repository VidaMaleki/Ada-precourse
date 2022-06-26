item = 3
list_of_items = [1, 4, 5, 6, 2, 3, 9]

def find_index_of_item(item, list_of_items):
    index = -1
    for i in range(len(list_of_items)):
        if list_of_items[i] == item:
            index = i
            break
    return index
            
            
print(find_index_of_item(item, list_of_items))



# list.index(x[, start[, end]])
# Arguments :
# x : Item to be searched in the list
# start : If provided, search will start from this index. Default is 0.
# end : If provided, search will end at this index. Default is the end of list.

# EXAMPLE (1)
# def find_index_of_item(item, list_of_items):
#     default = -1
#     count = 0
#     for current_item in list_of_items:
#         if current_item == item:
#             return count
#         count += 1
#     return default



# EXAMPLE (2)
# def find_index_of_item(item, list_of_items):
#     default = -1
#     count = 0
#     while count < len(list_of_items):
#         if list_of_items[count] == item:
#             return count
#         count += 1
#     return default