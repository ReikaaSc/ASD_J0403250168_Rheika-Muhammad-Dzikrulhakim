#Praktikum 1 : konsep adt dan manipulasi file path
#Latihan Dasar 1 : Membaca seluruh isi file data

print("---Membuka file dalam satu string---")
with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    isi_file = file.read()
print(isi_file)