    # Kamus Data :
    # negara1 : var. input (string)
    # emas1 : var. input (integer)
    # perak1 : var. input (integer)
    # perunggu1 : var. input (integer)
    # negara2 : var. input (string)
    # emas2 : var. input (integer)
    # perak2 : var. input (integer)
    # perunggu2 : var. input (integer)
    # total_medali1 : var. penampung total medali negara 1
    # total_medali2 : var. penampung total medali negara 2
    
    # input
    negara1 = str(input("Negara : "))
    emas1 = int(input("Emas : "))
    perak1 = int(input("Perak : "))
    perunggu1 = int(input("Perunggu : "))
    negara2 = str(input("Negara : "))
    emas2 = int(input("Emas : "))
    perak2 = int(input("Perak : "))
    perunggu2 = int(input("Perunggu : "))
    
    
    # process
    total_medali1 = emas1 + perak1 +perunggu1
    total_medali2 = emas2 + perak2 +perunggu2
    if(total_medali1 > total_medali2):
        print("Peringkat",negara1,"lebih tinggi dari",negara2)
    elif(total_medali1 == total_medali2 and perunggu1 < perunggu2):
        print("Peringkat",negara1,"lebih tinggi dari",negara2)
    elif(total_medali1 < total_medali2 and perunggu1 < perunggu2):
        print("Peringkat",negara1,"lebih rendah dari",negara2)
