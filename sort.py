import numpy as np
import time

m1 = 10
m2 = 100
m3 = 1000
m4 = 10000
m5 = 100000
m6 = 1000000

Best_Case_array = np.arange(m4)
Worst_Case_array = np.flip(Best_Case_array)
Mid_case_array = np.random.choice(range(m4), m4, replace=False)
nlen = len(Best_Case_array)

def bubble_sort(arr):
    def swapper(i,j):
        arr[i], arr[j] = arr[j], arr[i]

    n =len(arr)
    swapped = True

    x = -1
    while(swapped):
        swapped = False
        x += 1
        for i in range(1, n-x):
            if arr[i-1] > arr[i]:
                swapper(i-1, i)
                swapped = True

    return arr;


def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i

        for j in range(i +1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j

        arr[minimum], arr[i] =  arr[i], arr[minimum]

    return arr

def insertion_sort(arr):

    for i in range(len(arr)):
        cursor = arr[i]
        pos = i

        while pos > 0 and arr[pos-1] > cursor:
            arr[pos] = arr[pos-1]
            pos -= 1

        arr[pos] = cursor

    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2

    left, right  = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    return merge

def merge(left, right, merged):

    left_cursor, right_cursor = 0, 0
    while left_cursor < len (left) and right_cursor < len(right):

        if left[left_cursor] <= right_cursor[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]

            left_cursor += 1

        else:
            merged[left_cursor  + right_cursor] = right_cursor
            right_cursor +=1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2


    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap


        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


#################################################################

def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

########################



start_time = time.time()

#print(bubble_sort(Best_Case_array))
#print(bubble_sort(Mid_case_array))
#print(bubble_sort(Worst_Case_array))
#print(selection_sort(Best_Case_array))
#print(selection_sort(Mid_case_array))
print(selection_sort(Worst_Case_array))
#print(insertion_sort(Best_Case_array))
#print(insertion_sort(Worst_Case_array))
#print(insertion_sort(Mid_case_array))
#print(merge_sort(Best_Case_array))
#print(merge_sort(Worst_Case_array))
#heapSort(Worst_Case_array)
#quickSort(Mid_case_array,0,m5-1)
#nlen2 = len(Best_Case_array)
#quickSort(Best_Case_array,0,m5-2)
# quickSort(Worst_Case_array,0,m5-1)
#print(merge_sort(Mid_case_array))


print("--- %s seconds ---" % (time.time() - start_time))

