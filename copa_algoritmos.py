
def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1

        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


def median_of_three(arr, a, b, c):
    x = arr[a]
    y = arr[b]
    z = arr[c]

    if x < y:
        if y < z:
            return b
        elif x < z:
            return c
        else:
            return a
    else:
        if x < z:
            return a
        elif y < z:
            return c
        else:
            return b


def partition(arr, low, high):
    mid = (low + high) // 2
    pivot_index = median_of_three(arr, low, mid, high)

    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def RafaelSort(arr):
    n = len(arr)

    if n <= 1:
        return arr

    stack = [(0, n - 1)]

    while stack:
        low, high = stack.pop()

        while low < high:

            if high - low < 24:
                insertion_sort(arr, low, high)
                break

            p = partition(arr, low, high)
    return arr
