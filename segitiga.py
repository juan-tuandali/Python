# input
angka = int(input())
    
# process
for i in range(1,angka+1):
    print(" "*(angka-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
