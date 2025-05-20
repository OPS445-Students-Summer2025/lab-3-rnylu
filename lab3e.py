#!/usr/bin/env python3

mylist = [100,200,300,'six hundred']

def give_list():
    return mylist
def give_first_item():
    return str(mylist[0])
def give_first_and_last_item():
    first_last = [mylist[0], mylist[-1]]
    return first_last
def give_second_and_third_item():
    second_third = [mylist[1], mylist[2]]
    return second_third

print(give_list())
print(give_first_item())
print(give_first_and_last_item())
print(give_second_and_third_item())