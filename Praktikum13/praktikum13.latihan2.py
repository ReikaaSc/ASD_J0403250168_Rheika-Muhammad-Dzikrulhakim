# Nama  : Rheika Muhammad Dzikrulhakim
# NIM   : J0403251068
# Kelas : TPL A1
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Latihan 2 - Implementasi Sederhana Algoritma Kruskal
# ==========================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, "C", "D"),
    (2, "A", "C"),
    (3, "B", "D"),
    (4, "A", "B"),
    (5, "A", "D"),
]

# Mengurutkan edge berdasarkan bobot terkecil.
edges.sort()

mst = []
total_weight = 0
connected = set()

for weight, u, v in edges:
    # Memilih edge yang tidak membentuk cycle sederhana.
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight

        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total_weight)

# Jawaban Analisis:
# 1. Edge yang dipilih pertama kali adalah C-D dengan bobot 1.
# 2. Edge paling kecil dipilih dulu karena cara kerja Kruskal memang mulai dari
#    biaya yang paling ringan. Nanti kalau edge itu membuat cycle, baru dilewati.
# 3. Total bobot MST yang dihasilkan adalah 6, dari edge C-D, A-C, dan B-D.
# 4. Edge A-B dan A-D tidak dipilih karena saat sampai ke bagian itu semua node
#    sudah terhubung. Kalau tetap dimasukkan, hasilnya bukan makin efisien,
#    tetapi malah menambah bobot dan membuat jalur berulang.
