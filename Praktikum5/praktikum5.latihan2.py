# ==========================================================
# Nama  : Rheika Muhammad Dzikrulhakim
# NIM   : J0403251068
# Praktikum 5 - Latihan 2
# Tracing Rekursi
# ==========================================================

def countdown(n):  # fungsi rekursif untuk menghitung mundur dari n ke 0

    # BASE CASE: ketika n mencapai 0, hentikan rekursi dan tampilkan pesan
    if n == 0:
        print("Selesai")
        return

    # sebelum memanggil diri sendiri, tampilkan bahwa kita 'masuk' pada nilai n
    print("Masuk:", n)

    # panggilan rekursif dengan mengurangi nilai n
    countdown(n - 1)

    # setelah panggilan rekursif selesai (unwinding), cetak bahwa kita 'keluar'
    # dari level n tersebut
    print("Keluar:", n)


# panggil fungsi dengan n=3 dan perhatikan urutan print
countdown(3)

# output "Masuk" dicetak dari atas ke bawah saat memanggil fungsi
# ketika base case tercapai, fungsi mulai kembali (unwinding)
# oleh karena itu "Keluar" tercetak dalam urutan terbalik
# (dari panggilan terakhir kembali ke pertama)
