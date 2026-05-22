# Nama : Rheika Muhammad Dzikrulhakim
# NIM : J0403251068
# Kelas : TPL A1
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# ==========================================================

# Representasi weighted graph menggunakan dictionary bersarang
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D']  # A -> B -> D
jalur_2 = graph['A']['C'] + graph['C']['D']  # A -> C -> D

print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")

# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Berapa total bobot jalur A -> B -> D?
#    Total bobot jalur A -> B -> D = 9 (bobot edge A->B adalah 4, B->D adalah 5, jadi 4 + 5 = 9)

# 2. Berapa total bobot jalur A -> C -> D?
#    Total bobot jalur A -> C -> D = 3 (bobot edge A->C adalah 2, C->D adalah 1, jadi 2 + 1 = 3)

# 3. Jalur mana yang dipilih sebagai jalur terpendek?
#    Jalur terpendek adalah A -> C -> D karena memiliki total bobot 3, yang lebih kecil 
#    dibandingkan jalur A -> B -> D dengan bobot 9.

# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?
#    Karena pada weighted graph, fokus utama adalah total bobot (biaya) keseluruhan jalur,
#    bukan banyaknya edge/langkah yang dilalui. Sebuah jalur dengan lebih banyak edge
#    tetap bisa menjadi jalur terpendek jika total bobotnya lebih kecil. Misalnya,
#    jalur dengan 3 edge dan total bobot 4 akan lebih dipilih dibanding jalur dengan 2 edge
#    tetapi total bobot 9, karena algoritma shortest path fokus pada biaya minimum,
#    bukan jumlah langkah perjalanan.
