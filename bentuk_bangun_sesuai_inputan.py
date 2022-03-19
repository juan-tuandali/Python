print("Pilih Gambar\n1. Segitiga\n2. Persegi Panjang\n3.Jajaran Genjang\n4. Selesai\n----------------------")
    # input
    pilihan = int(input("Pilihan : "))
    
    # process
    # loop awal
    while (pilihan != 4):
        
        if (pilihan==1):
            sisi = int(input("sisi : "))
            # loop 1 -> untuk kolom dan cetak spasi
            for i in range(1,sisi+1,1):
                print("  "*(sisi-i),end="")
                # loop 2 -> untuk baris dan cetak angka
                for j in range(1,i+1,1):
                    print(i,end=" ")
                print()
                
        elif (pilihan==2):
            panjang = int(input("Panjang : "))
            lebar = int(input("Lebar : "))
            # loop 1 -> lebar
            for i in range(1,lebar+1,1):
                # loop 2 -> panjang
                for j in range(1,panjang+1,1):
                    print(i,end=" ")
                print()                    
                
        elif (pilihan==3):
            panjang = int(input("Panjang : "))
            lebar = int(input("Lebar : "))
            # loop 1 -> kolom
            for i in range(1,panjang+1,1):
                # loop 2 -> space
                for j in range(panjang,i,-1):
                    print(" ",end=" ")
                # loop 3 -> baris
                for k in range(1,lebar+1,1):
                    print(i,end=" ")
                print()
                                    
        elif (pilihan==4):
            break # keluar dari loop
        else:
            print("Masukkan pilihan yang benar!")
            
        print("----------------------")
        pilihan = int(input("Pilihan : "))
