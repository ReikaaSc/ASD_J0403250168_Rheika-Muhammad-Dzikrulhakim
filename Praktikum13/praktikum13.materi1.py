# Nama  : Rheika Muhammad Dzikrulhakim
# NIM   : J0403251068
# Kelas : TPL A1
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Materi 1 - Implementasi Kruskal
# ==========================================================

# Daftar edge disimpan dalam bentuk (bobot, node1, node2).
# Urutan bobot diletakkan di depan supaya mudah diurutkan.
edges = [
    (1, "C", "D"),
    (2, "A", "C"),
    (3, "B", "D"),
    (4, "A", "B"),
    (5, "A", "D"),
]


def find(parent, node):
    """Mencari akar dari sebuah node pada struktur disjoint set."""
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]


def union(parent, rank, node1, node2):
    """Menggabungkan dua kelompok node jika belum berada dalam kelompok yang sama."""
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
    """Membentuk MST dengan memilih edge terkecil yang tidak membuat cycle."""
    nodes = set()
    for _, u, v in edge_list:
        nodes.add(u)
        nodes.add(v)

    parent = {node: node for node in nodes}
    rank = {node: 0 for node in nodes}
    mst = []
    total_weight = 0

    # Kruskal selalu memproses edge dari bobot terkecil.
    for weight, u, v in sorted(edge_list):
        if union(parent, rank, u, v):
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight


mst, total = kruskal(edges)

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total)

# Catatan:
# Dari hasil program, Kruskal memilih edge yang paling murah dulu. Setelah itu
# edge dicek lagi, apakah masih aman atau malah membuat jalur berputar. Pada
# contoh ini edge yang masuk MST adalah C-D, A-C, dan B-D, total bobotnya 6.
