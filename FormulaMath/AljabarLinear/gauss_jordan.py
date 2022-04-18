"""
===Formula Aljabar Linear===
Tujuan Program => Sistem Persamaan Linear (SPL) -> Eliminasi (Gauss Jordan) 3x3 & 4x4
--Kamus Data-- :
ordo -> var input(string)
pers1_x -> var input(int)
pers1_y -> var input(int)
pers1_z -> var input(int)
pers1_hasil1 -> var input(int)
pers2_x -> var input(int)
pers2_y -> var input(int)
pers2_z -> var input(int)
pers2_hasil2 -> var input(int)
pers3_x -> var input(int)
pers3_y -> var input(int)
pers3_z -> var input(int)
pers3_hasil3 -> var input(int)
pers1_x_new -> var penampung nilai pers1 x yang baru
pers1_y_new -> var penampung nilai pers1 y yang baru
pers1_z_new -> var penampung nilai pers1 z yang baru
pers1_hasil1_new -> var penampung nilai pers1 hasil1 yang baru
pers2_x_new -> var penampung nilai pers2 x yang baru
pers2_y_new -> var penampung nilai pers2 y yang baru
pers2_z_new -> var penampung nilai pers2 z yang baru
pers2_hasil2_new -> var penampung nilai pers2 hasil2 yang baru
pers3_x_new -> var penampung nilai pers3 x yang baru
pers3_y_new -> var penampung nilai pers3 y yang baru
pers3_z_new -> var penampung nilai pers3 z yang baru
pers3_hasil3_new -> var penampung nilai pers3 hasil3 yang baru
"""

print("\nNote : Masukkan persamaan contohnya : poersamaan1 (x) = 5, persamaan1 (y) = 5, persamaan1 (z) = 10, persamaan hasil = 45. maka hasil yang dicetak akan seperti ini: 5x + 5y + 10z = 45")
# input
ordo = str(input("\nJumlah ordo yang mau di hitung (3/4) : "))
print("=====================================")

