    #input
    angka_N = int(input("N : "))
    
    # process
    # loop1 -> untuk kolom
    for i in range(0,angka_N,1):
        # loop2 -> untuk spasi
        for j in range(angka_N,i+1,-1):
            print(" ",end=" ")
        # loop3 -> untuk baris dan cetak bintang
        for k in range(0,angka_N,1):
            print("*",end=" ")
                
        print()
