#===========================================================
# Nama    : Rheika Muhammad Dzikrulhakim
# NIM     : J0403251068
# Kelas   : TPL A/P1
#===========================================================

#===========================================================
# Implementasi Dasar : Queue 
#===========================================================

class Node:
    # Konstruktor yang dijalankan secara otomatiis ketika class node dipanggil
    def __init__(self, data):
        self.data = data  # menyimpan nilai data pada list  
        self.next = None  # pointer ke node berikutnya, awalnya None (tidak menunjuk kemana-mana)
        
class Queue:
    def __init__(self): 
        self.front = None  # Front menunjuk ke node paling depan (awalnya None)
        self.rear = None   # Rear menunjuk ke node paling belakang (awalnya None)
    
    def is_empty(self):
        return self.front is None  # Queue kosong jika front None
    
    def enqueue(self, data): # memasukan data baru ke queue
        nodeBaru = Node(data)  # instansiasi/memanggil konstruktor pada class node
        if self.rear is None:  # jika queue kosong, front dan rear menunjuk ke node baru
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        self.rear.next = nodeBaru  # letakkan node baru pada setelah rear
        self.rear = nodeBaru  # jadikan data baru sebagai rear
    
    def dequeue(self): # menghapus data paling depan pada queue
        #menghapus data paling depan pada queue
        data_terhapus = None  # inisialisasi variabel untuk menyimpan data yang dihapus
        
        self.front = self.front.next  # geser front ke node berikutnya (front lama dihapus)
        if self.front is None:  # jika setelah di-dequeue queue menjadi kosong, set rear juga ke None
            self.rear = None
        return data_terhapus  # kembalikan data yang dihapus
    
    def tampilkan(self):
        current = self.front  # mulai dari front
        print("Front->", end="")
        while current is not None:  # selama current tidak None
            print(current.data, end="->")  # cetak data node saat ini
            current = current.next  # pindah ke node berikutnya
        print("Rear")  # akhir queue
        
#instansiasi class Queue
q = Queue()  # buat objek queue
q.enqueue("A")  # masukan data "A" ke queue
q.enqueue("B")  # masukan data "B" ke queue
q.enqueue("C")  # masukan data "C" ke queue
q.tampilkan()  # tampilkan isi queue