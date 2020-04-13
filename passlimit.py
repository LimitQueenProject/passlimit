#!/usr/bin/python

import os
import sys
import time

def jalankan_ulang_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()

def bersih_layar():
	if sys.platform == "linux2":
		os.system("clear")
	elif sys.platform == "win32":
		os.system("cls")
	else:
		os.system("clear")

bersih_layar()

print ("\33[36;1m _          _    _ _        _ _    _    _ _ _ _ _ _                                                ")
print ("\33[36;1m|||        |||  |||||      |||||  |||  |||||||||||||   ||||||||                                    ")                                   
print ("\33[36;1m|||        |||  ||||||    ||||||  |||       |||        ||    ||                                    ")
print ("\33[36;1m|||        |||  ||| |||  ||| |||  |||       |||        ||    || ||    || |||||| |||||\\  |||||\\   ")       
print ("\33[36;1m|||        |||  |||  ||||||  |||  |||       |||        |||||||| ||    || ||     ||    || ||    ||  ")     
print ("\33[36;1m|||        |||  |||   ||||   |||  |||       |||              || ||    || |||||  ||    || ||    ||  ")        
print ("\33[36;1m|||||||||  |||  |||    ||    |||  |||       |||              || ||    || ||     ||    || ||    ||  ")                                 
print ("\33[36;1m+++++++++++++++Code By Limit Queen Propject                  || |||||||| |||||| ||    || ||    ||  ")   
print ("")

print '\033[0;32mketikan "EXECUTION" untuk konfirmasi\033[0m'
print

interpreter='*>'
if os.geteuid()==0:
	interpreter='#>'

EXECUTION="""\033[0;36m
TOOLS INI DIBUAT
SEMATA-MATA HANYA UNTUK
PEMBELAJARAN, BUKAN UNTUK TINDAKAN
KRIMINAL ATAU MENCARI
KEUNTUNGAN.
SAYA TIDAK BERTANGGUNG JAWAB
ATAS MASALAH APAPUN YG
TERJADI NANTINYA AKIBAT DARI
AKSI ANDA DALAM MENGGUNAKAN
TOOLS INI. Terima
Kasih.
ingat gunakan tools ini dengan bijak!

<=========================>
	clear     clean the screen
	attack    start execution
	refresh   refresh the program
	exit      to exit the program
<=========================>\033[0m
"""

opt=True
while opt:
	wgen=raw_input('\033[0;31mMULAI' + interpreter + ' ')
	if wgen == 'EXECUTION':
		print EXECUTION
	elif wgen == 'clear':
		bersih_layar()
	elif wgen == 'attack':
		try:
			a=raw_input("\nNAME?> fill in: ")
			file=open(""+a+".txt", 'w')
			b=raw_input("NAME?> fill in: ")
			c=raw_input("NAME?> fill in: ")
			d=raw_input("NAME?> fill in: ")
			e=raw_input("NAME?> number: ")
			f=e[0:2]
			g=e[2:4]
			h=e[4:]
			i=raw_input("\nNAME?> fill in: ")
			j=raw_input("NAME?> fill in: ")
			k=raw_input("NAME?> fill in: ")
			l=k[0:2]
			m=k[2:4]
			n=k[4:]
			file.write("%s%s\n%s%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s" % (a,c,a,b,b,a,b,c,c,a,c,b,a,a,b,b,c,c,a,d,b,d,c,d,d,d,d,a,d,b,d,c,a,e,a,f,a,g,a,h,b,e,b,f,b,g,b,h,c,e,c,f,c,g,c,h,d,e,d,f,d,g,d,h,e,a,f,a,g,a,h,a,e,b,f,b,g,b,h,b,e,c,f,c,g,c,h,c,e,d,f,d,g,d,h,d,d,d,a,f,g,a,g,h,f,g,f,h,f,f,g,f,g,h,g,g,h,f,h,g,h,h,h,g,f,a,g,h,b,f,g,b,g,h,c,f,g,c,g,h,d,f,g,d,g,h,a,i,a,j,a,k,i,e,i,j,i,k,b,i,b,j,b,k,c,i,c,j,c,k,e,k,j,a,j,b,j,c,j,d,j,j,k,a,k,b,k,c,k,d,k,k,i,l,i,m,i,n,j,l,j,m,j,n,j,k))
			wg = 0
			while (wg < 100):
				wg = wg + 1
				file.write(a + str(wg) + '\n')
			en = 0
			while (en < 100):
				en = en + 1
				file.write(i + str(en) + '\n')
			word = 0
			while (word < 100):
				word = word + 1
				file.write(d + str(word) + '\n')
			gen = 0
			while (gen < 100):
				gen = gen + 1
				file.write(j + str(gen) + '\n')
			file.close()
			time.sleep(1.5)
			print " \n[+] wordlist is ready to use %s.txt\n" %a
		except IOError, e:
			print(" \n[!] ERROR: %s\n" %e)
	elif wgen == 'ulang':
		jalankan_ulang_program()
	elif wgen == 'keluar':
		print "\033[0m"
		opt=False