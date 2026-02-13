#Praktikum 2 konsep ADT dan File Handling (STUDI KASUS)
#Latihan 1 Membuat fungsi load data dari file 

#Variable menyimpan data
nama_file = "Praktikum2/data_mahasiswa.txt" 

def baca_data(nama_file):
    data_dict = {} #menginisialisasi dictionary
    with open(nama_file, "r", encoding="utf-8") as file :
        for baris in file :
            baris = baris.strip()#mengambil data dan menghilangka new lfine
            nim, nama, nilai = baris.split(",") # ambil data per item data
            data_dict[nim] = {"nama": nama, "nilai": int(nilai)}# masukan dalam
    return data_dict

# buka_data = baca_data(nama_file)
# print ("Jumlah data terbaca", len(buka_data))

#latihan 2 membuat fungsi menampilkan data

def tampilkan_data(data_dict):
    #membuat header tabel
    print("\n========= DAFTAR MAHASISWA =========")
    print(f"{'NIM' : <10} | {'Nama' : <12} | {'Nilai' :>5}")
    print("-"*36)# membuat garis
    
    '''
    NIM artinya untuk menampikan nim rata kiri dengan lebar kolom 10
    '''
    
    #menampikan isi datanya
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim:<10} | {nama:<12} | {int(nilai):>5}")
            
# tampilkan_data(buka_data) # memanggil fungsi untuk menampilkan data

# Latihan 3 Membuat fungsi mencari data

def cari_data(data_dict):
    # pencarian data berdasarkan nim sebagai key dictionary
    # membuat input nim mahasiswa yang akan dicari
    nim_cari =  input("Masukan NIM mahasiswa yang ingin dicari: ").strip()
    
    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]
        
        print("===== Data Mahasiswa Ditemukan =====")
        print(f'NIM     : {nim_cari}')
        print(f"Nama    : {nama}")
        print(f"Nilai   : {nilai}")
    else:
        print("Data tidak ditemukan. Pastikan NIM yang dimasukan benar dan terdaftar")
        
# # Memanggil fungsi cari data 
# cari_data(buka_data)

# Latihan 4 Membuat fungsi Update Data

def ubah_data(data_dict):
    
    #awali dulu dengan mencari data / nim mahasiswa yang ingin di update
    nim = input("Masukan NIM mahasiswa yang ingin diubah datanya :").strip()
    
    if nim not in data_dict:
        print("NIM tidak ditemukan. Update dibatalkan")
        return
    
    try:
        nilai_baru = int(input("Masukan nilai baru 0-100 :").strip())
    except ValueError:      
        print("Nilai harus berupa angka . Update dibatalkan")
        
    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus diantara 0 sampai 100. Update dibatalkan")
    
    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru
    
    print(f"Update behasil. NIlai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")
    
# # memanggil ubah data
# ubah_data(buka_data)

# Latihan 5 Membuat fungsi menyimpan data pada file

#  membuat fungsi menyimpan data ke file
def simpan_data(nama_file, data_dict):
    with open(nama_file,"w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")
            
# Memanggil fungsi simpan   
# simpan_data(nama_file,buka_data)
# print("\nData berhasil Disimpan ke file :",nama_file)

# Latihan 6 Membuat Menu interaktif

def main():
    # load data otomatis saat program dimulai
    buka_data = baca_data(nama_file) # fungsi nu kahiji
    
    while True:
        print("\n======MENU DATA MAHASISWA======")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Mahasiswa")
        print("3. Ubah Data Mahasiswa")
        print("4. Simpan Data ke File")
        print("0. Keluar")
        
        pilihan = input("Pilih Menu: ").strip()
        
        if pilihan == "1":
            tampilkan_data(buka_data) # calling Function number 2 show data
        elif pilihan == "2":
            cari_data(buka_data) # memanggil fungsi ke 3 mencari data
        elif pilihan == "3":
            ubah_data(buka_data) # Nyaut fungsi nu ka 4 ngubah data
        elif pilihan == "4":
            simpan_data(nama_file, buka_data) # calling function number 5 saving data to file
            print("Data Berhasil Disimpan")
        elif pilihan == "0":
            print("Program Selesai.") # mengakhiri program euy
            break
        else :
            print("Pilihan tidak Valid") # Kalo ga bener mengisi inout
        
main()