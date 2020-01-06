import os
import random
import sys
import unittest
import binary_search as bs


# Generates a random list of length numbers.
# IntValues parameter can be toggled to generate integer or floating point numbers.
def randomizeList(length, intValues=True):
    arr = []
    if intValues:
        for _ in range(length):
            arr.append(random.randint(-sys.maxsize + 1, sys.maxsize))
    else:
        for _ in range(length):
            # Generate a random number denoting if it its negative
            if (random.random() < 0.5):
                arr.append(random.random() * -sys.maxsize)
            else:
                arr.append(random.random() * sys.maxsize)

    return arr

class binarySearchTestCase(unittest.TestCase):

    # Confirm that passing an empty list will raise a ValueError 
    def test_empty_list(self):
        with self.assertRaises(ValueError):
            bs.binary_search([], random.randint(-sys.maxsize + 1, sys.maxsize))

    # Confirm that lists not containing the key will raise an IndexError
    def test_not_present(self):
        arr = [i for i in range(100)]
        with self.assertRaises(IndexError):
            bs.binary_search(arr, - 1)

    # Confirm a random value within the list can be found.
    def test_is_present(self):
        arr = randomizeList(100, True)
        arr.sort()
        random_element = arr[random.randint(0, 99)]
        ret_index = bs.binary_search(arr, random_element)
        self.assertEqual(arr[ret_index], random_element)

    # Confirm that unsorted lists will throw an Exception.
    def test_unsorted(self):
        arr = randomizeList(100, True)
        arr.sort()
        arr[0] = sys.maxsize
        with self.assertRaises(Exception):
            bs.binary_search(arr, random.randint(-sys.maxsize + 1, sys.maxsize))

    # Confirm it can find all elements within a list.
    def test_finds_all(self):
        arr = randomizeList(100, True)
        arr.sort()
        for i in range(100):
            ret_index = bs.binary_search(arr, arr[i])
            self.assertEqual(arr[ret_index], arr[i])

    # Confirm the algorithm works when a list has duplicate values
    def test_finds_dupes(self):
        arr = [0 for i in range(100)]
        self.assertEqual(bs.binary_search(arr, 0),  50 - 1)     

    # Confirm that floating point numbers do not break anything.
    def test_float_present(self):
        arr = randomizeList(100, False)
        arr.sort()
        for i in range(100):
            ret_index = bs.binary_search(arr, arr[i])
            self.assertEqual(arr[ret_index], arr[i])
    
    # Identical to not_present test but with floating point numbers,
    def test_float_not_present(self):
        arr = [i / 100000 for i in range(100)]
        with self.assertRaises(IndexError):
            bs.binary_search(arr, - 1)

    # Confirm non-list containers will raise a TypeError.
    def test_not_list(self):
        containers = [[0], {}, set(), ()]
        self.assertEqual(bs.binary_search(containers[0], 0), 0)
        for i in range(1, 4, 1):
            with self.assertRaises(TypeError):
                bs.binary_search(containers[i], 0)
        

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(binarySearchTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
