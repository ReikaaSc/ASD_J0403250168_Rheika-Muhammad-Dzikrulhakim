# ==========================================================
# Nama  : Rheika Muhammad Dzikrulhakim
# NIM   : J0403251068
# Modul : Praktikum 5 - Materi 1
# Topik : Rekursi Faktorial
# ==========================================================

# Fungsi rekursif untuk menghitung faktorial
# parameter n adalah angka yang akan dihitung faktorialnya

def faktorial(n):

    # BASE CASE: ketika n mencapai 0, kembalikan 1
    # ini menghentikan chain rekursi
    if n == 0:
        return 1

    # RECURSIVE CASE: kalikan n dengan faktorial(n-1)
    # setiap pemanggilan mengecilkan nilai n hingga base case
    return n * faktorial(n - 1)


# Pemanggilan fungsi dan cetak hasilnya
print("Hasil faktorial:", faktorial(5))

# panggilan awal membuat rangkaian rekursif hingga n=0
# panggilan terkecil mengembalikan 1, lalu setiap level
# mengalikan hasil dengan nilai n pada level itu
# proses unwinding mengembalikan produk akhir ke pemanggil
