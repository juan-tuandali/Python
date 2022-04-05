# tujuan program : Menghitung Bonus gaji pegawai
# kamus data :
#           nik = var. input (integer)
#           nama = var. input (string)
#           lama_kerja = var. input (integer)
#           jabatan = var. input (integer)
#           prestasi = var. input (integer)
#           gaji = var. input (integer)
#           bonus_awal = var. input (integer)
#           bonus_prestasi = var. input (integer)
#           bonus_jabatan = var. input (integer)
#           total_bonus = var. input (integer)

# input
nik = int(input("NIK : "))
nama = str(input("Nama : "))
lama_kerja = int(input("Lama Kerja (tahun) : "))
jabatan = int(input("Jabatan (0/1/2) : "))
prestasi = int(input("Prestasi (1/2/3) : "))
gaji = int(input("Gaji : "))
    
# process
bonus_awal = 0
bonus_prestasi = 0
bonus_jabatan = 0
total_bonus = 0
    
if(lama_kerja < 10):
    bonus_awal = gaji * 5 // 100
elif(10 <= lama_kerja < 15):
    bonus_awal = gaji * 10 // 100
elif(15 <= lama_kerja < 20):
    bonus_awal = gaji * 15 // 100
else:
    bonus_awal = gaji * 20 // 100
        
if (jabatan == 2):
    bonus_jabatan = (bonus_awal * 10 // 100)
elif (jabatan == 1):
    bonus_jabatan = (bonus_awal * 5 // 100)
elif (jabatan == 0):
    bonus_jabatan = bonus_awal
        
if (prestasi == 3):
    bonus_prestasi = ((bonus_awal + bonus_jabatan) * 10 // 100)
elif (prestasi == 2): 
    bonus_prestasi = ((bonus_awal + bonus_jabatan) * 5 // 100)
elif (prestasi == 1):
    bonus_prestasi = bonus_awal + bonus_jabatan
    
total_bonus = bonus_awal + bonus_jabatan + bonus_prestasi
    
# output
print("\nNama :",nama," (",nik,")",sep="")
print("--------------------------------")
print("Gaji :",gaji)
print("Bonus awal :",bonus_awal)
print("Bonus jabatan :",bonus_jabatan)
print("Bonus prestasi :",bonus_prestasi)
print("--------------------------------")
print("Total Bonus :",total_bonus)
