# Nama : Rheika Muhammad Dzikrulhakim
# NIM : J0403251068
# Kelas : TPL A1
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 2: Implementasi Dijkstra
# ==========================================================

import heapq

# Weighted graph dengan bobot positif
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak dari start ke start adalah 0
    distances[start] = 0
    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat,
        # maka proses dilewati
        if current_distance > distances[current_node]:
            continue
        
        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

hasil = dijkstra(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Berapa jarak terpendek dari A ke B?
#    Jarak terpendek dari A ke B = 4 (jalur langsung A -> B dengan bobot 4)

# 2. Berapa jarak terpendek dari A ke C?
#    Jarak terpendek dari A ke C = 2 (jalur langsung A -> C dengan bobot 2)

# 3. Berapa jarak terpendek dari A ke D?
#    Jarak terpendek dari A ke D = 3 (melalui jalur A -> C -> D = 2 + 1 = 3)

# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
#    Karena melalui C: A -> C -> D = 2 + 1 = 3
#    Sedangkan melalui B: A -> B -> D = 4 + 5 = 9
#    Jadi 3 < 9, sehingga rute melalui C adalah rute terpendek.

# 5. Apa fungsi priority_queue dalam algoritma Dijkstra?
#    Priority queue (min-heap) digunakan untuk selalu mengambil/memilih node dengan 
#    jarak sementara paling kecil untuk diproses berikutnya. Ini memastikan bahwa
#    Dijkstra menggunakan pendekatan greedy yang optimal: selalu memilih node dengan
#    jarak terkecil untuk eksplorasi berikutnya, sehingga menghindari pengujian node
#    yang tidak optimal terlebih dahulu.

# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?
#    Dijkstra tidak cocok untuk graph dengan bobot negatif karena menggunakan 
#    pendekatan greedy dengan asumsi bahwa jarak terpendek yang sudah dipilih tidak 
#    akan berubah lagi. Jika ada edge dengan bobot negatif, mungkin ada jalur alternatif
#    yang memberikan jarak lebih kecil, tetapi Dijkstra sudah "mengunci" keputusan 
#    sebelumnya dan tidak akan memeriksa kembali. Hasilnya adalah shortest path yang 
#    tidak akurat. Untuk mengatasi ini, gunakan algoritma Bellman-Ford yang dapat 
#    menangani bobot negatif.
