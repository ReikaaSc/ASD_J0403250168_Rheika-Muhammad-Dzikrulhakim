#===========================================================
# Nama    : Rheika Muhammad Dzikrulhakim
# NIM     : J0403251068
# Kelas   : TPL A/P1
#===========================================================

#===========================================================
# Implementasi Dasar : Node pada linked list
#===========================================================

class Node:
    #Konstruktor yang dijalankan secara otomatiis ketika class node dipanggil
    def __init__(self, data):
        self.data = data  # menyimpan nilai data pada list
        self.next = None  # pointer ke node berikutnya, awalnya None (tidak menunjuk kemana-mana)

# 1) Membuat node dengan instantiasi class Node
nodeA = Node("A")  # membuat node dengan data "A"
nodeB = Node("B")  # membuat node dengan data "B"
nodeC = Node("C")  # membuat node dengan data "C"

# 2) Menghubungkan node-node tersebut : A -> B -> C -> None
head = nodeA  # head menunjuk ke nodeA
nodeA.next = nodeB  # nodeA menunjuk ke nodeB
nodeB.next = nodeC  # nodeB menunjuk ke nodeC

# 3) Traversal : Menelusuri node dari head sampai akhir (None)
current = head  # mulai dari head
while current is not None:  # selama current tidak None
    print(current.data)  # cetak data node saat ini
    current = current.next  # pindah ke node berikutnya  
    


