# Praktikum 3: Mengubah Matriks ke List
# Nama : Rheika Muhammad Dzikrulhakim
# NIM : J0403251068


def matrixToList(matrix):
    # Hitung jumlah node dari ukuran matrix (jumlah baris)
    V = len(matrix)
    adj = {i: [] for i in range(V)}  # Inisialisasi tiap node

    # Cek semua kemungkinan pasangan node i -> j
    for i in range(V):
        for j in range(V):
            if matrix[i][j] == 1:  # Jika ada edge, tambahkan ke list
                adj[i].append(j)

    # Kembalikan hasil dalam bentuk adjacency list
    return adj


def praktikum3():
    # Data contoh adjacency matrix
    matrix = [
        [0, 1, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [0, 0, 1, 0],
    ]

    V = len(matrix)

    # Tampilkan matrix asal
    print("\nAdjacency Matrix (input):")
    print("    ", end="")
    for j in range(V):
        print(f"[{j}]", end=" ")
    print()
    for i in range(V):
        print(f"[{i}] ", end="")
        for j in range(V):
            print(f" {matrix[i][j]} ", end=" ")
        print()

    # Proses konversi
    adj = matrixToList(matrix)

    # Tampilkan adjacency list hasil konversi
    print("\nHasil Konversi - Adjacency List:")
    print("-" * 45)
    for node in range(V):
        print(f"  Node {node}: {adj[node]}")

if __name__ == "__main__":
    # Titik masuk program saat file dijalankan langsung
    praktikum3()
