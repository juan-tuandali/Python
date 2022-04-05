# Tujuan Program : Membaca suatu bilangan integer yang menyatakan jumlah hari.
# Kamus data :
            # var jmlhHari (untuk input jumlah hari)
            # var sisaHari (untuk mencari sisa hari setelah jumlah hari di konversi kedalam bulan)
            # var minggu (untuk mencari ada berapa minggu setelah jumlah hari dikonversi kedalam bulan )
            # var hari (untuk mencari ada berapa hari setelah sudah diketahui ada berapa minggu)

 # Input
 jmlHari = int(input('Masukkan jumlah hari : '))
    
 # Proses
 bulan = jmlHari // 30
 sisaHari = jmlHari % 30 
 minggu = sisaHari // 7
 hari = sisaHari % 7
    
 # Output
 print("====================================================")
 print(jmlHari,"hari setara dengan",bulan,"bulan,",minggu,"minggu dan",hari,"hari")
 print("====================================================")
    
