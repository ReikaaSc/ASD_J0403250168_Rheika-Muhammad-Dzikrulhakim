# Nama  : Rheika Muhammad Dzikrulhakim
# NIM   : J0403251068
# Kelas : TPL A1
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Latihan 4 - Studi Kasus Jaringan Kabel Antar Gedung
# ==========================================================

import heapq

# Representasi weighted graph untuk biaya pemasangan kabel antar gedung.
graph = {
    "GedungA": {"GedungB": 4, "GedungC": 2, "GedungD": 5},
    "GedungB": {"GedungA": 4, "GedungD": 3},
    "GedungC": {"GedungA": 2, "GedungD": 1},
    "GedungD": {"GedungA": 5, "GedungB": 3, "GedungC": 1},
}


def prim(graph_data, start):
    """Menentukan MST dengan algoritma Prim."""
    visited = {start}
    edges = []

    for neighbor, weight in graph_data[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_cost = 0

    while edges and len(visited) < len(graph_data):
        cost, u, v = heapq.heappop(edges)

        if v not in visited:
            visited.add(v)
            mst.append((u, v, cost))
            total_cost += cost

            for neighbor, neighbor_cost in graph_data[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (neighbor_cost, v, neighbor))

    return mst, total_cost


mst, total = prim(graph, "GedungA")

print("Jaringan kabel minimum:")
for u, v, cost in mst:
    print(f"{u} - {v} = {cost}")

print("Total biaya minimum =", total)

# Jawaban Analisis:
# 1. Algoritma yang digunakan adalah Prim.
#    Saya memilih Prim karena kasusnya mudah dibayangkan dari satu gedung awal.
#    Jaringan kabelnya dibuat pelan-pelan: mulai dari GedungA, lalu cari kabel
#    paling murah yang bisa menyambungkan gedung lain ke jaringan yang sudah ada.
# 2. Edge yang dipilih adalah GedungA-GedungC, GedungC-GedungD, dan
#    GedungD-GedungB.
# 3. Total biaya minimum adalah 6.
# 4. MST cocok karena kampus hanya butuh semua gedung saling terhubung, bukan
#    semua kemungkinan kabel dipasang. Jadi biaya bisa ditekan dan sambungan
#    yang berlebihan tidak perlu dibuat.
