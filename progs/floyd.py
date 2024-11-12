G = [[0, 3, 1000, 6],
     [1000, 0, 2, 2],
     [5, 1, 0, 1000],
     [1, 1000, 1000, 0]]

# Create P matrix with the same shape as G and fill it with -1
P = [[-1 for _ in range(len(G))] for _ in range(len(G))]

def floyd(G, P):
    D = [row[:] for row in G]  # Create a copy of G
    n = len(G)  # Number of vertices

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    P[i][j] = k

    return D, P

def print_matrix(matrix, name):
    print(f"{name} matrix:")
    for row in matrix:
        print("[" + " ".join(f"{value:4}" for value in row) + "]")
    print()

def path(i, j):
    v = P[i][j]
    if v == -1:
        return  # No intermediate vertex
    path(i, v)
    print(" ->", v, end="")
    path(v, j)

def print_path(i, j):
    print(i, end="")
    path(i, j)
    print(" ->", j)

# Run the Floyd-Warshall algorithm
D, P = floyd(G, P)

# Print matrices D and P
print_matrix(D, "D")
print_matrix(P, "P")

# Print a path
print("\nPath from 2 to 0:")
print_path(2, 0)

