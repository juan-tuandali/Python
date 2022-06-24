# penulis : Juan Tuandali
# tujuan program : A Butterfly
# --Kamus Data--
# y : var. parameter dari input dari var. a di fungsi main (int)
# i : var. looping baris(int)
# k : var. looping tanda tambah dan spasi(int)
def kupuKupuAtas(y):
    for i in range (0,y,1):
        for k in range (0,i+1):
            print("+",end=" ")
        for k in range (0,2*(y-i)-1):
            print(" ",end=" ")
        for k in range (0,i+1):
            print("+",end=" ")
        print()

# --Kamus Data--
# x : var. parameter dari input dari var. a di fungsi main (int)
# i : var. looping tanda tambah (int)
def kupuKupuTengah(x):
    for i in range (0,2*x+1,1):
        print("+",end=" ")
    print()

# --Kamus Data--
# z : var. parameter dari input dari var. a di fungsi main (int)
# i : var. looping baris (int)
# k : var. looping tanda tambah dan spasi(int)
def kupuKupuBawah(z):
    for i in range (z-1,-1,-1):
        for k in range (0,i+1):
            print("+",end=" ")
        for k in range (0,2*(z-i)-1):
            print(" ",end=" ")
        for k in range (0,i+1):
            print("+",end=" ")
        print()

# --Kamus Data--
# a : var. input (int)
def main():
    a = int(input(""))
    kupuKupuAtas(a)
    kupuKupuTengah(a)
    kupuKupuBawah(a)
    
if __name__ == '__main__':
    main()
