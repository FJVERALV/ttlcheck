#!/usr/bin/python3
#coding: utf-8

import re, sys, subprocess
import socket

entrada1 = sys.argv[1]

try:
    socket.inet_aton(entrada1)

    
except socket.error:
      print("\n[!] Uso: python3 " + "ttlcheck.py" + " <dirección-ip>\n")
      sys.exit(1)

def get_ttl(ip_address):

    proc = subprocess.Popen(["/usr/bin/ping -c 1 %s" % ip_address, ""], stdout=subprocess.PIPE, shell=True)
    (out,err) = proc.communicate()

    out= out.split()
    out = out[12].decode('utf-8')

    ttl_value = re.findall(r"\d{1,3}", out)[0]

    return ttl_value

def get_os(ttl):

    ttl = int(ttl)
    if ttl >= 2 and ttl <= 32:
        return "Windows 95/98/ME"
    elif ttl >= 33 and ttl <= 64:
        return "Linux/FreeBSD/MacOSX"
    elif ttl >= 65 and ttl <= 128:
        return "Windows"
    elif ttl >= 129 and ttl <= 254:
        return "Solaris"
    else:
        return "No Encontrado."

if __name__ == '__main__':

    ip_address = entrada1

    ttl = get_ttl(ip_address)

    os = get_os(ttl)

    print("%s (ttl -> %s): %s" % (ip_address, ttl, os))
