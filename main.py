import sys
import time
import numpy as np

sys.setrecursionlimit(10**7)

def load_tests(filename="input.txt"):
    tests = []
    with open(filename, "r") as f:
        for line in f:
            arr = np.array(list(map(float, line.split())))
            tests.append(arr)
    return tests

def quick_sort(a, l, r):
    if l >= r:
        return
    p = a[(l + r) // 2]
    i, j = l, r
    while i <= j:
        while a[i] < p:
            i += 1
        while a[j] > p:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    if l < j:
        quick_sort(a, l, j)
    if i < r:
        quick_sort(a, i, r)

def heapify(a, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and a[l] > a[largest]:
        largest = l
    if r < n and a[r] > a[largest]:
        largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)

def heap_sort(a):
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, i, 0)

def merge(a, l, mid, r):
    L = a[l:mid + 1]
    R = a[mid + 1:r + 1]
    i = j = 0
    k = l
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        a[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        a[k] = R[j]
        j += 1
        k += 1

def merge_sort(a, l, r):
    if l < r:
        mid = (l + r) // 2
        merge_sort(a, l, mid)
        merge_sort(a, mid + 1, r)
        merge(a, l, mid, r)

def numpy_sort(a):
    return np.sort(a)

tests = load_tests("input.txt")
for i, test in enumerate(tests):
    print(f"\nTest case {i + 1}")
    # QuickSort
    a = test.copy()
    start = time.perf_counter()
    quick_sort(a, 0, len(a) - 1)
    t_quick = time.perf_counter() - start
    print(f"QuickSort  : {t_quick:.6f} giây")
    # HeapSort
    a = test.copy()
    start = time.perf_counter()
    heap_sort(a)
    t_heap = time.perf_counter() - start
    print(f"HeapSort   : {t_heap:.6f} giây")
    # MergeSort
    a = test.copy()
    start = time.perf_counter()
    merge_sort(a, 0, len(a) - 1)
    t_merge = time.perf_counter() - start
    print(f"MergeSort  : {t_merge:.6f} giây")
    # NumPy sort
    a = test.copy()
    start = time.perf_counter()
    np.sort(a)
    t_numpy = time.perf_counter() - start
    print(f"NumPy sort : {t_numpy:.6f} giây")
