# panggil module subprocess (untuk dapat execute commands windows/linux/mac)
import subprocess
# memanggil module optparse (untuk dapat menangkap argument yang dimasukkan user agar bisa digunakan dengan program)
import optparse

def getArguments():
    parser = optparse.OptionParser()  # memanggil fungsi ini agar dapat menangkap command/perintah

    # argument untuk input interface
    parser.add_option(
        "-i",  # menangkap argument/command -i (interface)
        "--interface",  # or bisa juga meggunakan --interface untuk melihat option yang ada 
        dest="interface",  # membuat var dest sebagai interface
        help="Interface to change its MAC Address"
    )

    # argument untuk input MAC Address
    parser.add_option(
        "-m",  
        "--mac", 
        dest="newMAC", 
        help="New MAC Address"
    )  

    return parser.parse_args() # untuk bisa menampilkan semua argumen yang dapat dipakai dan me-return nilai dari argument yang ada
    
# end function

# start function (fungsi mengubah MAC Address)
def changeMAC(interface, newMAC):
    print(f"[+] Changing MAC Address for {interface}")

    subprocess.call(["ifconfig", interface, "down"]) # men-disable interface
    subprocess.call(["ifconfig", interface, "hw", "ether", newMAC]) # ubah MAC sesuai yang kita mau
    subprocess.call(["ifconfig", interface, "up"]) # enable kembali interface
    subprocess.call(["ifconfig", "eth0"])
# end function

print("MAC ADDRESS BEFORE CHANGE")
subprocess.call("ifconfig eth0", shell=True)

print("-" * 60)
print()

interface = options.interface  # interface = input("Interface: ")
newMAC = options.newMAC  # newMAC = input("Enter the new MAC Address: ")
print("MAC ADDRESS AFTER CHANGE")

(options, arguments) = getArguments() # panggil function dalam variabel
changeMAC(options.interface, options.newMAC) # panggil function

