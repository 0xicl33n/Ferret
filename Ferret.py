#!/usr/bin/python2
import socket
import sys
import os
import platform
import time
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
animation = '''|/-\\'''
idx = 0
os.system('cls')
os.system('title #')

def printsign():
	print """                                        
               _....._            ,_    _,
             .-'       '.       _ /7 \--/^|
           .'            `'._.-' ;   -   _|
         _/                      '. /O\ /o/
      .-' |                '       '-._Y.'
     /__.'\  '-.         .'           /
    |__/   '-._ '-.,___,.     ,   _.-L
    \__\       `""`      `-._  \-'.__,\\
     '-.;        Ferret     '-._'.  ```                                                         
     	  Tiny socket listener
\n\n"""
printsign()
host = str(raw_input("[*] Which host we connecting?	"))
port = int(raw_input("[**] Port tho?	"))
server.bind( ( host, port ) )
server.listen( 5 )
os.system('cls')
print "\n >>  Server bound to %s:%d  << \n\n"%(host, port)
printsign()
connected = False
while connected == False:
	print "[*] Forever listening for shell...",animation[idx % len(animation)] + "\r",
	idx += 1
	time.sleep(0.1)
while 1:
	if not connected:
		(client, address) = server.accept()
		connected = True
print "[ --> ] Accepted connexion from %s"%(host)
buffer = ""
while 1:
	try:
		recv_buffer = client.recv(4096)
		print "[!!] Received: %s" %(recv_buffer)
		if not len(recv_buffer):
			break
		else:
			buffer += recv_buffer
	except:
		break
command = raw_input("[#]Enter command>	")
client.sendall( command + "\r\n\r\n")
print "[!] Sent => %s"%(command)
