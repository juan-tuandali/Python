 
    # input
    titik_x1 = int(input("Titik x1 : "))
    titik_y1 = int(input("Titik y1 : "))
    titik_x2 = int(input("Titik x2 : "))
    titik_y2 = int(input("Titik y2 : "))
    titik_acuan = int(input("Titik acuan (1/2) : "))
    
    # process
        # jika titik x1,y1 dan x2,y2 sama
    if (titik_x1 == titik_x2 and titik_y1 == titik_y2):
        print(f"Titik ({titik_x1},{titik_y1}) memiliki posisi yang sama dengan titik acuan ({titik_x2},{titik_y2})")
        
        # acuan 1
    elif (titik_acuan == 1):
        if (titik_x1 > titik_x2): # kiri
            print(f"Titik ({titik_x2},{titik_y2}) terletak disebelah kiri ",end="")
        else: # kanan
            print(f"Titik ({titik_x2},{titik_y2}) terletak disebelah kanan ",end="")
        if (titik_y1 > titik_y2): # bawah
            print(f"bawah titik acuan ({titik_x1},{titik_y1})")
        else: # atas
            print(f"atas titik acuan ({titik_x1},{titik_y1})")
            
        # acuan 2 
    elif (titik_acuan == 2):
        if (titik_x1 > titik_x2): # kanan
            print(f"Titik ({titik_x1},{titik_y1}) terletak disebelah kanan ",end="")
        else: # kiri
            print(f"Titik ({titik_x1},{titik_y1}) terletak disebelah kiri ",end="")
        if (titik_y1 > titik_y2): # atas
            print(f"atas titik acuan ({titik_x2},{titik_y2})")
        else: # bawah
            print(f"bawah titik acuan ({titik_x2},{titik_y2})")
    
