# Nama  : Rheika Muhammad Dzikrulhakim
# NIM   : J0403251068
# Kelas : TPL A1
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Latihan 1 - Memahami Konsep Spanning Tree
# ==========================================================

# Daftar edge pada graph awal.
edges = [
    ("A", "B"),
    ("A", "C"),
    ("A", "D"),
    ("C", "D"),
    ("B", "D"),
]

# Salah satu contoh spanning tree yang valid.
# Semua node tetap terhubung, tetapi tidak ada cycle.
spanning_tree = [
    ("A", "C"),
    ("C", "D"),
    ("D", "B"),
]

print("Edge pada graph:")
for edge in edges:
    print(edge)

print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# Jawaban Analisis:
# 1. Graph awal masih berisi semua sambungan yang mungkin dipakai, jadi edge-nya
#    lebih banyak. Spanning tree hanya mengambil sambungan yang penting saja,
#    asal semua node tetap bisa terhubung.
# 2. Cycle tidak dipakai karena kalau sudah ada jalur yang memutar, berarti ada
#    edge yang sebenarnya tidak terlalu diperlukan. Kalau ini dianggap seperti
#    kabel, kabel tambahan itu hanya menambah biaya.
# 3. Edge pada spanning tree lebih sedikit karena untuk 4 node cukup 3 edge.
#    Kalau ditambah lagi, graph biasanya mulai membentuk cycle.
