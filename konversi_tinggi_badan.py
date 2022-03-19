   # input
    nama = str(input("Nama : "))
    tinggi = float(input("Tinggi (cm) : "))
    
    # process
    cm = tinggi
    meter = cm * 1/100
    desi = cm * 1/10
    inci =  cm / 2.54
    
    # output
    print(f"Tinggi badan {nama} adalah {meter} meter atau {desi} dm atau {inci:.2f} inci") # untuk syntax inci:.2f artinya akan mengambil 2 angka dibelakang koma dari hasil yang didapat.
