G = [[0, 3, 1000, 6],
     [1000,0 , 2, 2],
     [5, 1, 0, 1000],
     [1, 1000, 1000, 0]]

n = 4

P = [[0]*4]*4


def floyd(G, P, n):
    D = G
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    P[i][j] = k

    return D,P


def path(i, j):
    v = P[i][j]
    if v == 0:
        print("->", end="")
        return
    path(i, v)
    print(v, end="")
    path(v, j)

def print_path(i, j):
    print(i, end="")
    path(i,j)
    print(j)


print("P:", P)
D,P = floyd(G,P,n)
print("D:", D)
print("P:", P)

print_path(3,1)
