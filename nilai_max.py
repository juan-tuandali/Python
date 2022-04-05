# tujuan program : Cek nilai max
# kamus data :
            # var. nilai = penampung nilai inputan user
            # var. nilai_max = tempat menampung nilai max awal maupun akhir
            
# input user
nilai = int(input("masukkan nilai (9999 untuk stop) : "))
# nilai max awal  
nilai_max = 0
    
# process
while (nilai != 9999): # menentukan kondisi pengulangan
    nilai = int(input("masukkan nilai (9999 untuk stop) : "))
    if (nilai > nilai_max and nilai != 9999): # membuat pengkondisian untuk mencari nilai max
        nilai_max = nilai
            
# output
print("----------------------------------------(max)")
print("Nilai terbesar =",nilai_max)
