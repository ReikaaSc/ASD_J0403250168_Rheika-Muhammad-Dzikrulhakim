# Nama : Rheika Muhammad Dzikrulhakim
# NIM : J0403251068
# Kelas : TPL A1
# Praktikum 12 - Graph II: Shortest Path (Dijkstra & Bellman-Ford)

# Weighted graph dengan bobot positif (juga bisa handle bobot negatif)
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start ke seluruh node lain
    menggunakan algoritma Bellman-Ford.
    
    Algoritma Bellman-Ford dapat menangani graph dengan bobot negatif,
    berbeda dengan Dijkstra yang hanya cocok untuk bobot positif.
    
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
    
    # Relaksasi edge sebanyak jumlah node - 1 kali
    # Ini untuk memastikan setiap node memperoleh jarak minimum yang benar
    for _ in range(len(graph) - 1):
        # Periksa setiap node dalam graph
        for node in graph:
            # Periksa setiap edge/tetangga dari node saat ini
            for neighbor, weight in graph[node].items():
                # Jika jarak ke node saat ini sudah diketahui (bukan infinity),
                # dan ditemukan jarak yang lebih kecil ke neighbor,
                # maka lakukan update jarak (relaksasi)
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
    
    # Return dictionary berisi jarak terpendek dari start ke setiap node
    return distances

# Jalankan algoritma Bellman-Ford dari node 'A'
hasil = bellman_ford(graph, 'A')

# Tampilkan hasil
print("Jarak terpendek dari node A ke semua node (Bellman-Ford):")
for node, distance in hasil.items():
    print(f"{node} = {distance}")

# Output yang diharapkan: {'A': 0, 'B': 4, 'C': 2, 'D': 3}
