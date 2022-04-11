# Tujuan Program : Membuat program pertambahan waktu
# Kamus data :
            # var detik = menampung nilai detik
            # var menit = menampung nilai menit
            # var jam = menampung nilai jam
            # var jenisWaktu = menampung nilai jenisWaktu

def main():
    
    # input user
    detik = int(input("\ndetik : "))
    menit = int(input("menit : "))
    jam = int(input("jam : "))

    print(f"Waktu Sekarang :\n{jam:02} : {menit:02} : {detik:02}")

    # process
    while True:
        jenisWaktu = int(input("jenisWaktu (1.detik | 2.menit | 3.jam | 4.exit) : "))
        
        if (jenisWaktu == 1):
            detik_tambahan = int(input("detik : "))
            detik += detik_tambahan
            if (detik >= 60):
                menit += (detik // 60)
                detik %= 60
                if (menit >= 60):
                    jam += (menit//60)
                    menit %= 60
                    if (jam >= 24):
                        jam %= 24
        elif (jenisWaktu == 2):
            menit_tambahan = int(input("menit : "))
            menit += menit_tambahan
            if (menit >= 60):
                jam += (menit // 60)
                menit %= 60
                if (jam >= 24):
                    jam %= 24
        elif (jenisWaktu == 3):
            jam_tambahan = int(input("jam : "))
            jam = jam + jam_tambahan
            if (jam >= 24):
                jam %= 24
        elif (jenisWaktu == 4):
            break
            
        else:
            print("pilih jenis waktu sesuai yang ditentukan!")
            
        print(f"Hasil Penjumlahan : \n{jam:02} : {menit:02} : {detik:02}")
        print("------------------------------------")
        
    print(f"""------------------------------------
Hasil Penjumlahan :
{jam:02} : {menit:02} : {detik:02}
            """)
    
    return 0
if __name__ == '__main__':
    main()
