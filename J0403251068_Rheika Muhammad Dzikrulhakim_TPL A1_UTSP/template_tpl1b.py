# ==============================================================================
# UJIAN TENGAH PRAKTIKUM - ALGORITMA & STRUKTUR DATA (TPL2106)
# Nama    : Rheika Muhammad Dzikrulhakim
# NIM     : J0403251068
# Kelas   : TPL A/P1
# ==============================================================================


# 1. FILE HANDLING & DICTIONARY
def muat_data_buku(nama_file):
    """
    Fungsi untuk membaca file buku.txt kemudian
    menyimpannya ke dalam struktur data Dictionary.

    Format file:
    kode_buku,judul,harga
1
    """
    database_buku = {}

    try: # nyoba nyari file nya dulu
        with open(nama_file, "r") as file:
            for baris in file:
                # Menghapus newline dan memisahkan data berdasarkan koma
                kode, judul, harga = baris.strip().split(",")

                # Menyimpan ke dictionary
                database_buku[kode] = {
                    "judul": judul,
                    "harga": int(harga)
                }

    except FileNotFoundError: # kalo filenya ga ketemu bakal muncul ini
        print("File buku.txt tidak ditemukan.")

    return database_buku


# 2. LINKED LIST - MANAJEMEN PROMOSI
class Node:
    """
    Node pada Single Linked List.
    Setiap node menyimpan judul buku dan pointer ke node berikutnya.
    """
    def __init__(self, judul):
        self.judul = judul
        self.next = None


class LinkedListPromosi:
    """
    Implementasi Single Linked List untuk menyimpan
    daftar buku yang sedang dipromosikan.
    """
    def __init__(self):
        self.head = None

    def tambah_buku_promosi(self, judul):
        """
        Menambahkan buku baru ke akhir linked list.
        """
        node_baru = Node(judul)

        # Jika list masih kosong
        if self.head is None:
            self.head = node_baru
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node_baru

    def tampilkan_promosi(self):
        """
        Menampilkan semua judul buku dalam daftar promosi.
        """
        if self.head is None: # ngecek ada node atau enggak
            print("Belum ada buku promosi.")
            return

        current = self.head
        print("Daftar Buku Promosi:")
        while current:
            print("-", current.judul)
            current = current.next


# 3. QUEUE - ANTREAN KASIR
class AntreanKasir:
    """
    Implementasi Queue menggunakan list Python.
    Prinsip FIFO (First In First Out).
    """
    def __init__(self):
        self.antrean = []

    def tambah_antrean(self, nama_pelanggan): # Nambah anttrian
        """
        Menambahkan pelanggan ke antrean (enqueue).
        """
        self.antrean.append(nama_pelanggan) 
        print(nama_pelanggan, "masuk ke antrean.")

    def layani_pelanggan(self):
        """
        Melayani pelanggan pertama dalam antrean (dequeue).
        """
        if len(self.antrean) == 0: # Mengecek antrianye kosong apa enggak
            print("Antrean kosong.")
        else:
            pelanggan = self.antrean.pop(0) # kalo ada dilayani
            print("Melayani pelanggan:", pelanggan)


# 4. SORTING - LAPORAN TRANSAKSI
def urutkan_transaksi(list_harga):
    """
    Mengurutkan list harga menggunakan algoritma
    Insertion Sort dari yang terkecil ke terbesar.
    """
    for i in range(1, len(list_harga)):
        key = list_harga[i]
        j = i - 1

        # Memindahkan elemen yang lebih besar ke kanan
        while j >= 0 and list_harga[j] > key:
            list_harga[j + 1] = list_harga[j]
            j -= 1

        list_harga[j + 1] = key

    return list_harga


# ==============================================================================
# MAIN PROGRAM - MENU ANTARMUKA
# ==============================================================================
def main():

    # Inisialisasi data
    file_db = "J0403251068_Rheika Muhammad Dzikrulhakim_TPL A1_UTSP/buku.txt"
    data_buku = muat_data_buku(file_db)
    list_promosi = LinkedListPromosi()
    antrean_toko = AntreanKasir()
    riwayat_transaksi = [150000, 50000, 200000, 75000, 120000]

    while True:
        print("\n--- SISTEM MANAJEMEN TOKO BUKU ---")
        print("1. Lihat Katalog Buku (Dictionary/File)")
        print("2. Kelola Daftar Promosi (Linked List)")
        print("3. Kelola Antrean Kasir (Queue)")
        print("4. Lihat Laporan Penjualan Terurut (Sorting)")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            print("\nKatalog Buku:")
            for kode, info in data_buku.items():
                print(kode, "-", info["judul"], "- Rp", info["harga"])

        elif pilihan == '2':
            judul_baru = input("Masukkan judul buku untuk promosi: ")
            list_promosi.tambah_buku_promosi(judul_baru)
            list_promosi.tampilkan_promosi()

        elif pilihan == '3':
            print("\n1. Tambah Antrean")
            print("2. Layani Pelanggan")
            sub = input("Pilih: ")

            if sub == '1':
                nama = input("Nama Pelanggan: ")
                antrean_toko.tambah_antrean(nama)
            elif sub == '2':
                antrean_toko.layani_pelanggan()

        elif pilihan == '4':
            print("Harga Sebelum Urut:", riwayat_transaksi)
            hasil_sort = urutkan_transaksi(riwayat_transaksi.copy())
            print("Harga Sesudah Urut:", hasil_sort)

        elif pilihan == '5':
            print("Program selesai. Terima kasih.")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()