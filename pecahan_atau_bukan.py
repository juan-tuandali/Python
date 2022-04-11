    # Tujuan Program : Menentukan apakah hasil merupakan bilangan pecahan atau bukan
    # Kamus data :
            # pembilang = var. untuk penampung nilai pembilang dari inputan user 
            # penyebut = var. untuk penampung nilai penyebut dari inputan user 
            # pecahan = var. untuk menampung nilai dari hasil bilangan pecahan

    # input
    pembilang = int(input("Pembilang : "))
    penyebut = int(input("Penyebut : "))
    
    # process
    pecahan = 0
    
    if (pembilang % penyebut == 0):
        print(f"Bilangan bulat {pembilang // penyebut}")
    else:
        pecahan = pembilang // penyebut
        print(f"{pecahan} {pembilang % penyebut}/{penyebut}")
