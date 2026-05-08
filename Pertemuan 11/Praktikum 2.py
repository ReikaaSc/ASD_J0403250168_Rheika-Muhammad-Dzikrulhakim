# Praktikum 2: Representasi Graph dengan Adjacency List
# Nama : Rheika Muhammad Dzikrulhakim
# NIM : J0403251068

def createGraph(V, edges):
    adj = [[] for _ in range(V)]

    # menambah edge ke adjacency list
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)  # graph nya undirected jadi bebas

    return adj


if __name__ == "__main__":
    V = 4
    # list edge (u, v) menggunakan indeks vertex
    edges = [(0, 1), (0, 2), (1, 3), (2, 3)]

    # buat graph menggunakan edge
    adj = createGraph(V, edges)

    print("Adjacency List Representation:")
    for i in range(V):
        # print vertex jadi huruf
        vertex = chr(ord('A') + i)
        print(f"{vertex}:", end=" ")
        # print adjacent vertices jadi huruf
        for j in adj[i]:
            adj_vertex = chr(ord('A') + j)
            print(adj_vertex, end=" ")
        print()