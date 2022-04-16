# Tujuan Program : Money Changer
# Kamus Data : 
#            jumlah_uang : var. input (integer)
#            jenis_mata_uang : var. input (string)
#            rupiah : parameter funct

    # Rupiah -> Dolar Singapura
def idrToSgd(rupiah):
    # process
    toSGD = rupiah / 10586
    print(f"{rupiah} Rupiah dapat menjadi {toSGD:.2f} Dolar Singapura")
    
    # Rupiah -> Bath Thailand
def idrToThb(rupiah):
    # process
    toTHB = rupiah / 429
    print(f"{rupiah} Rupiah dapat menjadi {toTHB:.2f} Bath Thailand")
    
    # Rupiah -> Ringgit Malaysia
def idrToMyr(rupiah):
    # process
    toMYR = rupiah / 3405
    print(f"{rupiah} Rupiah dapat menjadi {toMYR:.2f} Ringgit Malaysia")
        

def main():
    
    print("================= Money Changer =================")
    
    # input
    jumlah_uang = int(input("Jumlah Uang : "))
    jenis_mata_uang = str(input("Jenis Mata Uang yang ingin diktukar (SGD/THB/MYR) : "))

    # output
    print("=================================================")
    if (jenis_mata_uang == "SGD"):
        idrToSgd(jumlah_uang)
    elif (jenis_mata_uang == "THB"):
        idrToThb(jumlah_uang)
    elif (jenis_mata_uang == "MYR"):
        idrToMyr(jumlah_uang)
    else:
        print("Masukkan jenis mata uang yang benar!")
    
    
if __name__=='__main__':
    main()
