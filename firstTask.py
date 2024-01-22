import random
import time


def start_first_task(name):
    print("Type 1 to fill at random, type 2 to fill yourself, type another key to exit")
    inp = input()

    if inp not in "12":
        return

    array = []
    print("Enter size of array")
    n = int(input())

    if inp == "1":
        array = fill_array(n)
        print(array)
    elif inp == "2":
        print("Fill the array with numbers")
        ar = input().split()
        for i in range(n):
            array.append(int(ar[i]))

    start_time = time.time()
    if name == 2:
        selection_sort(array)
    elif name == 1:
        insertion_sort(array)
    elif name == 3:
        buble_sort(array)
    elif name == 5:
        start_quick_sort(array)
    elif name == 4:
        MergeSort(array)
    else:
        return

    end_time = time.time()

    print("Time spent on sorting:", end_time - start_time)

    print(array)


def fill_array(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(1, 1000))
    return arr


def buble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(i):
            if array[j] > array[i]:
                array[j], array[i] = array[i], array[j]


def MergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_arr = array[:mid]
        right_arr = array[mid:]

        MergeSort(left_arr)
        MergeSort(right_arr)

        i, k, j = 0, 0, 0
        while i < len(left_arr) and k < len(right_arr):
            if left_arr[i] < right_arr[k]:
                array[j] = left_arr[i]
                i += 1
            else:
                array[j] = right_arr[k]
                k += 1
            j += 1

        while i < len(left_arr):
            array[j] = left_arr[i]
            j += 1
            i += 1

        while k < len(right_arr):
            array[j] = right_arr[k]
            j += 1
            k += 1


def selection_sort(array):
    for i in range(len(array)):
        temp_max = i
        for j in range(i, len(array)):
            if array[temp_max] > array[j]:
                temp_max = j
        array[i], array[temp_max] = array[temp_max], array[i]


def insertion_sort(array):
    for i in range(len(array)):
        temp_i = i
        while temp_i > 0 and array[temp_i - 1] > array[temp_i]:
            array[temp_i], array[temp_i - 1] = array[temp_i - 1], array[temp_i]
            temp_i -= 1


def start_quick_sort(array):
    array = quick_sort(array, 0, len(array) - 1)
    print(*array)


def quick_sort(arr, s, e):
    if s < e:
        mid = (s + e) // 2
        pivot = arr[mid]
        index = partition(arr, s, e, pivot)
        quick_sort(arr, s, index - 1)
        quick_sort(arr, index, e)

    return arr


def partition(arr, k, r, pivot):
    while k <= r:
        while arr[k] < pivot:
            k += 1

        while arr[r] > pivot:
            r -= 1

        if k <= r:
            arr[k], arr[r] = arr[r], arr[k]
            k += 1
            r -= 1

    return k
