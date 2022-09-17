import scapy.all as scapy # memanggil module scapy untuk dapat melakukan scanning paket jaringan
import argparse as arg

# start fucntion
def get_arguments():
    parser = arg.ArgumentParser()  # memanggil fungsi ini agar dapat menangkap command/perintah
    # argument untuk input
    parser.add_argument(
        "-t",  # menangkap argument/command -t (target)
        "--target",  # or bisa juga meggunakan --target  
        dest="target",  # membuat var dest sebagai gateway
        help="Target IP Address or range IP Address")
    (options, arguments) = parser.parse_args()
    
    if not options.target:
        parser.error("[-] Please specify an IP Address or range IP Address")  # untuk menampilkan kesalahan saat tidak ada input yang dimasukkan oleh user
    
    return options 
# end def
# start function
def scan(ip):
    print("-"*50)
    
    # memanggil fungsi .ARP untuk kita menjalankan request arp pada jaringan yang dituju
    arp_request = scapy.ARP(pdst=ip)  # pdst adalah fungsi dalam scapy.ARP untuk menambahkan ip address
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") # memberikan MAC Address yang dituju
    arp_request_broadcast = broadcast/arp_request # membuat variabel untuk mengkombinasi arp_request dan broadcast
    
    print(arp_request_broadcast.summary()) # .summary artinya meringkas hasil object (packet) dari hasil program kita
    
    print("-"*50)
    
    answered_list = scapy.srp(arp_request_broadcast, timeout=2, verbose=False)[0] # memanggil fungsi .sr (send /recieved) untuk mengirim / menerima packet data
    
    clients_list = [] # membuat list kosong untuk nantinya menampung dictionary yang kita buat
    for element in answered_list: # default nya data/packet adalah dalam sebuah list pada
        clients_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc} # membuat variabel baru dengan type dictionary
        clients_list.append(clients_dict) # menambahkan dictionary ke list
        
    return clients_list
# end def
# start function
def print_result(result_list):
    for client in result_list:
        print("IP: ", end="")
        print(client["ip"]) # karena sudah berbentuk dictionary, maka kita dapat memanggilnya dengan key bukan index
        print("MAC Address: ", end="")
        print(client["mac"]) # karena sudah berbentuk dictionary, maka kita dapat memanggilnya dengan key bukan index
        print("-"*30)
# end def

# start function utama
def main():
    options = get_arguments()
    scan_result = scan(options.target) 
    print_result(scan_result)
    
    return
if __name__=='__main__':
    main()
# end def
