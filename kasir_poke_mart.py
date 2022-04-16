# Tujuan Program : Poke Mart
# kamus data :
#           pokeBall : var input (int)
#           greatBall : var input (int)
#           ultraBall : var input (int)
#           potion : var input (int)
#           fullheal : var input (int)
#           nama_barang : var input (int)
#           jumlah_barang : var input (int)
#           total_terjual : var penampung value barang yang terjual
#           total_labaKotor : var penampung value laba yang dihasilkan

def main():
    
    # input
    print("Masukkan Stok Barang")
    pokeBall = int(input("PokeBall : "))
    greatBall = int(input("GreatBall : "))
    ultraBall = int(input("UltraBall : "))
    potion = int(input("Potion : "))
    fullheal = int(input("FullHeal : "))
    print("============================")
    
    nama_barang = str(input("Nama Barang (PokeBall/GreatBall/UltraBall/Potion/FullHeal/Selesai) :\n "))

    # process
    total_terjual = 0
    total_laba = 0
    
    while nama_barang != "selesai":
        
        jumlah_barang = int(input("Jumlah : "))
        
        if (nama_barang == "PokeBall"):
            if (pokeBall>=jumlah_barang):
                pokeBall -= jumlah_barang
                total_laba += 200*jumlah_barang
                total_terjual+= jumlah_barang
            else:
                print(f"Mohon maaf stok barang tidak mancukupi\nJumlah : {pokeBall}")
                
        elif (nama_barang == "Potion"):
            if (potion>=jumlah_barang):
                potion -= jumlah_barang
                total_laba += 300*jumlah_barang
                total_terjual+= jumlah_barang
            else:
                print(f"Mohon maaf stok barang tidak mancukupi\nJumlah : {potion}")

        elif (nama_barang == "GreatBall"):
            if (greatBall>=jumlah_barang):
                greatBall -= jumlah_barang
                total_laba += 600*jumlah_barang
                total_terjual+= jumlah_barang
            else:
                print(f"Mohon maaf stok barang tidak mancukupi\nJumlah : {greatBall}")

        elif (nama_barang == "UltraBall"):
            if (ultraBall>=jumlah_barang):
                ultraBall -= jumlah_barang
                total_laba += 1200*jumlah_barang
                total_terjual+= jumlah_barang
            else:
                print(f"Mohon maaf stok barang tidak mancukupi\nJumlah : {ultraBall}")
                
        elif (nama_barang == "FullHeal"):
            if (ultraBall>=jumlah_barang):
                fullheal -= jumlah_barang
                total_laba += 600*jumlah_barang
                total_terjual+= jumlah_barang
            else:
                print(f"Mohon maaf stok barang tidak mancukupi\nJumlah : {fullheal}")
            
        else:
            break
        
        nama_barang = str(input("\nNama Barang (PokeBall/GreatBall/UltraBall/Potion/FullHeal/Selesai) :\n "))
    
    # output
    print("============================")
    print(f"""Sisa Stok Barang yang dimiliki :
PokeBall  : {pokeBall}
GreatBall : {greatBall}
UltraBall : {ultraBall}
Potion    : {potion}
FullHeal  : {fullheal}
""")
    print(f"Total barang yang terjual : {total_terjual} ")
    print(f"Total Laba Kotor : {total_laba} ")
    print("============================\n")
    
if __name__=='__main__':
    main()
