#!/usr/bin/python3
""" Module containing the find_peak function """


def find_peak(list_of_integers):
    """ Function that finds a peak in a list of unsorted integers """

    if not list_of_integers:
        return None

    length = len(list_of_integers)
    if length == 1:
        return list_of_integers[0]
    elif length == 2:
        return max(list_of_integers)

    mid = length // 2
    if list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    elif list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid + 1:])
    else:
        return list_of_integers[mid]
