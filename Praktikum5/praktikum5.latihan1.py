# ==========================================================
# Nama  : Rheika Muhammad Dzikrulhakim
# NIM   : J0403251068
# Praktikum 5 - Latihan 1
# Rekursi Pangkat
# ==========================================================

def pangkat(a, n):  # fungsi untuk menghitung a^n menggunakan rekursi

    if n == 0: # BASE CASE: jika eksponen n sudah 0, berhenti rekursi dan kembalikan 1
        return 1

    # RECURSIVE CALL: kalikan a dengan hasil pangkat(a, n-1)
    # setiap pemanggilan menurunkan nilai n hingga mencapai base case
    return a * pangkat(a, n - 1)


# pemanggilan fungsi dan menampilkan hasil perhitungan 2 pangkat 4
print(pangkat(2, 4))

# pangkat(2,4) memanggil pangkat(2,3) dan mengalikan hasilnya dengan 2
# pangkat(2,3) memanggil pangkat(2,2) dan mengalikan hasilnya dengan 2
# proses berlanjut hingga pangkat(2,0) yang memenuhi base case dan mengembalikan 1
# nilai-nilai dikalikan mundur menuju pangkat(2,4) sehingga hasil akhir 16
