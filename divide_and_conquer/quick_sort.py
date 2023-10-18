"""

Author: Mike Farad
RegNo: P15/102164/2017
Date: 15th November 2019, Friday

An Implementation of quick sort
-----------------------------------

This script allows user to sort elements in a list using the quick sort
algorithm which is an implementation of the divide and conquer problem solving
strategy.

This file can also be imported as a module and contains the following
functions:

    * quick_sort - recursively divides and sorts the subsections with use of a
        pivot

    * partition - returns the index of the pivot

    * get_quick_sorted_list - returns a sorted version of the list passed to it
        as an argument

"""

# Local module
from divide_and_conquer.helper import print_list


def quick_sort(my_list, start, end):
    """Recursively divides and sorts the subsections with use of a pivot

        Parameters
        ----------
        my_list : list
            The list that is to be sorted

        start : int
            The least index of the list/sub-list excluding the pivot index

        end : int
            The highest index of the list/sub-list excluding the pivot index

        Raises
        ------
        TypeError
            If type of my_list is not list
    """
    if type(my_list) != list:
        raise TypeError("First argument my_list needs to be a list.")

    if start >= end:
        return

    p_index = partition(my_list, start, end)
    quick_sort(my_list, start, p_index-1)
    quick_sort(my_list, p_index + 1, end)


def partition(my_list, start, end):
    pivot = my_list[end]  # Pivot is always the rightmost element in the list
    p_index = start

    for index in range(start, end):

        if my_list[index] <= pivot:
            # Swapping of the elements in case condition is met
            my_list[index], my_list[p_index] = my_list[p_index], \
                my_list[index]

            p_index += 1

    my_list[end], my_list[p_index] = my_list[p_index], my_list[end]

    return p_index


def get_quick_sorted_list(my_list: list):
    """Simply returns the sorted version of the passed list.

        Parameters
        -----------
        my_list : list
            List to be sorted using quick sort

        Returns
        --------
        my_list : list
            Sorted version of my_list

        Raises
        ------
        TypeError
            If type of my_list is not list
    """
    start = 0
    end = len(my_list) - 1

    quick_sort(my_list, start, end)
    return my_list


if __name__ == "__main__":
    a_list = [7, 6, 5, 4, 3, 2, 1, 0]
    quick_sort(a_list, 0, 7)
    print_list(a_list)
