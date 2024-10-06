

def qsort(A):
    print("===================> A:",A)
    if len(A) <= 1:
        print("nop")
        return A
    pivot = A[0]
    print("*** pivot:", pivot)
    P = []
    Q = []
    for a in A[1:]:
        if a <= pivot:
            P.append(a)
        else:
            Q.append(a)
    print("P:",P)
    print("Q:",Q)
    M = qsort(P)
    N = qsort(Q)
    print("M:",M)
    print("N:",N)
    L = M + [pivot] + N
    print("----------- pivot:", pivot)
    print("M + [pivot] + N")
    print("L:",L)
    L = M + [pivot] + N
    return L

A = [7,8,5,9,3,2]
B = qsort(A)
print(B)
