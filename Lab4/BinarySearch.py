def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the index of the target value.

    Parameters:
    arr (list): A sorted list of elements.
    target: The value to search for in the array.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2     #Use integer division

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

#Example usage:
numbers = [6, 12, 17, 23, 38, 45, 77, 90]   #Sorted array
target = 45
result = binary_search(numbers, target)

if result != -1:
    print(f"Target {target} found at index: {result}")
else:
    print(f"Target {target} not found in the array.")