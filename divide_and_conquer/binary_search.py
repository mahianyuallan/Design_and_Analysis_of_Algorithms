"""

Author: Allan Mwenja
Date: 18th November 2023, Wednesday

An Implementation of binary search
-----------------------------------

This script allows user to search for an element in a list using the binary
search algorithm

This file can also be imported as a module and contains the following
functions:

    * binary_search - returns -1 if the element is not found or the index of
       the element if it is found.

"""


def binary_search(ordered_list, element):
    """Finds an element in a list using binary search.

        Parameters
        ----------
        ordered_list : list
            The list from which an element is to be searched

        element : any
            The element to be searched in the list

        Returns
        -------
        index_of_element or -1
            the index of the element if found or -1 if the element is not found

        Raises
        ------
        TypeError
            If type of ordered_list is not list
    """

    if type(ordered_list) != list:
        raise TypeError("First argument ordered_list needs to be a list.")

    # sorts list just in case the list is not ordered
    ordered_list = sorted(ordered_list)

    start = 0
    end = len(ordered_list) - 1

    while start <= end:
        # The int() automatically floors decimal
        mid_index = int((start + end)/2)

        if ordered_list[mid_index] == element:
            return mid_index

        elif element < ordered_list[mid_index]:
            end = mid_index - 1

        else:
            start = mid_index + 1

    return -1


if __name__ == "__main__":
    a_list = [i for i in range(10000)]
    print(binary_search(a_list, 3000))
