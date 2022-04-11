    # Tujuan Program : Membuat program kelipatan 5 atau 7
    # Kamus data :
    #             nilai = var. untuk menampung inputan nilai yang di masukkan user
    # Imput user
    nilai = int(input("Masukkan nilai : "))
    
    # Process
    print("---------------output---------------")
    print("Nilai : ", nilai)
    if (nilai % 7 == 0 and nilai % 5 == 0):
        print(nilai,"adalah kelipatan 5 dan kelipatan 7\n")
    elif (nilai % 7 == 0 and nilai % 5 != 0):
        print(nilai,"adalah bukan kelipatan 5 tetapi kelipatan 7\n")
    elif (nilai % 7 != 0 and nilai % 5 == 0):
        print(nilai,"adalah kelipatan 5 tetapi bukan kelipatan 7\n")
    else :
        print(nilai,"adalah bukan kelipatan 5 dan bukan kelipatan 7\n")
