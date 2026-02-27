# ==========================================================
# Nama  : Rheika Muhammad Dzikrulhakim
# NIM   : J0403251068
# Praktikum 5 - Latihan 3
# Mencari Nilai Maksimum Rekursif
# ==========================================================

def cari_maks(data, index=0):  # cari nilai maksimum dari list 'data' mulai pada posisi 'index'

    # BASE CASE: jika index berada di elemen terakhir, kembalikan nilai itu
    if index == len(data) - 1:
        return data[index]

    # RECURSIVE CALL: tentukan maksimum dari sisa list setelah index
    maks_sisa = cari_maks(data, index + 1)

    # bandingkan nilai sekarang dengan maksimum dari sisa
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa


angka = [3, 7, 2, 9, 5]
# cetak hasil maksimum yang ditemukan oleh fungsi
print("Nilai maksimum:", cari_maks(angka))

# mulai dari index 0, fungsi memanggil diri sendiri hingga indeks terakhir
# pada setiap langkah, nilai saat ini dibandingkan dengan hasil rekursif
# nilai tertinggi dibawa kembali melalui tumpukan panggilan
# akhirnya fungsi utama menerima nilai maksimum dan mencetaknya
