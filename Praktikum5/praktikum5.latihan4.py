# ==========================================================
# Nama  : Rheika Muhammad Dzikrulhakim
# NIM   : J0403251068
# Praktikum 5 - Latihan 4
# Kombinasi Huruf A dan B
# ==========================================================

def kombinasi(n, hasil=""):  # cetak semua kombinasi panjang n dari huruf A dan B

    # BASE CASE: jika panjang string yang dibangun sama dengan n, tampilkan
    if len(hasil) == n:
        print(hasil)
        return

    # pilih A di posisi berikutnya dan lanjutkan rekursi
    kombinasi(n, hasil + "A")
    # pilih B di posisi berikutnya dan lanjutkan rekursi
    kombinasi(n, hasil + "B")


# panggil fungsi untuk n=2 dan amati daftar kombinasi
kombinasi(2)

# setiap posisi memiliki dua pilihan, sehingga total kombinasi = 2^n
# pemanggilan rekursif membentuk pohon keputusan dengan dua cabang
# untuk n=2, algoritme mencetak 4 string: AA, AB, BA, BB
