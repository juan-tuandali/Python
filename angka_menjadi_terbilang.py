# Tujuan Program : Membuat program Konversi Angka menjadi terbilang
# Kamus data :
            # angka_spesial : var. sebagai tempat menampung beberapa angka khusus
            # hasil : var. yang saya buat untuk menampung nilai yang di manipulasi/diproses 
            # nilai : var. tempat untuk menampung angka yang di input user untuk di proses
            # konversi = var. tempat yang menampung value akhir yang nanti akan di tampilkan ke layar (output)


def terbilang(bil):
    
    angka_spesial = ["","Satu","Dua","Tiga","Empat","Lima","Enam",
            "Tujuh","Delapan","Sembilan","Sepuluh","Sebelas"]
    hasil = " "
    nilai = int(bil)
    
    # Process
    if (nilai>= 0 and nilai <= 11):
        hasil = angka_spesial[nilai]
        
    elif (nilai < 20):
        hasil = terbilang (nilai - 10) + " Belas "
        
    elif (nilai < 100):
        hasil = terbilang (nilai / 10) + " Puluh " + terbilang (nilai % 10)
        
    elif (nilai < 200):
        hasil = " Seratus " + terbilang (nilai - 100)
        
    elif (nilai < 1000):
        hasil = terbilang (nilai / 100) + " Ratus " + terbilang (nilai % 100)
    else:
        hasil = "Tidak terjangkau"
        
    return hasil # return untuk mengembalikan value dari hasil yang sudah di proses

# Input user
angka = input("Masukkan angka (1 sd 999) : ")
print("---------------------------")
print("Angka",angka)

# Output
konversi = terbilang(angka)
print("Hasil Konversi :")
print(konversi)