# process
if (ordo == "3"):
    
    # Perasamaan 1
    print("---Persamaan 1---")
    pers1_x = int(input("Persamaan1 (x) : "))
    pers1_y = int(input("Persamaan1 (y) : "))
    pers1_z = int(input("Persamaan1 (z) : "))
    pers1_hasil1 = int(input("Persamaan1 (=) : "))
    # # Perasamaan 2
    print("---Persamaan 2---")
    pers2_x = int(input("Persamaan2 (x) : "))
    pers2_y = int(input("Persamaan2 (y) : "))
    pers2_z = int(input("Persamaan2 (z) : "))
    pers2_hasil2 = int(input("Persamaan2 (=) : "))
    # # Perasamaan 3
    print("---Persamaan 3---")
    pers3_x = int(input("Persamaan3 (x) : "))
    pers3_y = int(input("Persamaan3 (y) : "))
    pers3_z = int(input("Persamaan3 (z) : "))
    pers3_hasil3 = int(input("Persamaan3 (=) : "))
    # output1
    print("=====================================")
    print(f"SPL :\n{pers1_x}x + {pers1_y}y + {pers1_z}z = {pers1_hasil1}")
    print(f"{pers2_x}x + {pers2_y}y + {pers2_z}z = {pers2_hasil2}")
    print(f"{pers3_x}x + {pers3_y}y + {pers3_z}z = {pers3_hasil3}")
    print("=====================================")
    # process elimination
    print(f"Bentuk dalam Matriks mula-mula :")
    # bagian baris 1 
    print(f"{pers1_x}  {pers1_y}  {pers1_z}  {pers1_hasil1}")
    print(f"{pers2_x}  {pers2_y}  {pers2_z}  {pers2_hasil2}")
    print(f"{pers3_x}  {pers3_y}  {pers3_z}  {pers3_hasil3}")
    print("=====================================")
    if (pers1_x == 1):
        # new Matriks1
        print("Matriks baru1 :")
        # jadikan pers2(x) dan pers3(x) = 0
        pers2_x_new1 = pers2_x + ((pers2_x * (-1)) * pers1_x )
        pers2_y_new1 = pers2_y + ((pers2_x * (-1)) * pers1_y )
        pers2_z_new1 = pers2_z + ((pers2_x * (-1)) * pers1_z )
        pers2_hasil2_new1 = pers2_hasil2 + ((pers2_x * (-1)) * pers1_hasil1 )
        pers3_x_new1 = pers3_x + ((pers3_x * (-1)) * pers1_x )
        pers3_y_new1 = pers3_y + ((pers3_x * (-1)) * pers1_y )
        pers3_z_new1 = pers3_z + ((pers3_x * (-1)) * pers1_z )
        pers3_hasil3_new1 = pers3_hasil3 + ((pers3_x * (-1)) * pers1_hasil1 )
        # output1
        print(f"{pers1_x}  {pers1_y}  {pers1_z}  {pers1_hasil1}")
        print(f"{pers2_x_new1}  {pers2_y_new1}  {pers2_z_new1}  {pers2_hasil2_new1}")
        print(f"{pers3_x_new1}  {pers3_y_new1}  {pers3_z_new1}  {pers3_hasil3_new1}")
        print("=====================================")
        if (pers2_y_new1 != 0):
            print("Matriks baru2 :")
            # jadikan pers2(y) leading 1
            pers2_x_new2 = (pers2_x_new1 * 1)/pers2_y_new1
            pers2_y_new2 = (pers2_y_new1 * 1)/pers2_y_new1
            pers2_z_new2 = (pers2_z_new1 * 1)/pers2_y_new1 
            pers2_hasil2_new2 = pers2_hasil2_new1 * 1/pers2_y_new1
            # jadikan pers1(y) = 0
            pers1_x_new1 = pers1_x + ((pers1_y * (-1)) * pers2_x_new2)
            pers1_y_new1 = pers1_y + ((pers1_y * (-1)) * pers2_y_new2)
            pers1_z_new1 = pers1_z + ((pers1_y * (-1)) * pers2_z_new2)
            pers1_hasil1_new1 = pers1_hasil1 + ((pers1_y * (-1)) * pers2_hasil2_new2)
            # jadikan pers3(y) = 0
            pers3_x_new2 = pers3_x_new1 + ((pers3_y_new1 * (-1)) * pers2_x_new2)
            pers3_y_new2 = pers3_y_new1 + ((pers3_y_new1 * (-1)) * pers2_y_new2)
            pers3_z_new2 = pers3_z_new1 + ((pers3_y_new1 * (-1)) * pers2_z_new2)
            pers3_hasil3_new2 = pers3_hasil3_new1 + ((pers3_y_new1 * (-1)) * pers2_hasil2_new2)
            # output2
            print(f"{pers1_x_new1}  {pers1_y_new1}  {pers1_z_new1}  {pers1_hasil1_new1}")
            print(f"{pers2_x_new2}  {pers2_y_new2}  {pers2_z_new2}  {pers2_hasil2_new2}")
            print(f"{pers3_x_new2}  {pers3_y_new2}  {pers3_z_new2}  {pers3_hasil3_new2}")
            print("=====================================")
            print("Matriks baru3 :")
            if (pers3_z_new2 != 0):
                # jadikan pers3(z) leading 1
                pers3_x_new3 = (pers3_x_new2 * 1)/pers3_z_new2
                pers3_y_new3 = (pers3_y_new2 * 1)/pers3_z_new2
                pers3_z_new3 = (pers3_z_new2 * 1)/pers3_z_new2 
                pers3_hasil3_new3 = pers3_hasil3_new2 * 1/pers3_z_new2
                # jadikan pers1(z) = 0
                pers1_x_new2 = pers1_x_new1 + ((pers1_z_new1 * (-1)) * pers3_x_new3)
                pers1_y_new2 = pers1_y_new1 + ((pers1_z_new1 * (-1)) * pers3_y_new3)
                pers1_z_new2 = pers1_z_new1 + ((pers1_z_new1 * (-1)) * pers3_z_new3)
                pers1_hasil1_new2 = pers1_hasil1_new1 + ((pers1_z_new1 * (-1)) * pers3_hasil3_new3)
                # jadikan pers2(z) = 0
                pers2_x_new3 = pers2_x_new2 + ((pers2_z_new2 * (-1)) * pers3_x_new3)
                pers2_y_new3 = pers2_y_new2 + ((pers2_z_new2 * (-1)) * pers3_y_new3)
                pers2_z_new3 = pers2_z_new2 + ((pers2_z_new2 * (-1)) * pers3_z_new3)
                pers2_hasil2_new3 = pers2_hasil2_new2 + ((pers2_z_new2 * (-1)) * pers3_hasil3_new3)
                # output3
                print(f"{pers1_x_new2}  {pers1_y_new2}  {pers1_z_new2}  {pers1_hasil1_new2}")
                print(f"{pers2_x_new3}  {pers2_y_new3}  {pers2_z_new3}  {pers2_hasil2_new3}")
                print(f"{pers3_x_new3}  {pers3_y_new3}  {pers3_z_new3}  {pers3_hasil3_new3}")
                print("=====================================")
        
        else:
            pass
            
    else:
        print("Matriks baru1 :")
        # leading 1 pers1 (x)
        pers1_x_new1 = pers1_x * 1/pers1_x
        pers1_y_new1 = pers1_y * 1/pers1_x
        pers1_z_new1 = pers1_z * 1/pers1_x
        pers1_hasil1_new1 = pers1_hasil1 * 1/pers1_x
        # jadikan pers2_x = 0
        pers2_x_new1 = pers2_x + ((pers2_x * (-1)) * pers1_x_new1)
        pers2_y_new1 = pers2_y + ((pers2_x * (-1)) * pers1_y_new1)
        pers2_z_new1 = pers2_z + ((pers2_x * (-1)) * pers1_z_new1)
        pers2_hasil2_new1 = pers2_hasil2 + ((pers2_x * (-1)) * pers1_hasil1_new1)
        # jadikan pers3_x = 0
        pers3_x_new1 = pers3_x + ((pers3_x * (-1)) * pers1_x_new1)
        pers3_y_new1 = pers3_y + ((pers3_x * (-1)) * pers1_y_new1)
        pers3_z_new1 = pers3_z + ((pers3_x * (-1)) * pers1_z_new1)
        pers3_hasil3_new1 = pers3_hasil3 + ((pers3_x * (-1)) * pers1_hasil1_new1)
        # output1
        print(f"{pers1_x_new1}  {pers1_y_new1}  {pers1_z_new1}  {pers1_hasil1_new1}")
        print(f"{pers2_x_new1}  {pers2_y_new1}  {pers2_z_new1}  {pers2_hasil2_new1}")
        print(f"{pers3_x_new1}  {pers3_y_new1}  {pers3_z_new1}  {pers3_hasil3_new1}")
        print("=====================================")
        if pers2_y_new1 != 0:
            print("Matriks baru2 :")
            # jadikan pers2(y) leading 1
            pers2_x_new2 = (pers2_x_new1 * 1)/pers2_y_new1
            pers2_y_new2 = (pers2_y_new1 * 1)/pers2_y_new1
            pers2_z_new2 = (pers2_z_new1 * 1)/pers2_y_new1 
            pers2_hasil2_new2 = pers2_hasil2_new1 * 1/pers2_y_new1
            # jadikan pers1(y) = 0
            pers1_x_new2 = pers1_x_new1 + ((pers1_y_new1 * (-1)) * pers2_x_new2)
            pers1_y_new2 = pers1_y_new1 + ((pers1_y_new1 * (-1)) * pers2_y_new2)
            pers1_z_new2 = pers1_z_new1 + ((pers1_y_new1 * (-1)) * pers2_z_new2)
            pers1_hasil1_new2 = pers1_hasil1_new1 + ((pers1_y_new1 * (-1)) * pers2_hasil2_new2)
            # jadikan pers3(y) = 0
            pers3_x_new2 = pers3_x_new1 + ((pers3_y_new1 * (-1)) * pers2_x_new2)
            pers3_y_new2 = pers3_y_new1 + ((pers3_y_new1 * (-1)) * pers2_y_new2)
            pers3_z_new2 = pers3_z_new1 + ((pers3_y_new1 * (-1)) * pers2_z_new2)
            pers3_hasil3_new2 = pers3_hasil3_new1 + ((pers3_y_new1 * (-1)) * pers2_hasil2_new2)
            # output2
            print(f"{pers1_x_new2}  {pers1_y_new2}  {pers1_z_new2}  {pers1_hasil1_new2}")
            print(f"{pers2_x_new2}  {pers2_y_new2}  {pers2_z_new2}  {pers2_hasil2_new2}")
            print(f"{pers3_x_new2}  {pers3_y_new2}  {pers3_z_new2}  {pers3_hasil3_new2}")
            print("=====================================")
            print("Matriks baru3 :")
            if (pers3_z_new2 != 0):
                # jadikan pers3(z) leading 1
                pers3_x_new3 = (pers3_x_new2 * 1)/pers3_z_new2
                pers3_y_new3 = (pers3_y_new2 * 1)/pers3_z_new2
                pers3_z_new3 = (pers3_z_new2 * 1)/pers3_z_new2 
                pers3_hasil3_new3 = pers3_hasil3_new2 * 1/pers3_z_new2
                # jadikan pers1(z) = 0
                pers1_x_new3 = pers1_x_new2 + ((pers1_z_new2 * (-1)) * pers3_x_new3)
                pers1_y_new3 = pers1_y_new2 + ((pers1_z_new2 * (-1)) * pers3_y_new3)
                pers1_z_new3 = pers1_z_new2 + ((pers1_z_new2 * (-1)) * pers3_z_new3)
                pers1_hasil1_new3 = pers1_hasil1_new2 + ((pers1_z_new2 * (-1)) * pers3_hasil3_new3)
                # jadikan pers2(z) = 0
                pers2_x_new3 = pers2_x_new2 + ((pers2_z_new2 * (-1)) * pers3_x_new3)
                pers2_y_new3 = pers2_y_new2 + ((pers2_z_new2 * (-1)) * pers3_y_new3)
                pers2_z_new3 = pers2_z_new2 + ((pers2_z_new2 * (-1)) * pers3_z_new3)
                pers2_hasil2_new3 = pers2_hasil2_new2 + ((pers2_z_new2 * (-1)) * pers3_hasil3_new3)
                # output3
                print(f"{pers1_x_new3}  {pers1_y_new3}  {pers1_z_new3}  {pers1_hasil1_new3}")
                print(f"{pers2_x_new3}  {pers2_y_new3}  {pers2_z_new3}  {pers2_hasil2_new3}")
                print(f"{pers3_x_new3}  {pers3_y_new3}  {pers3_z_new3}  {pers3_hasil3_new3}")
                print("=====================================")
                print(f"Solusi dari persamaan linear :\n{pers1_x}x + {pers1_y}y + {pers1_z}z = {pers1_hasil1}\n{pers2_x}x + {pers2_y}y + {pers2_z}z = {pers2_hasil2}\n{pers3_x}x + {pers3_y}y + {pers3_z}z = {pers3_hasil3}\nsolusi => x = {pers1_hasil1_new3}, y = {pers2_hasil2_new3}, z = {pers3_hasil3_new3}")
            else:
                pass
            
        else:
            pass
        
else:
    print("Masukkan Matriks dengan ordo 3x3 / 4x4!")
