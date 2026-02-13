class Node:  # Node merepresentasikan elemen tunggal dalam linked list.
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:  # Implementasi linked list sederhana (singly linked list).
    def __init__(self):
        self.head = None     # head: node pertama dalam list (None jika kosong)

    def insert_at_end(self, data):  # Menambahkan node baru di akhir linked list.
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_node(self, key):  # Menghapus node pertama yang memiliki nilai sama dengan key.
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

    def display(self):  # Menampilkan seluruh elemen linked list dari head ke akhir.
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

# main kode block
ll = LinkedList()  # main: baca input, bangun list, hapus, tampilkan
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