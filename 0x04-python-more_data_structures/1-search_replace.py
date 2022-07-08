#!/usr/bin/python3
# 1-search_replace.py
# Brennan D Baraban <375@holbertonschool.com

def search_replace(my_list, search, replace):
    """Replace all occurrences of an element by another in a new list."""
    new_list = my_list[:]
    for item in my_list:
        new_list.append(item) if item != search else new_list.append(replace)
            return (new_list)
