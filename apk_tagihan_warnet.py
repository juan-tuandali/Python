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
    # note1: untuk harga 1 jam pertama adalah 7000
    harga = 0
    if (menit == 1):
        harga += 7000
    else:
        harga += 7000 + ((menit-1)*6000)
    return harga
    # note2: untuk harga sisa menit = sisa menit*125
    
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
    if (sisaMenit(durasi_sewa) == 0):
        print("Jumlah Tagihan :",totalTagihan(menitKeJam(durasi_sewa)))
        if (jml_saldo >= totalTagihan(menitKeJam(durasi_sewa))):
            print("="*25)
            print('!!! LUNAS !!!\nSisa saldo :',jml_saldo - totalTagihan(menitKeJam(durasi_sewa)))
            print("="*25)
        else:
            print("="*25)
            print('Saldo anda tidak cukup!!!')
            print("="*25)
    else:
        print("Jumlah Tagihan :",totalTagihan(menitKeJam(durasi_sewa)) + (sisaMenit(durasi_sewa)*125))
        print("="*25)
        if (jml_saldo >= totalTagihan(menitKeJam(durasi_sewa))):
            print('!!! LUNAS !!!\nSisa saldo :',jml_saldo - (totalTagihan(menitKeJam(durasi_sewa))+ (sisaMenit(durasi_sewa)*125)))
            print("="*25)
        else:
            print("="*25)
            print('Saldo anda tidak cukup!!!')
            print("="*25)
                
    return 0
if __name__=='__main__':
    main()
    
