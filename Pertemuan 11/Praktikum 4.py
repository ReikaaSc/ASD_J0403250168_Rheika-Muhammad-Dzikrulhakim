# ============================================================
# PRAKTIKUM 4 - Studi Kasus Dunia Nyata
# Studi Kasus  : Peta Kota
# Nama         : Rheika Muhammad Dzikrulhakim
# NIM          : J0403251068
# ============================================================

kota = ["TUBAN", "SURABAYA", "MADIUN", "KEDIRI", "MALANG", "PROBOLINGGO", "LUMAJANG"]

# (kota_asal, kota_tujuan, jarak_km)
edges_weighted = [
    ("TUBAN",       "SURABAYA",     106),
    ("SURABAYA",    "MADIUN",       165),
    ("SURABAYA",    "MALANG",       100),
    ("SURABAYA",    "PROBOLINGGO",  109),
    ("MADIUN",      "KEDIRI",        95),
    ("KEDIRI",      "MALANG",       105),
    ("MALANG",      "LUMAJANG",     156),
    ("PROBOLINGGO", "LUMAJANG",      47),
]

V = len(kota)
index = {nama: i for i, nama in enumerate(kota)}  # mapping nama -> indeks

# ============================================================
# BAGIAN 1: ADJACENCY LIST (menggunakan dictionary)
# ============================================================

def buatAdjacencyList(kota, edges):
    graph = {k: [] for k in kota}
    for u, v, w in edges:
        graph[u].append((v, w))   # simpan (tetangga, bobot)
        graph[v].append((u, w))   # undirected: dua arah
    return graph

# ============================================================
# BAGIAN 2: ADJACENCY MATRIX (menggunakan 2D list)
# ============================================================

def buatAdjacencyMatrix(V, index, edges):
    # Inisialisasi semua 0 (tidak ada koneksi)
    mat = [[0] * V for _ in range(V)]
    for u, v, w in edges:
        i, j = index[u], index[v]
        mat[i][j] = w   # simpan bobot jarak
        mat[j][i] = w   # undirected: simetris
    return mat

# ============================================================
# MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    adj  = buatAdjacencyList(kota, edges_weighted)
    mat  = buatAdjacencyMatrix(V, index, edges_weighted)

    # ----------------------------------------------------------
    # OUTPUT 1: Informasi node dan edge
    # ----------------------------------------------------------
    print("=" * 60)
    print("  PRAKTIKUM 4 - STUDI KASUS PETA KOTA (JAWA TIMUR)")
    print("=" * 60)

    print("\n[ NODE / VERTEX ]")
    for i, nama in enumerate(kota):
        print(f"  Node {i}: {nama}")

    print(f"\nTotal node  : {V}")
    print(f"Total edge  : {len(edges_weighted)}")

    print("\n[ DAFTAR EDGE (Jalan + Jarak) ]")
    print("-" * 40)
    for i, (u, v, w) in enumerate(edges_weighted, 1):
        print(f"  {i}. {u:15s} <---> {v:15s} : {w} km")

    # ----------------------------------------------------------
    # OUTPUT 2: Adjacency List
    # ----------------------------------------------------------
    print("\n" + "=" * 60)
    print("  ADJACENCY LIST")
    print("=" * 60)
    for kota_nama in kota:
        tetangga = ", ".join(
            f"{t} ({w} km)" for t, w in adj[kota_nama]
        )
        print(f"  {kota_nama:15s} -> {tetangga}")

    # ----------------------------------------------------------
    # OUTPUT 3: Adjacency Matrix
    # ----------------------------------------------------------
    print("\n" + "=" * 60)
    print("  ADJACENCY MATRIX (bobot = jarak km, 0 = tidak terhubung)")
    print("=" * 60)

    # Header kolom (singkatan 3 huruf agar rapi)
    singkat = [n[:4] for n in kota]
    header_width = 6
    print(" " * 16, end="")
    for s in singkat:
        print(f"{s:^{header_width}}", end="")
    print()

    # Isi matriks
    for i in range(V):
        print(f"  {kota[i]:13s} ", end="")
        for j in range(V):
            val = mat[i][j]
            if val == 0:
                print(f"{'0':^{header_width}}", end="")
            else:
                print(f"{val:^{header_width}}", end="")
        print()