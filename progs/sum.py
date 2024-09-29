
def merge(P,Q):
    i, j = 0, 0
    M = []
    while i < len(P) and j < len(Q):
        if P[i] < Q[j]:
            M.append(P[i])
            i += 1
        else: 
            M.append(Q[j])
            j += 1
    if i < len(P):
        while i < len(P):
            M.append(P[i])
            i += 1
    else:
        while j < len(Q):
            M.append(Q[j])
            j += 1
    return M


def merge_sort(A):
    print("---------------------")
    print("Input:",A)
    n = len(A)
    if n <= 1:
        print("nop")
        return A

    m = n // 2
    P = merge_sort(A[0:m])
    print("P:",P)
    Q = merge_sort(A[m:])
    print("Q:",Q)
    L = merge(P,Q)
    print("L:", L)
    return L


A = [7,8,5,3,2]
print(A)
L = merge_sort(A)
print(L)
