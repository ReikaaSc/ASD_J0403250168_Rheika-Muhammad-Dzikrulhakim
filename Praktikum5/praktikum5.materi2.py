# ==========================================================
# Nama  : Rheika Muhammad Dzikrulhakim
# NIM   : J0403251068
# Praktikum 5 - Materi 2
# Tracing Rekursi (Masuk & Keluar)
# ==========================================================

def hitung(n):  # tunjukkan urutan masuk/keluar panggilan rekursif

    # BASE CASE: jika n = 0, hentikan rekursi
    if n == 0:
        print("Selesai")
        return

    # STACKING: kita 'masuk' ke level dengan nilai n saat ini
    print("Masuk:", n)

    # panggil lagi dengan n-1, membentuk urutan rekursif
    hitung(n - 1)

    # UNWINDING: setelah panggilan balik selesai, kita keluar dari level n
    print("Keluar:", n)


# jalankan fungsi dengan n=3 untuk memperlihatkan logika
hitung(3)

# cetakan "Masuk" terjadi saat menurunkan n hingga mencapai 0
# setelah base case, panggilan dimulai kembali (unwinding)
# "Keluar" dicetak dalam urutan terbalik karena stack
