def __is_sorted(arr):
    """Simple helper method to check if a list is sorted in ascending order"""
    for i in range (len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False

    return True

def binary_search(arr, key):
    """ Simple binary search algorithm that returns the index of occurance.
        If passed list is not sorted in ascending order, it will be sorted.
        Empty Lists will return ValueErrors, 
    """

    if not isinstance(arr, list):
        raise TypeError("Non-list object passed")
    # An empty list has no contents. 
    if len(arr) == 0:
        raise ValueError("Passed list is empty")
      
    # Binary search is not defined for an unsorted list.
    if not __is_sorted(arr):
        raise Exception("Passed list is not sorted")

    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if key > arr[mid]:
            low = mid + 1
        elif key < arr[mid]:
            high = mid - 1
        else:
            return mid

    # Key is not present
    raise IndexError("List does not contiain key")