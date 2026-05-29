# Nama  : Rheika Muhammad Dzikrulhakim
# NIM   : J0403251068
# Kelas : TPL A1
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Materi 2 - Implementasi Prim
# ==========================================================

import heapq

# Graph berbobot disimpan sebagai dictionary bertingkat.
# Setiap node menyimpan tetangga beserta bobot edge-nya.
graph = {
    "A": {"B": 4, "C": 2, "D": 5},
    "B": {"A": 4, "D": 3},
    "C": {"A": 2, "D": 1},
    "D": {"A": 5, "B": 3, "C": 1},
}


def prim(graph_data, start):
    """Membentuk MST dengan memperluas tree dari satu node awal."""
    visited = {start}
    candidate_edges = []

    # Semua edge dari node awal dimasukkan sebagai kandidat pertama.
    for neighbor, weight in graph_data[start].items():
        heapq.heappush(candidate_edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    while candidate_edges and len(visited) < len(graph_data):
        weight, u, v = heapq.heappop(candidate_edges)

        # Edge dipakai hanya jika menghubungkan node baru.
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight

            for neighbor, neighbor_weight in graph_data[v].items():
                if neighbor not in visited:
                    heapq.heappush(candidate_edges, (neighbor_weight, v, neighbor))

    return mst, total_weight


mst, total = prim(graph, "A")

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total)

# Catatan:
# Pada program ini Prim dimulai dari node A. Tiap langkahnya mengambil edge
# termurah yang bisa menyambungkan node baru ke tree yang sedang dibentuk.
# Hasil akhirnya tetap C-D, A-C, dan D-B dengan total bobot 6.
