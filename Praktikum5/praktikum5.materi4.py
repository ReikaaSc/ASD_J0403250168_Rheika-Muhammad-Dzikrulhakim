# ==========================================================
# Nama  : Rheika Muhammad Dzikrulhakim
# NIM   : J0403251068
# Praktikum 5 - Materi 4
# Backtracking Kombinasi Biner
# ==========================================================

def biner(n, hasil=""):  # buat semua kombinasi biner sepanjang n

    # BASE CASE: panjang string telah mencapai n, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return

    # pilih 0 lalu lanjutkan konstruksi
    biner(n, hasil + "0")

    # pilih 1 lalu lanjutkan konstruksi
    biner(n, hasil + "1")


# panggil fungsi untuk n=3 dan amati struktur keluaran
biner(3)

# setiap panggilan menghasilkan dua cabang: 0 dan 1
# konstruksi membentuk pohon keputusan penuh
# semua kombinasi biner panjang 3 dicetak
