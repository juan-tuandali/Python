# panggil module subprocess (untuk dapat execute commands windows/linux/mac)
import subprocess
# memanggil module optparse (untuk dapat menangkap argument yang dimasukkan user agar bisa digunakan dengan program)
import optparse

# start function (fungsi mengubah MAC Address)
def changeMAC(interface, newMAC):
    print(f"[+] Changing MAC Address for {interface}")

    subprocess.call(["ifconfig", interface, "down"]) # men-disable interface
    subprocess.call(["ifconfig", interface, "hw", "ether", newMAC]) # ubah MAC sesuai yang kita mau
    subprocess.call(["ifconfig", interface, "up"]) # enable kembali interface
    subprocess.call(["ifconfig", "eth0"])
# end function

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

(options, argument) = parser.parse_args()  # untuk menangkap value dari argument yang dinput
print("MAC ADDRESS BEFORE CHANGE")
subprocess.call("ifconfig eth0", shell=True)

print("-" * 60)
print()

interface = options.interface  # interface = input("Interface: ")
newMAC = options.newMAC  # newMAC = input("Enter the new MAC Address: ")
print("MAC ADDRESS AFTER CHANGE")

changeMAC(interface, newMAC)  # panggil function
