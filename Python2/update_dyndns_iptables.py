#!/usr/bin/env python2

import os
import socket

dyndns_host = ""
dyndns_log = "/tmp/dynip.log"
local_ip = ""
tcp_ports = ('22',)
udp_ports = ()

def updatelog(file, new_ip):
    file.write(new_ip)
    print "Log updated with new IP", new_ip
    file.close()

def updateiptables(old_ip, new_ip):
    print "Updating iptables..."
    for tcp_port in tcp_ports:
        os.system("iptables -D INPUT -s " + old_ip + " -d " + local_ip + " -p tcp --dport " + tcp_port + " -j ACCEPT")
        os.system("iptables -I INPUT 2 -s " + new_ip + " -d " + local_ip + " -p tcp --dport " + tcp_port + " -j ACCEPT")
    for udp_port in udp_ports:
        os.system("iptables -D INPUT -s " + old_ip + " -d " + local_ip + " -p udp --dport " + udp_port + " -j ACCEPT")
        os.system("iptables -I INPUT 2 -s " + new_ip + " -d " + local_ip + " -p udp --dport " + udp_port + " -j ACCEPT")
    print "iptables updated."

try:
    log = open(dyndns_log, 'r+')
except IOError:
    log = open(dyndns_log, 'w+')

dynip_pre = log.read()
dynip_cur = socket.gethostbyname(dyndns_host)

print "Log:", dynip_pre
print "Cur:", dynip_cur

if dynip_cur != dynip_pre:
    updatelog(log, dynip_cur)
else:
    print "Adresses match, not updating log."

updateiptables(dynip_pre, dynip_cur)
