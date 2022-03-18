# Membuat program pendeteksi hari lahir

print("")
print("\tPENDETEKSI HARI LAHIR\n")
a = "y"
while (a != "g"):
        import datetime as dt
        tanggal = int(input("\tTanggal (1 sd 31) \t         : "))
        bulan = int(input("\tBulan (1 sd 12) \t         : "))
        tahun = int(input("\tTahun (1000 sd tahun sekarang)   : "))

        print("")
        tgl_lahir = dt.date(tahun,bulan,tanggal)
        print("\t+----------------------------------------------------------------------")
        print(f"\t+  Tanggal lahir anda   : {tgl_lahir}")
        print(f"\t+  Anda lahir pada hari : {tgl_lahir:%A}")
        hari_ini = dt.date.today()
        umur = hari_ini
        hidup_selama = hari_ini - tgl_lahir
        umur = hidup_selama.days // 365
        print(f"\t+  Anda sudah hidup selama {hidup_selama.days} hari di dunia,")
        print(f"\t+  atau anda berumur {umur} tahun")
        print("\t+----------------------------------------------------------------------\n")
        
        a = input("\tLagi (y/g) ? ")
