#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers
"""

def find_peak(list_of_integers):
    """
    finds num that's greater than both left and right
    """
    lint = list_of_integers
    if lint == []:
        return None
    total = len(lint)
    if total == 1:
        return lint[0]
    elif total == 2:
        return max(lint)
    middle = int(total / 2)
    peak = lint[middle]
    if peak > lint[middle - 1] and peak > lint[middle + 1]:
        return peak
    elif peak < lint[middle - 1]:
        return find_peak(lint[:middle])
    else:
        return find_peak(lint[middle + 1:])
