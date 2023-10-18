# Inbuilt modules
import unittest
from random import shuffle

# Local modules
from divide_and_conquer.binary_search import binary_search
from divide_and_conquer.merge_sort import get_merge_sorted_list
from divide_and_conquer.quick_sort import get_quick_sorted_list


class TestBinarySearch(unittest.TestCase):

    def test_finding_present_element(self):
        """
        Test that it can find an element existing in a list.
        """
        test_list = [1, 2, 3, 4]
        self.assertEqual(binary_search(test_list, 3), 2, "Should be 2")

    def test_finding_absent_element(self):
        """
        Test that it can find an element absent from a list.
        """
        test_list = [1, 2, 3, 4]
        self.assertEqual(binary_search(test_list, 6), -1, "Should be -1")


class TestMergeSort(unittest.TestCase):

    def test_merge_sort_sorts_unordered_list(self):
        """
        Test that merge-sort can sort an unordered list.
        """
        test_list = [i for i in range(1000)]
        shuffle(test_list)
        expected_result = sorted(test_list)
        self.assertEqual(get_merge_sorted_list(test_list), expected_result)

    def test_merge_sort_sorts_ordered_list(self):
        """
        Test that merge-sort can sort an already sorted list correctly.
        """
        test_list = [1, 2, 3, 4]
        self.assertEqual(get_merge_sorted_list(test_list), test_list)

    def test_merge_sort_sorts_empty_list(self):
        """
        Test that merge-sort can sort an empty list.
        """
        test_list = []
        self.assertEqual(get_merge_sorted_list(test_list), test_list)


class TestQuickSort(unittest.TestCase):

    def test_quick_sort_sorts_unordered_list(self):
        """
        Test that quick_sort can sort an unordered list.
        """
        test_list = [i for i in range(1000)]
        shuffle(test_list)
        expected_result = sorted(test_list)
        self.assertEqual(get_quick_sorted_list(test_list), expected_result)

    def test_quick_sort_sorts_ordered_list(self):
        """
        Test that quick can sort an already sorted list correctly.
        """
        test_list = [1, 2, 3, 4]
        self.assertEqual(get_quick_sorted_list(test_list), test_list)

    def test_quick_sort_sorts_empty_list(self):
        """
        Test that it can sorts an empty list.
        """
        test_list = []
        self.assertEqual(get_quick_sorted_list(test_list), test_list)


if __name__ == "__main__":
    unittest.main()
