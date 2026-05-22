# Nama : Rheika Muhammad Dzikrulhakim
# NIM : J0403251068
# Kelas : TPL A1
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 5: Studi Kasus dengan Program Shortest Path
# Mencari jalur terpendek antar kota menggunakan Dijkstra
# ==========================================================

import heapq

# Graph representasi jalur antar kota dengan bobot jarak
# Bogor -> Jakarta = 5
# Bogor -> Depok = 2
# Depok -> Jakarta = 2
# Jakarta -> Bandung = 7
# Depok -> Bandung = 6

graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start ke seluruh node lain
    menggunakan algoritma Dijkstra.
    
    Parameter:
    - graph: dictionary merepresentasikan weighted graph antar kota
    - start: kota awal untuk mencari shortest path
    
    Return:
    - distances: dictionary jarak terpendek dari start ke setiap kota
    """
    # Inisialisasi semua jarak ke infinity
    distances = {node: float('inf') for node in graph}
    
    # Jarak ke kota awal adalah 0
    distances[start] = 0
    
    # Priority queue untuk menyimpan (jarak, kota)
    # Heap akan selalu mengambil elemen dengan jarak terkecil
    priority_queue = [(0, start)]
    
    # Proses sampai priority queue kosong
    while priority_queue:
        # Ambil kota dengan jarak terkecil
        current_distance, current_city = heapq.heappop(priority_queue)
        
        # Skip jika jarak saat ini lebih besar dari jarak yang tercatat
        if current_distance > distances[current_city]:
            continue
        
        # Periksa semua kota tetangga yang terhubung
        for neighbor, weight in graph[current_city].items():
            # Hitung jarak baru melalui current_city
            new_distance = current_distance + weight
            
            # Jika ditemukan jalur lebih pendek, perbarui dan tambah ke queue
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))
    
    return distances

# Jalankan algoritma dari Bogor
start_city = 'Bogor'
hasil = dijkstra(graph, start_city)

# Tampilkan hasil
print(f"Jarak terpendek dari {start_city}:")
for city, distance in hasil.items():
    if distance == float('inf'):
        print(f"{start_city} -> {city} = Tidak terhubung")
    else:
        print(f"{start_city} -> {city} = {distance}")

# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Node awal yang digunakan apa?
#    Node awal yang digunakan adalah Bogor. Dari sini kita mencari jarak terpendek
#    ke seluruh kota lainnya (Depok, Jakarta, dan Bandung).

# 2. Node mana yang memiliki jarak paling kecil dari node awal?
#    Node Depok memiliki jarak paling kecil dari Bogor yaitu 2 km.
#    Ini adalah rute langsung Bogor -> Depok dengan bobot 2.

# 3. Node mana yang memiliki jarak paling besar dari node awal?
#    Node Bandung memiliki jarak paling besar dari Bogor yaitu 8 km.
#    Rute terpendeknya adalah Bogor -> Depok -> Bandung = 2 + 6 = 8 km
#    (lebih pendek dibanding Bogor -> Jakarta -> Bandung = 5 + 7 = 12 km)

# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
#    Langkah kerja Dijkstra pada kasus ini:
#    
#    Iterasi 1: Mulai dari Bogor (jarak = 0)
#    - Update jarak Depok = 0 + 2 = 2
#    - Update jarak Jakarta = 0 + 5 = 5
#    
#    Iterasi 2: Pilih Depok (jarak terkecil = 2)
#    - Update jarak Jakarta = min(5, 2 + 2) = 4 (jalur Bogor -> Depok -> Jakarta)
#    - Update jarak Bandung = 2 + 6 = 8
#    
#    Iterasi 3: Pilih Jakarta (jarak = 4)
#    - Update jarak Bandung = min(8, 4 + 7) = 8 (tetap 8)
#    
#    Iterasi 4: Pilih Bandung (jarak = 8)
#    - Tidak ada tetangga lagi, selesai
#    
#    Hasil akhir:
#    - Bogor = 0
#    - Depok = 2 (jalur: Bogor -> Depok)
#    - Jakarta = 4 (jalur: Bogor -> Depok -> Jakarta)
#    - Bandung = 8 (jalur: Bogor -> Depok -> Bandung)
#    
#    Algoritma Dijkstra bekerja dengan prinsip greedy: selalu memilih node dengan
#    jarak terkecil yang belum diproses, kemudian melakukan relaksasi (update) pada
#    semua tetangganya. Proses ini diulang sampai semua node terproses, memastikan
#    hasil akhir adalah jarak terpendek yang optimal.
