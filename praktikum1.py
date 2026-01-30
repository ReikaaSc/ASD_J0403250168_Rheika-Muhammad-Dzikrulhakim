#Praktikum 1 : konsep adt dan manipulasi file path
#Latihan Dasar 1 : Membaca seluruh isi file data

print("---Membuka file dalam satu string---")
with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    isi_file = file.read()
print(isi_file)
print('===hasil read===')
print("Tipe Data:", type(isi_file))

print("---Membuka file per baris---")
jumlah_baris = 0
with open('data_mahasiswa.txt','r')as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip()
        print('baris ke-', jumlah_baris)
        print('isinya', baris)
        
#Parsing baris menjadi data satuan dan menampilkannya dalam bentuk kolom2 data

with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() 
        nim, nama, nilai = baris.split(",") # pecah data menjadi satuan dalam bentuk kolom
        print("NIM :", nim, "| Nama:", nama, "  |Nilai:", nilai) #menampilkan data dalam bentuk kolom
        
#latian dasar 3 membaca data dan menyimpan data ke struktur data list
        
        data_list = []
        
        with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()
                nim, nama, nilai = baris.split(",") # pecah data satuan dan simpan ke variable
                data_list.append([nim,nama,int(nilai)]) # menyimpan data ke list
print("===Menampilkan List===")
print(data_list)
print('contoh record pertama', data_list[0])

#latihan dasar 4 membaca data dan menyimpannya ke struktur data dictionary

data_dict = {} #inisialisasi Dictionary

with open("data_mahasiswa.txt","r",encoding="utf=8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter newline
        nim, nama, nilai = baris.split(',') #pecah menjadi data satuan
            #simpan data dalam dictionary
        data_dict[nim] = {
        'nama' : nama,
        'nilai' : int(nilai),
        }
        
print("===menampilkan data dictionary===")
print(data_dict)