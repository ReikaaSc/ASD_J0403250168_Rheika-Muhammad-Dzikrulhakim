# Nama  : Rheika Muhammad Dzikrulhakim
# NIM   : J0403251068
# Kelas : TPL A1
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Latihan 5 - Kasus 2: Jaringan Komputer
# ==========================================================

# Data hubungan router disimpan sebagai edge berbobot.
# Format: (bobot, router1, router2)
edges = [
    (3, "RouterA", "RouterB"),
    (2, "RouterA", "RouterC"),
    (5, "RouterB", "RouterD"),
    (1, "RouterC", "RouterD"),
    (4, "RouterB", "RouterC"),
]


def find(parent, node):
    """Mencari akar kelompok dari sebuah router."""
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]


def union(parent, rank, node1, node2):
    """Menggabungkan dua kelompok router jika belum tersambung."""
    root1 = find(parent, node1)
    root2 = find(parent, node2)

    if root1 == root2:
        return False

    if rank[root1] < rank[root2]:
        parent[root1] = root2
    elif rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root2] = root1
        rank[root1] += 1

    return True


def kruskal(edge_list):
    """Menentukan MST jaringan komputer menggunakan algoritma Kruskal."""
    routers = set()
    for _, u, v in edge_list:
        routers.add(u)
        routers.add(v)

    parent = {router: router for router in routers}
    rank = {router: 0 for router in routers}
    mst = []
    total_weight = 0

    for weight, u, v in sorted(edge_list):
        if union(parent, rank, u, v):
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight


mst, total = kruskal(edges)

print("Minimum Spanning Tree jaringan komputer:")
for u, v, weight in mst:
    print(f"{u} - {v} = {weight}")

print("Total bobot minimum =", total)

# Jawaban Analisis:
# 1. Kasus yang dipilih adalah Kasus 2, yaitu jaringan komputer antar router.
# 2. Algoritma yang digunakan adalah Kruskal.
# 3. Edge yang dipilih dalam MST adalah RouterC-RouterD, RouterA-RouterC, dan
#    RouterA-RouterB.
# 4. Total bobot MST adalah 6.
# 5. RouterB-RouterC tidak diambil karena RouterB dan RouterC sudah bisa
#    terhubung lewat RouterA. RouterB-RouterD juga tidak dipakai karena RouterD
#    sudah tersambung lebih murah lewat RouterC. Kalau dua edge itu ditambahkan,
#    jaringan memang tetap jalan, tetapi bobotnya jadi lebih besar dan ada jalur
#    yang berputar.
