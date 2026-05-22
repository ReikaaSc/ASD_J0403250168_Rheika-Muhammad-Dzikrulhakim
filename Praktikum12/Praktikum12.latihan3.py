# Nama : Rheika Muhammad Dzikrulhakim
# NIM : J0403251068
# Kelas : TPL A1
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak dari start ke start adalah 0
    distances[start] = 0
    
    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):
        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():
                # Jika jarak ke node saat ini sudah diketahui,
                # dan ditemukan jarak yang lebih kecil ke neighbor,
                # maka lakukan update jarak
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
    
    return distances

hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Berapa bobot langsung dari A ke B?
#    Bobot langsung dari A ke B = 5 (edge A -> B memiliki bobot 5)

# 2. Berapa total bobot jalur A -> C -> B?
#    Total bobot jalur A -> C -> B = 4 + (-2) = 2
#    (A -> C dengan bobot 4, C -> B dengan bobot -2)

# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
#    Jalur A -> C -> B menghasilkan jarak lebih kecil (2) dibanding jalur langsung
#    A -> B (5). Ini karena edge C -> B memiliki bobot negatif (-2), sehingga
#    mengurangi total jarak keseluruhan.

# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
#    Bellman-Ford dapat digunakan pada graph dengan bobot negatif karena algoritma ini
#    tidak menggunakan pendekatan greedy. Sebaliknya, Bellman-Ford melakukan relaksasi
#    edge berkali-kali (sebanyak jumlah node - 1 kali) untuk memastikan setiap node
#    mendapatkan jarak minimum yang benar. Dengan cara ini, edge negatif tidak akan
#    menghasilkan hasil yang salah seperti pada Dijkstra, karena algoritma terus
#    memperbarui jarak jika menemukan jalur yang lebih pendek.

# 5. Apa yang dimaksud dengan proses relaksasi edge?
#    Relaksasi edge adalah proses memperbarui jarak ke node tetangga jika ditemukan
#    jalur alternatif yang lebih pendek. Pada setiap iterasi, Bellman-Ford memeriksa
#    setiap edge dan melihat apakah jarak ke node tujuan dapat diperbaiki dengan
#    menambahkan bobot edge tersebut ke jarak node sumber. Jika ya, maka jarak
#    diperbarui. Proses ini diulang sampai tidak ada lagi pembaruan (jarak sudah optimal).

# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
#    Perbedaan utama:
#    a) Bobot negatif: Dijkstra tidak bisa, Bellman-Ford bisa
#    b) Kecepatan: Dijkstra lebih cepat O(E log V), Bellman-Ford lebih lambat O(VE)
#    c) Pendekatan: Dijkstra greedy (memilih node terkecil), Bellman-Ford relaksasi
#       (memperbarui semua edge berulang-ulang)
#    d) Struktur data: Dijkstra pakai priority queue, Bellman-Ford tidak perlu
#    
#    Pilihan algoritma tergantung pada karakteristik graph:
#    - Gunakan Dijkstra jika semua bobot positif (lebih cepat)
#    - Gunakan Bellman-Ford jika ada bobot negatif atau perlu deteksi negative cycle
