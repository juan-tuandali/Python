# Tujuan program : Program membaca nama dan data tanggal, bulan, tahun kadaluwarsa dari suatu makanan instan.
# Kamus data :
            # var nama_barang = untuk menampung nama barang yang di input user
            # var tanggal = untuk menampung tangal yang di input user
            # var bulan = untuk menampung bulan yang di input user
            # var tahun = untuk menampung tahun yang di input user
            # var tanggal_sekarang = untuk menampung tangal sekarang yang di input user
            # var bulan_sekarang = untuk menampung bulan sekarang yang di input user
            # var tahun_sekarang=beli = untuk menampung tahun sekarang yang di input user

# input
nama_barang = str(input("\nNama barang : "))
tanggal_kadaluwarsa = int(input("Tanggal kadaluwarsa : "))
bulan_kadaluwarsa = int(input("Bulana kadaluwarsa : "))
tahun_kadaluwarsa = int(input("Tahun kadaluwarsa : "))
print("+-----------------------+")
tanggal_sekarang = int(input("Tanggal sekarang : "))
bulan_sekarang = int(input("Bulan sekarang : "))
tahun_sekarang = int(input("Tahun sekarang : "))
print("+-----------------------+")

# proses
if tahun_kadaluwarsa<tahun_sekarang:
    # output1
    print(nama_barang,"sudah KADALUWARSA, tidak boleh dimakan !")
elif tahun_kadaluwarsa>tahun_sekarang:
    # output2
    print(nama_barang," masih aman untuk dikonsumsi sampai dengan ",tanggal_kadaluwarsa,"/",bulan_kadaluwarsa,"/",tahun_kadaluwarsa,sep="") # menambahkan format sep untuk membuat tanggal,bulan dan tahun berdempetan atau tidak ada spasi    
else:
    if bulan_kadaluwarsa>bulan_sekarang:
        # output3
        print(nama_barang," masih aman untuk dikonsumsi sampai dengan ",tanggal_kadaluwarsa,"/",bulan_kadaluwarsa,"/",tahun_kadaluwarsa,sep="")
    elif bulan_kadaluwarsa<bulan_sekarang:
        # output4
        print(nama_barang,"sudah KADALUWARSA, tidak boleh dimakan !")
    else:
        if tanggal_kadaluwarsa>tanggal_sekarang:
            # output5
            print(nama_barang," masih aman untuk dikonsumsi sampai dengan " ,tanggal_kadaluwarsa,"/",bulan_kadaluwarsa,"/",tahun_kadaluwarsa,sep="")
        elif tanggal_kadaluwarsa<tanggal_sekarang:
            # output6
            print(nama_barang,"sudah KADALUWARSA, tidak boleh dimakan !")
        else:
            print(nama_barang,"ini KADALUWARSA pada hari ini.")
            
