#!/usr/bin/env python3

def give_list():
    return [100, 200, 300, 'six hundred']

def give_first_item():
    return str(give_list()[0])

def give_first_and_last_item():
    lst = give_list()
    return [lst[0], lst[-1]]

def give_second_and_third_item():
    lst = give_list()
    return [lst[1], lst[2]]
