def main():
    
    # input
    pembilang = int(input("Pembilang : "))
    penyebut = int(input("Penyebut : "))
    
    pecahan = 0
    
    # process
    if (pembilang % penyebut == 0):
        print(f"Bilangan bulat : {pembilang // penyebut}")
    else:
        pecahan = pembilang // penyebut
        print(f"Bilangan pecahan : {pecahan} {pembilang % penyebut}/{penyebut}")
    
    return 0

if __name__ == '__main__':
    main()
