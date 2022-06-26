import sys
import socket
from IPy import IP
import pyfiglet
from printy import printy

ascii_banner = pyfiglet.figlet_format("port_scanner")
printy(ascii_banner,'n')
ports = {21, 22, 23, 25, 53, 80, 135, 443, 445, 8000, 8080}
info = "This a basic port scanner which scan very few but popular ports and also my computer is slow to scan all 65535 ports"
usage = "Usage: python3 port_scan.py <target>,<target>,<target>.."
print(info)


if len(sys.argv) > 1:
 targets = sys.argv[1]
else:
 targets = False

if len(sys.argv) < 1 or targets == False:
 print(usage)

elif len(sys.argv) > 1 or targets != False:
 print("Port Scanner is running.Sit back, relax and wait for results..")
 def scan(target):
  converted_ip = get_ip(target)
  print("\n[-]Scanning target", str(target))
  for i in ports:
   scan_port(converted_ip, i)
 def get_banner(sock):
  return sock.recv(1024)
 
 def get_ip(ip):
  try:
   IP(ip)
   return(ip)
  except ValueError:
   return socket.gethostbyname(ip) 

 def scan_port(ipaddress, port):
  try: 
   s = socket.socket()
   s.settimeout(0.5)
   s.connect((ipaddress, port))
   try: 
    banner = get_banner(s)
    print("[+] Open Port",str(port),":",str(banner))
   except:
    print("[+] Open Port",str(port))
  except:
   pass

 if len(sys.argv) > 1:
  targets = sys.argv[1]
  if "," in targets:
   for ip in targets.split(","):
    scan(ip.strip())
  else:
   scan(targets)
