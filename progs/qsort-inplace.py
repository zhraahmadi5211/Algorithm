def switch(A, i, j):
    A[i], A[j] = A[j], A[i]

def partition(A, start, end):
    pivot = A[start]
    i = start
    for j in range(start + 1, end + 1):
        if A[j] < pivot:
            i += 1
            switch(A, i, j)
    switch(A, start, i)  # Move pivot to the correct position
    return i

def qsort(A, start, end):
    if start < end:
        p = partition(A, start, end)
        qsort(A, start, p - 1)
        qsort(A, p + 1, end)

A = [7, 8, 5, 9, 3, 2]
qsort(A, 0, len(A) - 1)
print("output:", A)

