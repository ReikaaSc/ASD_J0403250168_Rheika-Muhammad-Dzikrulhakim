# ==================================================================
# Praktikum 6 - Merge Sort
# ascending order
# ==================================================================

def mergeSort(data): # fungsi untuk mengurutkan data dengan metode merge sort
    print("Splitting ",data) # menampilkan data yang akan diurutkan sebelum proses splitting dimulai
    if len(data)>1: # jika panjang data lebih dari 1, maka data akan dibagi menjadi dua bagian
        mid = len(data)//2 # mencari titik tengah data
        lefthalf = data[:mid] # bagian kiri data
        righthalf = data[mid:] # bagian kanan data
        
        mergeSort(lefthalf) # rekursif untuk mengurutkan bagian kiri data
        mergeSort(righthalf) # rekursif untuk mengurutkan bagian kanan data
        i=0 # inisialisasi indeks untuk bagian kiri data
        j=0 # inisialisasi indeks untuk bagian kanan data
        k=0 # inisialisasi indeks untuk data yang sudah diurutkan
        while i < len(lefthalf) and j < len(righthalf): # selama indeks bagian kiri data dan indeks bagian kanan data masih dalam batas panjang data
            if lefthalf[i] < righthalf[j]:  # jika elemen bagian kiri data lebih kecil dari elemen bagian kanan data, maka elemen bagian kiri data akan dimasukkan ke dalam data yang sudah diurutkan
                data[k]=lefthalf[i] # memasukkan elemen bagian kiri data ke dalam data yang sudah diurutkan
                i=i+1 # menambahkan indeks bagian kiri data
            else: # jika elemen bagian kanan data lebih kecil dari elemen bagian kiri data, maka elemen bagian kanan data akan dimasukkan ke dalam data yang sudah diurutkan
                data[k]=righthalf[j] # memasukkan elemen bagian kanan data ke dalam data yang sudah diurutkan
                j=j+1 # menambahkan indeks bagian kanan data
            k=k+1 # menambahkan indeks untuk data yang sudah diurutkan
            
        while i < len(lefthalf): # jika masih ada elemen bagian kiri
            data[k]=lefthalf[i] # memasukkan elemen bagian kiri data ke dalam data yang sudah diurutkan
            i=i+1 # menambahkan indeks bagian kiri data
            k=k+1 # menambahkan indeks untuk data yang sudah diurutkan
            
        while j < len(righthalf): # jika masih ada elemen bagian kanan
            data[k]=righthalf[j] # memasukkan elemen bagian kanan data ke dalam data yang sudah diurutkan
            j=j+1 # menambahkan indeks bagian kanan data
            k=k+1 # menambahkan indeks untuk data yang sudah diurutkan
            
        print("Merging ",data) # menampilkan data yang sudah diurutkan setelah proses merging selesai
        
data = [54,26,93,17,77,31,44,55,20] # data yang akan diurutkan
mergeSort(data) # memanggil fungsi mergeSort untuk mengurutkan data
print(data) # menampilkan data yang sudah diurutkan setelah proses merge sort selesai
