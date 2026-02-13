class Node:
    # Node merepresentasikan satu elemen dalam linked list.
    def __init__(self, data):
        self.data = data  # simpan nilai
        self.next = None  # next -> node selanjutnya
        
class LinkedList:
    # Implementasi singly linked list sederhana.    
    def __init__(self):
        self.head = None  # awal list

    def insert_at_end(self, data):
        # Menambahkan node baru di akhir linked list.
        # Jika list kosong, node baru menjadi head.
        new_node = Node(data)
        if not self.head:
            self.head = new_node  # head = node baru
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node  # sambung di akhir

    def delete_node(self, key):
        # Menghapus node pertama yang memiliki nilai sama dengan key.
        # Kasus yang ditangani:
        # Hapus head jika cocok.
        # Hapus node di tengah/akhir dengan menghubungkan prev.next ke temp.next.
        # Jika tidak ditemukan, beri tahu pengguna.
        temp = self.head

        # kalau head yg mau dihapus
        if temp and temp.data == key:
            self.head = temp.next  # geser head
            print(f"Elemen {key} berhasil dihapus.")
            return

        prev = None  # simpan node sebelumnya
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if not temp:
            print(f"Elemen {key} tidak ditemukan.")
            return

        prev.next = temp.next  # lewati node yang dihapus
        print(f"Elemen {key} berhasil dihapus.")

    def display(self):
        # Menampilkan isi linked list dari head sampai akhir.
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")  # cetak nilai
            temp = temp.next
        print("null")
        
class MergeLinkedList(LinkedList):
    def merge(self, list2):
        # Menggabungkan list2 di akhir list ini (operasi in-place).
        # Jika list ini kosong, head di-set ke head list2.
        # Jika list2 kosong, tidak ada perubahan.
        if not self.head:
            self.head = list2.head
            return

        if not list2.head:
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        # Sambungkan akhir list1 ke awal list2
        temp.next = list2.head  # gabung
        
# Blok eksekusi utama:
# Minta input dua daftar nilai untuk dua linked list,
# Bangun kedua linked list dengan memasukkan nilai di akhir,
# Tampilkan kedua list, gabungkan list2 ke list1, lalu tampilkan hasil gabungan.
list1 = MergeLinkedList()
list2 = MergeLinkedList()

data1 = input("Masukkan elemen untuk Linked List 1 (pisahkan koma): ")
if data1.strip() != "":
    for data in data1.split(","):
        list1.insert_at_end(int(data.strip()))  # tambah ke list1

data2 = input("Masukkan elemen untuk Linked List 2 (pisahkan koma): ")
if data2.strip() != "":
    for data in data2.split(","):
        list2.insert_at_end(int(data.strip()))  # tambah ke list2

print("Linked List 1:")
list1.display()

print("Linked List 2:")
list2.display()

# Gabungkan list2 ke akhir list1 (in-place) dan tampilkan hasil
list1.merge(list2)

print("Linked List setelah digabungkan:")
list1.display()
