    # input
    bilangan = int(input("Bilangan (11 - 9999): "))

    # process
    bil = bilangan
    temp = 0
    rev = 0
    
    if (bilangan >= 11):
        # proses mengambil angka terakhir pada inputan
        temp = bil % 10
        rev = temp
        # untuk menjadikan rev mengambil 1 angka lagi
        bil //= 10 # mengubah bilangan yang tadinya misalkan 4 digit sekarang tinggal 3 digit
        temp = bil % 10
        rev = (rev * 10) + temp 
        
        if (bilangan == rev): # pengecekan pertama
            print(f"Bilangan {bilangan} merupakan bilangan polindrom")
        else:
            # untuk menjadikan rev mengambil 1 angka lagi
            bil //= 10 # mengubah bilangan yang tadinya misalkan 3 digit sekarang tinggal 2 digit
            temp = bil % 10
            rev = (rev * 10) + temp 
            
            if (bilangan == rev): # pengecekan kedua
                print(f"Bilangan {bilangan} merupakan bilangan polindrom")
            else:
                # untuk menjadikan rev mengambil 1 angka lagi
                bil //= 10 # mengubah bilangan yang tadinya misalkan 2 digit sekarang tinggal 1 digit
                temp = bil % 10
                rev = (rev * 10) + temp 
                # print(rev)
                if (bilangan == rev): # pengecekan ketiga
                    print(f"Bilangan {bilangan} merupakan bilangan polindrom")
                else:
                    print(f"Bilangan {bilangan} bukan bilangan polindrom")
                
    else:
        print("Angka yang anda masukkan tidak sesuai range yang ditentukan!")
