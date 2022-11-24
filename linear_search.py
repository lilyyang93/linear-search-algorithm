array_to_search_through = []
for number in range(1, 1001):
    array_to_search_through.append(number)

def linear_search(value_to_find, array_to_search_through):
    for index, num in enumerate(array_to_search_through):
        if num == value_to_find:
            return index
    return None

def linear_search_global(value_to_find, array_to_search_through):
    new_list = []
    for index, letter in enumerate(array_to_search_through):
        if letter == value_to_find:
            new_list.append(index)
    return new_list
