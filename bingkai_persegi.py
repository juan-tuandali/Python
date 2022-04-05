# tujuan program : latihan membuat fungsi -> membuat bingkai persegi
# fungsi menu
def menu():
    print("Program membuat kotak")
    print("Selamat mencoba")
    print("Silakan masukan karakter dan integer !") 

# fungsi keluaran
def keluaran(n, c):
    # kamus data lokal : n = parameter1 fungsi
    #                    c = parameter2 fungsi
    #                    i = var1. counter pengulangan
    #                    j = var2. counter pengulangan
    for i in range(1,n+1,1):
        for j in range(1,n+1,1):
            if(i==1)or(j==1)or(i==n)or(j==n):
                print(c,end=" ")
            else:
                print(" ",end=" ")
        print()
        
# fungsi input karakter
def inputKar():
    # kamus data lokal : c = var untuk inputan karakter (string)

    # input karakter
    c = str(input("masukan satu karakter :"))
    
    return c

# fungsi input integer
def inputInt():
    # kamus data lokal : n = var untuk inputan nilai (integer)

    # input integer
    n = int(input("masukan nilai integer :"))
    while(n <= 0): 
        n = int(input("masukan nilai integer : "))
        
    return n

# fungsi utama
def main():
    
    # meanggil fungsi
    menu()
    c = inputKar()
    n = inputInt()
    keluaran(n,c)
    
    return 0
if __name__=='__main__':
    main()
