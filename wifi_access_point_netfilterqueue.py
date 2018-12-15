from scapy.all import *
from netfilterqueue import NetfilterQueue
from struct import unpack

# To use netfilterqueue as a reverse proxy
iptablesr = "iptables -A OUTPUT -j NFQUEUE --queue-num 0"

print("[*] Adding iptables rule.......")
print(iptablesr)
os.system(iptablesr)

def modify(packet):
    #converts the raw packet to a scapy compatible string
    pkt = IP(packet.get_payload())
    #print(pkt)

    print("Got a packet ! source ip : " + str(pkt.src) + str(pkt.id))
    id_payload = "aa"
    a = unpack("<H",id_payload)[0]
    # 192.168.136.182 is the IP address of the Wi-Fi access point
    if pkt.src == "192.168.136.182" :
    	pkt.id = a

    #Set the packet content to modified modified version
    packet.set_payload(str(pkt))
    print("Sent a packet ! source ip : " + str(pkt.src) + str(pkt.id))

    packet.accept() #accept the packet



nfqueue = NetfilterQueue()
#1 is the iptabels rule queue number, modify is the callback function
nfqueue.bind(0, modify) 
try:
    print "[*] waiting for data"
    nfqueue.run()
except KeyboardInterrupt:
    pass
    os.system('iptables -F')
    os.system('iptables -X')
