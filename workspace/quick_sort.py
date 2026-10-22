def quick_sort(arr):
    """
    Sorts an array of integers in ascending order using the QuickSort algorithm.

    :param arr: List[int] -- the list of integers to be sorted
    :return: List[int] -- the sorted list of integers
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Predefined lists
list1 = [3, 6, 8, 10, 1, 2, 1]
list2 = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6, 4, 1]
list3 = [4, 5, 1, 2, 8, 7, 6, 3]

# Sorting the lists
sorted_list1 = quick_sort(list1)
sorted_list2 = quick_sort(list2)
sorted_list3 = quick_sort(list3)
