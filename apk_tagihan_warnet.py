# penulis : Juan Tuandali
# tujuan program: aplikasi tagihan warnet

# funct menit ke jam
# --kamus data-- :
#                convert : var penampung konversi menit ke jam 
#                menit : parameter function 
def menitKeJam(menit):
    convert = menit // 60
    return convert

# funct sisa menit
# --kamus data-- :
#                sisaMenit : var penampung sisa menit dari hasil konversi
#                menit : parameter function 
def sisaMenit(menit):
    sisaMenit = menit % 60
    return sisaMenit

# funct totalTagihan
# --kamus data-- :
#                sisaMenit : var penampung sisa menit dari hasil konversi
#                menit : parameter function 
def totalTagihan(menit):
    harga = 0
    if (menit == 1):
        harga += 7000
        return harga
    else:
        harga += 7000 + ((menit-1)*6000)
        return harga

# funct utama
# --kamus data-- :
#                jml_saldo : var inputan (integer)
#                durasi_sewa : var inputan (integer)
def main():
    print("="*7,"WARNET KUY",7*"=")
    jml_saldo = int(input("Jumlah Saldo : "))
    durasi_sewa = int(input("Durasi Sewa (menit) : "))
    print("="*25)
    print("Total Sewa",menitKeJam(durasi_sewa),"jam",sisaMenit(durasi_sewa),"menit")
    print("Jumlah Tagihan :",totalTagihan(menitKeJam(durasi_sewa)))
    print("="*25)
    if (jml_saldo > totalTagihan(menitKeJam(durasi_sewa))):
        print("SIsa Saldo :",jml_saldo - totalTagihan(menitKeJam(durasi_sewa)))
    else:
        print("Mohon lakukan isi ulang kepada admin!")
    print("="*25)
    
    return 0
if __name__=='__main__':
    main()
