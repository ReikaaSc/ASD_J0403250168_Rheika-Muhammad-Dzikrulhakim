# Nama  : Rheika Muhammad Dzikrulhakim
# NIM   : J0403251068
# Kelas : TPL A1
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Latihan 3 - Implementasi Algoritma Prim
# ==========================================================

import heapq

graph = {
    "A": {"B": 4, "C": 2, "D": 5},
    "B": {"A": 4, "D": 3},
    "C": {"A": 2, "D": 1},
    "D": {"A": 5, "B": 3, "C": 1},
}


def prim(graph_data, start):
    """Membangun MST dari node awal menggunakan priority queue."""
    visited = {start}
    edges = []

    for neighbor, weight in graph_data[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    while edges:
        weight, u, v = heapq.heappop(edges)

        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight

            for neighbor, w in graph_data[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight


mst, total = prim(graph, "A")

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total)

# Jawaban Analisis:
# 1. Node awal yang digunakan adalah A.
# 2. Edge pertama yang dipilih adalah A-C dengan bobot 2, karena dari node A
#    edge itulah yang paling murah dibanding A-B dan A-D.
# 3. Prim melihat pilihan edge dari node yang sudah masuk MST. Dari pilihan itu,
#    program mengambil yang bobotnya paling kecil dan menuju node yang belum
#    dikunjungi.
# 4. Total bobot MST yang dihasilkan adalah 6.
# 5. Prim terasa seperti membangun jaringan dari satu titik lalu diperluas.
#    Kruskal beda, karena dari awal ia melihat semua edge, mengurutkannya, lalu
#    memilih edge murah selama tidak membuat cycle.
