######################################
# IP ID ISN Server 
######################################
from scapy.all import *
from struct import pack

print "[*] Sniffing Started..."
packets = sniff( iface = 'lo', timeout=10)
print "[*] Sniffing Stopped..."

print "[*]Packets captured..."
print packets
packets = packets[::2]


payload = ''.join( [ pack('<HI',packet.id, packet.seq) for packet in packets ] )
print "[*]Captured Payload..."
print payload

print "[*]Hexdump of captured traffic..."
for packet in packets:
	print hexdump(packet)
