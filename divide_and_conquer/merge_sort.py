"""

Author: Allan Mwenja
Date: 18th October 2023, Wednesday 

An Implementation of merge sort
-----------------------------------

This script allows user to sort elements in a list using the merge sort
algorithm which is an implementation of the divide and conquer problem solving
strategy.

This file can also be imported as a module and contains the following
functions:

    * merge - merges subsets of the list created by merge  sort in an ordered
        way.

    * merge_sort - divides the list recursively in to two up until the elements
        can't be divided further and merges the subsets of the list into a
        single list by calling merge.

    * get_merge_sorted_list - returns a sorted version of the list passed to
        it as an argument

"""

from divide_and_conquer.helper import print_list


def merge(left_list, right_list, my_list):
    """Merges two subsets of list into a larger set of ordered elements

        Parameters
        ----------
        left_list : list
            The first set of the pair of subsets to be merged

        right_list : list
            The second set of the pair of subsets to be merged

        my_list : list
            An unordered combination of the left and right list

        Raises
        ------
        TypeError
            If type of my_list is not list
    """
    if type(my_list) != list:
        raise TypeError("First argument my_list needs to be a list.")

    left_list_len = len(left_list)
    right_list_len = len(right_list)

    unfilled_r = 0  # Index of smallest unfilled element in the right list
    unfilled_l = 0  # Index of smallest unfilled element in the left list
    position_to_fill = 0

    while unfilled_l < left_list_len and unfilled_r < right_list_len:

        if left_list[unfilled_l] <= right_list[unfilled_r]:
            my_list[position_to_fill] = left_list[unfilled_l]
            unfilled_l += 1

        else:
            my_list[position_to_fill] = right_list[unfilled_r]
            unfilled_r += 1

        position_to_fill += 1

    # Checking if any element was left
    while unfilled_l < left_list_len:
        my_list[position_to_fill] = left_list[unfilled_l]
        unfilled_l += 1
        position_to_fill += 1

    while unfilled_r < right_list_len:
        my_list[position_to_fill] = right_list[unfilled_r]
        unfilled_r += 1
        position_to_fill += 1


def merge_sort(my_list: list):
    """Divides the passed list recursively into smaller subsets up until the
        subsets/sub-lists can no longer be divided and then merges them with
        help from merge() in an ordered way.

        Parameters
        -----------
        my_list : list
            List to be sorted using merge sort

        Raises
        ------
        TypeError
            If type of my_list is not list
    """

    list_len = len(my_list)

    if list_len > 1:

        mid = list_len//2 + 1 if list_len % 2 != 0 else list_len//2
        left_list = my_list[:mid]
        right_list = my_list[mid:]

        merge_sort(left_list)
        merge_sort(right_list)

        merge(left_list, right_list, my_list)


def get_merge_sorted_list(my_list: list):
    """Simply returns the sorted version of the passed list.

        Parameters
        -----------
        my_list : list
            List to be sorted using merge sort

        Returns
        --------
        my_list : list
            Sorted version of my_list

        Raises
        ------
        TypeError
            If type of my_list is not list
    """

    merge_sort(my_list)
    return my_list


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    print_list(arr)
    merge_sort(arr)
    print("Sorted array is: ", end="\n")
    print_list(arr)
