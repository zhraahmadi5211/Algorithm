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
        print(f"Call {start} to {end} ===============>", A[start:end + 1], ":", A)
        p = partition(A, start, end)
        print("After:", A)
        print("P:",p)
        qsort(A, start, p - 1)
        qsort(A, p + 1, end)
    else:
        print(f"Call {start} to {end} NOP *****************") 
        

A = [7, 8, 5, 9, 3, 2]
print(A)
qsort(A, 0, len(A) - 1)
print("output:", A)

