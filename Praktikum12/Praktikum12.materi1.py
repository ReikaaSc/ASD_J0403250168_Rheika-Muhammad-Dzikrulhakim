# Nama : Rheika Muhammad Dzikrulhakim
# NIM : J0403251068
# Kelas : TPL A1
# Praktikum 12 - Graph II: Shortest Path (Dijkstra & Bellman-Ford)

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
    Fungsi untuk mencari jarak terpendek dari node start ke seluruh node lain
    menggunakan algoritma Dijkstra dengan priority queue (heap).
    
    Parameter:
    - graph: dictionary yang merepresentasikan weighted graph
    - start: node awal untuk mencari shortest path
    
    Return:
    - distances: dictionary yang berisi jarak terpendek dari start ke setiap node
    """
    
    # Menyimpan jarak minimum dari start ke setiap node
    # Awalnya semua node memiliki jarak tak hingga (infinity)
    distances = {node: float('inf') for node in graph}
    
    # Jarak dari node awal ke dirinya sendiri adalah 0
    distances[start] = 0
    
    # Priority queue (min-heap) menyimpan tuple (jarak, node)
    # Digunakan untuk selalu memilih node dengan jarak terkecil
    pq = [(0, start)]
    
    # Proses hingga priority queue kosong
    while pq:
        # Ambil node dengan jarak terkecil dari priority queue
        current_distance, current_node = heapq.heappop(pq)
        
        # Periksa semua tetangga (neighbor) dari node saat ini
        for neighbor, weight in graph[current_node].items():
            # Hitung jarak baru ke tetangga melalui current_node
            distance = current_distance + weight
            
            # Jika ditemukan jalur yang lebih pendek ke neighbor,
            # perbarui jaraknya dan tambahkan ke priority queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    # Return dictionary berisi jarak terpendek dari start ke setiap node
    return distances

# Jalankan algoritma Dijkstra dari node 'A'
hasil = dijkstra(graph, 'A')

# Tampilkan hasil
print("Jarak terpendek dari node A ke semua node:")
for node, distance in hasil.items():
    print(f"{node} = {distance}")

# Output yang diharapkan: {'A': 0, 'B': 4, 'C': 2, 'D': 3}
