# ==========================================================
# Nama  : Rheika Muhammad Dzikrulhakim
# NIM   : J0403251068
# Praktikum 5 - Materi 3
# Menjumlahkan Elemen List Rekursif
# ==========================================================

def jumlah_list(data, index=0):  # jumlahkan semua elemen list secara rekursif

    # BASE CASE: jika indeks sudah berada di luar akhir list, tidak ada tambahan
    if index == len(data):
        return 0

    # RECURSIVE CASE: tambahkan elemen saat ini dengan jumlah sisa list
    return data[index] + jumlah_list(data, index + 1)


print("Total:", jumlah_list([2, 4, 6, 8]))

# setiap panggilan memproses satu elemen dan menaikkan index
# saat index mencapai panjang list, fungsi mengembalikan 0
# nilai-nilai dijumlah saat stack rekursif kembali
