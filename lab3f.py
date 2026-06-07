#!/usr/bin/env python3

my_list = [1, 2, 3, 4]

def add_item_to_list(my_list):
    if len(my_list) == 4:
        my_list.extend([5, 6])
    elif len(my_list) == 6:
        my_list.extend([7, 8])

def remove_items_from_list(my_list, items):
    for item in items:
        if item in my_list:
            my_list.remove(item)
