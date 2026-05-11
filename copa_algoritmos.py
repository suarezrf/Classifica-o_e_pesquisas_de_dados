def insertion_sort(arr, left, right):
    i = left + 1

    while i <= right:
        key = arr[i]
        j = i - 1

        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        i += 1


def median_of_three(arr, low, high):
    mid = (low + high) // 2

    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]

    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]

    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]

    arr[mid], arr[high - 1] = arr[high - 1], arr[mid]

    return arr[high - 1]


def partition(arr, low, high):
    pivot = median_of_three(arr, low, high)

    i = low
    j = high - 1

    while True:

        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            break

        arr[i], arr[j] = arr[j], arr[i]

    arr[i], arr[high - 1] = arr[high - 1], arr[i]

    return i


def rafael_sort(arr):
    n = len(arr)

    if n <= 1:
        return arr

    stack = [(0, n - 1)]

    while stack:
        low, high = stack.pop()

        while low < high:

            if high - low <= 24:
                insertion_sort(arr, low, high)
                break

            pivot_index = partition(arr, low, high)

            if pivot_index - low < high - pivot_index:
                stack.append((pivot_index + 1, high))
                high = pivot_index - 1
            else:
                stack.append((low, pivot_index - 1))
                low = pivot_index + 1

    return arr
