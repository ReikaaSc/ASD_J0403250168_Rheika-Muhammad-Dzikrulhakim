class Node:
    # Node merepresentasikan elemen tunggal dalam linked list.
    # Atribut:
    # - data: nilai yang disimpan di node
    # - next: referensi ke node berikutnya (None jika tidak ada)
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Implementasi linked list sederhana (singly linked list).
    # Atribut:
    # - head: node pertama dalam list (None jika kosong)
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        # Menambahkan node baru di akhir linked list.
        # Langkah:
        # 1. Buat Node baru dengan data.
        # 2. Jika list kosong, jadikan node ini sebagai head.
        # 3. Jika tidak, temukan node terakhir dan sambungkan next ke node baru.
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_node(self, key):
        # Menghapus node pertama yang memiliki nilai sama dengan key.
        # Penanganan kasus:
        # - Jika head yang cocok -> geser head ke node berikutnya.
        # - Jika node ditemukan di tengah/akhir -> sambungkan prev.next ke temp.next.
        # - Jika tidak ditemukan -> beri tahu pengguna.
        temp = self.head

        # Jika node pertama yang ingin dihapus
        if temp and temp.data == key:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if not temp:
            print("Data tidak ditemukan")
            return

        prev.next = temp.next

    def display(self):
        # Menampilkan seluruh elemen linked list dari head ke akhir.
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

# Blok eksekusi utama:
# 1. Baca input elemen dari pengguna (dipisah koma),
# 2. Bangun linked list dengan menambahkan tiap elemen di akhir,
# 3. Tampilkan list, minta nilai yang ingin dihapus, lalu tampilkan hasil akhir.
ll = LinkedList()
data_input = input("Masukkan elemen (pisahkan dengan koma): ")
data_list = data_input.split(",")

for data in data_list:
    ll.insert_at_end(int(data.strip()))

print("Linked List:")
ll.display()

key = int(input("Masukkan elemen yang ingin dihapus: "))
ll.delete_node(key)

print("Linked List setelah penghapusan:")
ll.display()