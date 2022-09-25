import netfilterqueue # panggil module metfilterqueue

# start def
def process_packet(packet): # fungsi untuk proses paket kedalam queue
    print(packet)
    packet.accept() # untuk menerima / meneruskan paket ke komputer korban
    # packet.drop() # sebaliknya, dengan drop kita tidak akan meneruskan paket ke komputer korban, tetapi hanya pada komputer kita
    
    return
# end def

queue = netfilterqueue.NetfilterQueue() # membuat var queue yang dimana supaya kita mendapat akses ke packet yang sesuai dengan iptables.
queue.bind(0, process_packet) # panggil fungsi bind untuk dapat menargetkan pada queue_number mana yang dituju
queue.run() # run queue
