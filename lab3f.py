#!/usr/bin/env python3

my_list = [1,2,3,4,5]

def add_item_to_list(ordered_list): # Appends a new number to the end of my_list with a value +1 of last number
    last_item = ordered_list[-1]
    new_last_item = last_item + 1
    ordered_list.append(new_last_item)


def remove_items_from_list(ordered_list, items_to_remove): # Removes all values found in items_to_remove list from my_list
    for remove_item in items_to_remove: 
        for existing_num in ordered_list:
            if existing_num == remove_item:
                ordered_list.remove(remove_item)

#Main code
if __name__ == '__main__':
    print(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)
    remove_items_from_list(my_list, [1,5,6])
    print(my_list)