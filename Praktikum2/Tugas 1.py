# ===============================================================
# Tugas Hands-on Modul 1
# Studi kasus sistem stok barang kantin (berbasis file .txt)
# Nama : Rheika Muhammad Dzikrulhakim
# NIM  : J0403251068
# Kelas: A/P1
# ===============================================================

# Tugas 1 
# Algoritma dan Struktur Data
nama_file = "Praktikum2/stok_barang.txt"

# -----------------------------------------------------------
# Fungsi Membaca data dari File
# -----------------------------------------------------------

def baca_stok(nama_file):
    stok_dict = {}
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file :
            baris = baris.strip()#mengambil data dan menghilangka new line
            kodebarang, nama, stok = baris.split(",") # ambil data per item data
            stok_dict[kodebarang] = {"nama": nama, "stok": int(stok)}

    return stok_dict

# -----------------------------------------------------------
# Fungsi Menampilkan semua data 
# -----------------------------------------------------------

def tampil_stok(stok_dict):
    #membuat header tabel
    print("\n========= DAFTAR BARANG =========")
    print(f"{'Kode barang' : <10} | {'Nama' : <12} | {'Nilai' :>5}")
    print("-"*36)# membuat garis
    
    #menampikan isi datanya
    for kodebarang in sorted(stok_dict.keys()):
        nama = stok_dict[kodebarang]["nama"]
        stok = stok_dict[kodebarang]["stok"]
        print(f"{kodebarang:<10} | {nama:<12} | {int(stok):>5}")
            
# -----------------------------------------------------------
# Fungsi Menyimpan data ke file 
# -----------------------------------------------------------

def simpan_stok(nama_file, stok_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for kode_barang in sorted(stok_dict.keys()):
            nama = stok_dict[kode_barang]["nama"]
            stok = stok_dict[kode_barang]["stok"]
            file.write(f"{kode_barang},{nama},{stok}\n")
        
# -----------------------------------------------------------
# Fungsi Cari berdasarkan kode barang
# -----------------------------------------------------------

def cari_barang(stok_dict):
    kode_barang = input("Masukan Kode Barang : ").strip()
    
    if kode_barang in stok_dict:
        nama = stok_dict[kode_barang]["nama"]
        stok = stok_dict[kode_barang]["stok"]
        
        print("===== Data Barang Ditemukan =====")
        print(f'Kode Barang:    {kode_barang}')
        print(f"Nama Barang:    {nama}")
        print(f"Jumlah Stok:    {stok}")
    else:
        print("Kode Barang tidak ditemukan, pastikan kode barang tepat dan terdaftar")
        
# -----------------------------------------------------------
# Fungsi Tambah barang baru
# -----------------------------------------------------------

def tambah_barang(stok_dict):
    kode = input("Masukan Kode Barang baru : ").strip()
    nama = input("Masukan Nama Barang baru : ").strip()
    
    if nama in stok_dict:
        print("Nama barang baru sudah ada")
    elif kode in stok_dict:
        print("Kode sudah ada")
        
    try:
        stok_awal = int(input("Masukkan stok awal: "))
        if stok_awal < 0:
            print("Stok tidak boleh negatif")
            return
    except ValueError:
        print("Stok harus berupa angka")
        return
        
    stok_awal = int(input("Masukan jumlah stok baru: "))
    stok_dict[kode] = {
        "nama": nama,
        "stok": stok_awal
    }

    print("Barang berhasil ditambahkan")
    
# -----------------------------------------------------------
# Fungsi Update stok barang
# -----------------------------------------------------------

def update_barang(stok_dict):
    kode_barang = input("Masukan kode barang yang ingin diupdate: ").strip()

    if kode_barang not in stok_dict:
        print("Kode tidak ada di database")
        return

    print("Pilih Jenis update:")
    print("1. Tambah Stok")
    print("2. Kurangi Stok")

    pilihan = input("Masukan pilihan (1/2) : ").strip()

    try:
        jumlah = int(input("Masukan Jumlah: "))
    except ValueError:
        print("Jumlah harus berupa angka")
        return

    stok_sekarang = stok_dict[kode_barang]["stok"]

    if pilihan == "1":
        stok_dict[kode_barang]["stok"] = stok_sekarang + jumlah
        print("Stok berhasil ditambahkan")
    elif pilihan == "2":
        if jumlah > stok_sekarang:
            print("Stok tidak mencukupi")
        else:
            stok_dict[kode_barang]["stok"] = stok_sekarang - jumlah
            print("Stok berhasil dikurangi")
    else:
        print("Pilihan tidak valid")


# -----------------------------
# Program Utama
# -----------------------------
def main():
    # Membaca data dari file saat program mulai
    stok_barang = baca_stok(nama_file)

    while True:
        print("\n=== MENU ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampil_stok(stok_barang)

        elif pilihan == "2":
            cari_barang(stok_barang)

        elif pilihan == "3":
            tambah_barang(stok_barang)

        elif pilihan == "4":
            update_barang(stok_barang)

        elif pilihan == "5":
            simpan_stok(nama_file, stok_barang)
            print("Data berhasil disimpan")

        elif pilihan == "0":
            print("Terima kasih. Program selesai.")
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi.")
            
# Menjalankan program utama
if __name__ == "__main__":
    main()
