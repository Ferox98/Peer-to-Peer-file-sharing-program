"""
Author: Kaleab Belete (ATR/3763/09) Section-02
Description: Below is a simple peer-to-peer file sharing program in which
	     one peer sends a file it has while receiving another file from
	     another peer
Usage: peer.py host_address host_port file_to_send file_to_receive
Example: peer.py '127.0.0.1' 65432 file_1.pdf file_2.pdf	
"""		

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = False

try:
	s.connect(('127.0.0.1', 65432))
except:
	# No peer willing to exchange files exists, therefore act as server
	s.bind((HOST, PORT))
	s.listen(5)
	server = true

HOST = sys.argv[1]
PORT = int(sys.argv[2])

file_send = sys.argv[3]
file_receive = sys.argv[4]

fr = open(file_receive, "wb")
fs = open(file_send, "rb")

l = fs.read(4096)
print("Sending data")
if server == False:
	while (l):
		# send data
		s.send(l)
		l = fs.read(4096)
	s.send("TRANSFER--COMPLETE--")
	# receive data from peer
	print("preparing to receive data")
	l = s.recv(4096)
	while (l):
		fr.write(l)
		l = s.recv(4096)	
	print("Transfer complete")	
else:
	conn, addr = s.accept()
	while (True):
		# receive data
		fr.write(l)
		l = conn.recv(4096)
		if("TRANSFER--COMPLETE--" in l):
			res = l.replace('TRANSFER-COMPLETE--', '')
			fr.write(res)
			break
	print("preparing to send data")
	l = fs.read(4096)
	while(l):
		conn.send(l)
		l = fs.read(4096)
	print("Transfer complete")

fr.close()
fs.close()
	

