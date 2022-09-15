import subprocess # panggil module subprocess (untuk dapat execute commands windows/linux/mac)
import optparse # memanggil module optparse (untuk dapat menangkap argument yang dimasukkan user agar bisa digunakan dengan program)
import re  # memanggil module Regular Expression 

# start function
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

    (options, arguments) = parser.parse_args()
    
    if not options.interface and not options.newMAC:
        parser.error("[-] Please specify an interface and new MAC, use --help or -h for more info.")  # untuk menampilkan kesalahan saat tidak ada input yang dimasukkan oleh user
    elif not options.interface:
        parser.error("[-] Please specify an interface, use --help or -h for more info.")  # untuk menampilkan kesalahan karena user tidak memasukkan interface yang dituju
    elif not options.newMAC:
        parser.error("[-] Please specify a new MAC Address, use --help or -h for more info.")  # untuk menampilkan kesalahan karena user tidak memasukkan MAC baru yang dituju
    
    return options 
# end function

# start function (fungsi mengubah MAC Address)
def changeMAC(interface, newMAC):
    print(f"[+] Changing MAC Address for {interface} to {newMAC}")

    subprocess.call(["ifconfig", interface, "down"]) # men-disable interface
    subprocess.call(["ifconfig", interface, "hw", "ether", newMAC]) # ubah MAC sesuai yang kita mau
    subprocess.call(["ifconfig", interface, "up"]) # enable kembali interface
    subprocess.call(["ifconfig", "eth0"])
    
    retrun
# end function

# start function
def get_current_mac(interface):

    #  menampilkan hasil
    ifconfig_result = subprocess.check_output(["ifconfig", interface],text=True) # untuk cek output
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result) # untuk menangkap MAC address yang baru
    # validasi
    if mac_address_search_result:
        return mac_address_search_result.group(0) # group disini mulai dari 0 sampai 3
    else:
        print("[-] Could not read MAC Address")
    
    return
# end def

# start fuction utama
def main():
      
    print("MAC ADDRESS BEFORE CHANGE")
    subprocess.call("ifconfig eth0", shell=True) # memanggil fungsi call pada module subprocess untuk menjalankan perintah/command

    print("-" * 60)
    print()

    print("MAC ADDRESS AFTER CHANGE")

    # panggil function getArguments 
    options = getArguments() 
    
    # panggil fungsi get_current_mac (before change)
    current_mac = get_current_mac(options.interface)
    print("Current MAC : (",options.interface,")", current_mac) # MAC Address sebelum diubah
    
    #panggil fungsi changeMAC
    changeMAC(options.interface, options.newMAC)
    
    # panggil fungsi get_current_mac (after change)
    current_mac = get_current_mac(options.interface) # MAC Address setelah diubah
    
    # validasi
    if current_mac == options.newMAC:
        print("[+] MAC Address was successfully changed to",current_mac)
    else:
        print("[-] MAC Address did not get changed.")
    
    return
if __name__=='__main__':
    main()
# end def

