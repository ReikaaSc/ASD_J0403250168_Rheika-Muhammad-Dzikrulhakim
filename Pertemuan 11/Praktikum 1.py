# Praktikum 1: Representasi Graph dengan Matriks Adjacency
# Nama : Rheika Muhammad Dzikrulhakim
# NIM : J0403251068

def createGraph(V, edges):
    mat = [[0 for _ in range(V)] for _ in range(V)]

    # menambah edge ke matriks adjacency
    for u, v in edges:
        mat[u][v] = 1
        mat[v][u] = 1  # graph nya undirected jadi bebas

    return mat


if __name__ == "__main__":
    V = 4
    # list edge (u, v) menggunakan indeks vertex
    edges = [[0, 1], [0, 2], [1, 2], [2, 3]]

    # buat graph menggunakan edge
    mat = createGraph(V, edges)

    print("Adjacency Matrix Representation:")
    for i in range(V):
        for j in range(V):
            print(mat[i][j], end=" ")
        print()
