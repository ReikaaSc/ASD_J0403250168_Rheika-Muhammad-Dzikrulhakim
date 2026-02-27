# ==========================================================
# Nama  : Rheika Muhammad Dzikrulhakim
# NIM   : J0403251068
# Praktikum 5 - Materi 5
# Backtracking dengan Pruning
# ==========================================================

def biner_batas(n, batas, hasil="", jumlah_1=0):  # kombinasikan biner dengan batas maksimal angka 1

    # PRUNING: hentikan cabang jika jumlah '1' sudah lebih dari batas
    if jumlah_1 > batas:
        return

    # BASE CASE: jika panjang hasil sama dengan n, cetak dan berhenti
    if len(hasil) == n:
        print(hasil)
        return

    # cabang di mana kita memilih 0 (tidak menambah jumlah_1)
    biner_batas(n, batas, hasil + "0", jumlah_1)

    # cabang di mana kita memilih 1 (menambah jumlah_1)
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)


# jalankan fungsi dengan n=4 dan batas 2 untuk melihat efek pruning
biner_batas(4, 2)

# fungsi menelusuri kombinasi biner dan menghentikan cabang
# setelah jumlah '1' melebihi batas
# pruning mengurangi jumlah panggilan rekursif yang tidak perlu
