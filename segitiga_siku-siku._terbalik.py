# input
angka = int(input())
    
# process
for i in range(angka,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
