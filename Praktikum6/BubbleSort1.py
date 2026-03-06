# =======================================
# Praktikum 6 - Bubble Sort
# ascending order
# =======================================

def bubblesort(data):
    for passnum in range(len(data)-1,0,-1):
        for i in range(passnum):
            if data[i]>data[i+1]:
                # tukar dua data yang salah urutannya
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp
                
data = [54,26,93,17,77,31,44,55,20]
bubblesort(data)
print(data)

def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum-1
        
alist=[70, 30, 100, 20, 60, 110, 40, 80, 50, 90]
shortBubbleSort(alist)
print(alist)