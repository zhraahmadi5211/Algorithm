def switch(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def inplace(A, pivot):
    i = 0
    j = 0
    while j < len(A):
        #print("i:", i)
        #print("j:", j)
        if A[j] < pivot:
            #print("Before:",A)
            switch(A, i, j)
            #print(f"------switch i:{i} j:{j} ------")
            #print("After:",A)
            i += 1
        j += 1
    switch(A, i, j-1)
    return i

def qsort(A, start, end):
    print("===================> A:",A)
    if end <= start:
        print("nop")
    pivot = A[0]
    print("*** pivot:", pivot)
    p = inplace(A, pivot)
    print("After:", A)
    print("P:",A[:p])
    print("Q:",A[p +1:])
    qsort(A, start, p -1 )
    qsort(A, p + 1, end)

A = [7,8,5,9,3,2]
print(A)
qsort(A, 0, len(A))
print("output:", A)

#print("A[3:4]:", A[3:4])
#print("A[1:5]:", A[1:5])
#print("A[:5]:", A[:5])
#print("A[4:]", A[4:])
