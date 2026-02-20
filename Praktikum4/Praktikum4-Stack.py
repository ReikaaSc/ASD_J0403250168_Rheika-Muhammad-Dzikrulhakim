#===========================================================
# Nama    : Rheika Muhammad Dzikrulhakim
# NIM     : J0403251068
# Kelas   : TPL A/P1
#===========================================================

#===========================================================
# Implementasi Dasar : Stack 
#===========================================================

class Node:
    #konstruktor yang dijalankan secara otomatiis ketika class node dipanggil
    def __init__(self, data):
        self.data = data  # menyimpan nilai data pada list
        self.next = None  # pointer ke node berikutnya, awalnya None (tidak menunjuk kemana-mana)
        
# Stack ada operasi push(memasukan head baru) dan pop(menghapus head)

class Stack:
    def __init__(self):
        self.top = None  # Top menunjuk ke node paling atas (awalnya None)
        
    def is_empty(self):
        return self.top is None  # Stack kosong jika top None

    def push(self, data): # memasukan data baru ke stack
        #1) membuat node baru
        nodeBaru = Node(data)  # instansiasi/memanggil konstruktor pada class node
        
        #2) node baru  menunjuk ke top uang lama (head lama)
        nodeBaru.next = self.top  # node baru menunjuk ke top lama
        
        #3) geser top pindah ke node baru
        self.top = nodeBaru  # top sekarang menunjuk ke node baru
    
    def pop(self): # menghapus data paling atas pada stack
        
        if self.is_empty():  # cek apakah stack kosong
            print("Stack kosong. Tidak ada data yang bisa di-pop.")
            return None
        data_terhapus = self.top.data  # soroti bagian top dan simpan di variabel (Peek)
        self.top = self.top.next  # geser top ke node berikutnya (top lama dihapus)
        return data_terhapus  # kembalikan data yang dihapus
    
    def peek(self):
        # melihat data yang paling atas tanpa menghapus
        if self.is_empty():  # cek apakah stack kosong
            print("Stack kosong. Tidak ada data yang bisa di-peek.")
            return None
        return self.top.data  # kembalikan data pada top tanpa menghapus
        
    def tampilkan(self):
        # top - A -> B
        current = self.top  # mulai dari top
        print("Top->", end="")
        while current is not None:  # selama current tidak None
            print(current.data, end="->")  # cetak data node saat ini
            current = current.next  # pindah ke node berikutnya
        print("None")  # akhir stack
        
#Instantiasi class stack
s = Stack()  # membuat objek stack
s.push("A")  # push data "A" ke stack
s.push("B")  # push data "B" ke stack
s.push("C")  # push data "C" ke stack
s.tampilkan()  # tampilkan isi stack
print("peek lihat top :", s.peek())  # lihat data paling atas
s.pop()  # pop data paling atas (C dihapus)
s.tampilkan()  # tampilkan isi stack setelah pop
print("peek lihat top :", s.peek())  # lihat data paling atas
s.pop()  # pop data paling atas (C dihapus)
s.tampilkan()  # tampilkan isi stack setelah pop
print("peek lihat top :", s.peek())  # lihat data paling atas
s.pop()  # pop data paling atas (C dihapus)
s.tampilkan()  # tampilkan isi stack setelah pop