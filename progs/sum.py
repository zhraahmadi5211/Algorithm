
def sum(A):
    s = 0
    counter = 1
    for a in A:
        for b in A:
            s += a*b
            counter += 2
    return s, counter

A = range(100000)
print(A)
S,c = sum(A)
print("?:", S)
print("Dastoorat:", c)
