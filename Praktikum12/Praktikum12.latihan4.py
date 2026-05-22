# Nama : Rheika Muhammad Dzikrulhakim
# NIM : J0403251068
# Kelas : TPL A1
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================

import heapq

# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):
    """Fungsi untuk mencari jarak terpendek menggunakan algoritma Dijkstra"""
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

hasil = dijkstra(graph, 'Gerbang')

print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")

# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Lokasi mana yang paling dekat dari Gerbang?
#    Lokasi yang paling dekat dari Gerbang adalah Kantin dengan waktu tempuh 2 menit
#    (jalur langsung Gerbang -> Kantin).

# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
#    Waktu tempuh terpendek dari Gerbang ke Aula = 7 menit
#    Jalur: Gerbang -> Kantin -> Lab -> Aula = 2 + 4 + 1 = 7 menit
#    (Jalur alternatif melalui Perpustakaan akan lebih lama:
#     Gerbang -> Perpustakaan -> Lab -> Aula = 6 + 3 + 1 = 10 menit)

# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
#    Tidak, jalur langsung tidak selalu menghasilkan jarak paling kecil. Contohnya:
#    - Jalur langsung Gerbang -> Aula tidak ada (tidak terhubung langsung)
#    - Jalur Gerbang -> Kantin -> Lab = 2 + 4 = 6 menit
#    - Jalur Gerbang -> Perpustakaan -> Lab = 6 + 3 = 9 menit
#    Rute tidak langsung (Gerbang -> Kantin -> Lab) menghasilkan jarak lebih kecil
#    dibanding rute melalui Perpustakaan. Ini menunjukkan bahwa pada weighted graph,
#    perlu mempertimbangkan semua kemungkinan rute, bukan hanya rute langsung.

# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
#    Dijkstra cocok digunakan pada kasus lokasi kampus karena:
#    a) Semua bobot (waktu tempuh) bernilai positif - tidak ada waktu tempuh negatif
#    b) Graph relatif kecil - hanya 5 lokasi
#    c) Dijkstra lebih cepat dan efisien untuk bobot positif (O(E log V))
#    d) Tidak perlu mendeteksi negative cycle atau edge negatif
#    e) Kebutuhan real-time: Dijkstra lebih cepat daripada Bellman-Ford untuk
#       menemukan rute terpendek, sehingga cocok untuk aplikasi navigasi kampus.
