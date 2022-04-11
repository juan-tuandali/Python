# tujuan program : Prima
# kamus data : 
            # angka = var. untuk inputan dari user
            # cek = var. untuk menampung nilai prima/bukan
# note : bilangan prima adalah bilangan yang hanya habis jika dibagi dengan 1 dan dirinya sendiri

# input
angka = int(input())

# process
cek = "Prima"
if (angka > 1):
    for i in range(2,angka): # dimulai dari 2 karena jika i=1, semua angka dapat habis dibagi dengan 1
        if (angka % i == 0):
            cek = "Bukan Prima"
    print(cek)
else:
    print("Angka harus lebih dari 1!")
