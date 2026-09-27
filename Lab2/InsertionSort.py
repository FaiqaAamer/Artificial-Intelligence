array = [2, 4, 5, 1, 3]
for i in range(1, len(array)):
    key = array[i]
    j = i - 1
    while j >= 0 and array[j] > key:
        array[j + 1] = array[j]
        j = j - 1
    array[j + 1] = key
    print("Sorted Array: ", array)
