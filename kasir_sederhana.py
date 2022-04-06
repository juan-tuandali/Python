    # membuat program kasir sederhana
    # Kamus Data
    # kode : var. input (integer)
    # pkt1 : var. input (integer)
    # pkt2 : var. input (integer)
    # pkt3 : var. input (integer)
    # diskon : var. penampung nilai diskon
    # paket1 : var. penampung nilai paket1
    # paket2 : var. penampung nilai paket2
    # paket3 : var. penampung nilai paket3
    # total : var. penampung nilai total
    
    print("Kode == 1 or 2 -> diskon 10%")
    kode = int(input("Kode (99 untuk stop) : "))

    # process
    while kode != 99:
        
        # input
        pkt1 = int(input("Paket1 : "))
        pkt2 = int(input("Paket2 : "))
        pkt3 = int(input("Paket3 : "))
        
        diskon = 0
        paket1 = 60000
        paket2 = 40000
        paket3 = 45000
        total = 0
    
        print("---------------------------------------")
        # paket 1
        if (pkt1 == 0):
            paket1 *= 0
        elif (pkt1 >= 1):
            paket1 *= pkt1
            print("Paket1 :",pkt1,"x Rp. 60000 = Rp.",paket1)
        # paket 2   
        if (pkt2 == 0):
            paket2 *= 0
        elif (pkt2 >= 1):
            paket2 *= pkt2
            print("Paket2 :",pkt2,"x Rp. 40000 = Rp.",paket2)
        # paket 3 
        if (pkt3 == 0):
            paket3 *=0
        elif (pkt3 >= 1):
            paket3 *= pkt3
            print("Paket3 :",pkt3,"x Rp. 45000 = Rp.",paket3)
            
        # total
        total = paket1 + paket2 + paket3
        print("Total = Rp.",total)
        
        # diskon 
        if (kode == 1 or kode == 2):
            diskon = total * 10 // 100
            print("Diskon = Rp.",diskon)
        else:
            diskon
            print("Diskon = Rp.",diskon)
            
        # dibayar
        print("---------------------------------------")
        print("Yang harus dibayar = ",total - diskon)
        print("---------------------------------------")

        print("Kode == 1 or 2 -> diskon 10%")
        kode = int(input("Kode (99 untuk stop) : "))
