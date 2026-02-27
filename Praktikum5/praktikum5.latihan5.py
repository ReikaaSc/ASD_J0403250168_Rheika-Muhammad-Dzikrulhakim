# ==========================================================
# Nama  : Rheika Muhammad Dzikrulhakim
# NIM   : J0403251068
# Praktikum 5 - Latihan 5
# Generator PIN Backtracking
# ==========================================================

def buat_pin(panjang, hasil=""):  # buat semua kombinasi PIN dengan digit 0-2

    # BASE CASE: jika panjang string sudah sama dengan panjang yang diinginkan
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return

    # iterasi terhadap setiap kemungkinan angka, tambahkan satu per satu
    for angka in ["0", "1", "2"]:
        # panggil rekursif dengan menambahkan angka baru ke hasil
        buat_pin(panjang, hasil + angka)


# panggil generator pin untuk panjang 3
buat_pin(3)

# algoritme mengeksplorasi semua urutan panjang 3 dari digit 0-2
# karena tidak ada pembatasan, angka dapat muncul berulang
# untuk menghindari pengulangan, kita bisa menambah parameter
# atau struktur data yang mencatat apa saja yang sudah dipakai
