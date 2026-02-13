class Node:
    # Node merepresentasikan satu elemen dalam linked list.
    # Atribut:
    # - data: nilai yang disimpan di node
    # - next: referensi ke node berikutnya (None jika belum terhubung)
    def __init__(self, data):
        self.data = data
        self.next = None
        
class CircularSinglyLinkedList:
    # Implementasi circular singly linked list sederhana.
    # Atribut:
    # - head: node pertama dalam list
    # - tail: node terakhir dalam list, tail.next menunjuk kembali ke head
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            # Jika list kosong, head dan tail sama-sama menunjuk ke node baru
            self.head = new_node
            self.tail = new_node
            # Karena circular, tail.next harus menunjuk ke head
            self.tail.next = self.head
        else:
            # Tambahkan node baru setelah tail dan update tail
            self.tail.next = new_node
            self.tail = new_node
            # Pastikan tetap circular dengan menunjuk kembali ke head
            self.tail.next = self.head

    def search(self, key):
        if not self.head:
            # Jika list kosong, hentikan pencarian
            print("Circular Linked List kosong. Tidak ada elemen yang bisa dicari.")
            return

        temp = self.head
        while True:
            if temp.data == key:
                # Ditemukan: tampilkan pesan dan hentikan
                print(f"Elemen {key} ditemukan dalam Circular Linked List.")
                return
            temp = temp.next
            if temp == self.head:
                break

        # Jika sudah kembali ke head, elemen tidak ada dalam list
        print(f"Elemen {key} tidak ditemukan dalam Circular Linked List.")

# Blok eksekusi utama: membaca input, membangun list, lalu melakukan pencarian
cll = CircularSinglyLinkedList()
data_input = input("Masukkan elemen (pisahkan dengan koma, kosong jika tidak ada): ")

if data_input.strip() != "":
    # Memisahkan input berdasarkan koma dan menambahkan setiap nilai ke list
    data_list = data_input.split(",")
    for data in data_list:
        cll.insert_at_end(int(data.strip()))

# Minta kunci untuk dicari dan panggil fungsi search
key = int(input("Masukkan elemen yang ingin dicari: "))
cll.search(key)