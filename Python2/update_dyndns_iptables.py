#!/usr/bin/env python2

import os
import socket

home_dyndns = "home-dyn.charlesed.net"
log_dyndns = "/tmp/home-dyn.charlesed.net.log"
local_ip = "162.211.66.2"
tcp_ports = ('22','20406')
udp_ports = ()

def updatelog(file, new_ip):
    file.write(new_ip)
    print "Log updated with new IP", new_ip
    file.close()

def updateiptables(old_dynip, new_dynip):
    print "Updating iptables..."
    for port in tcp_ports:
        os.system("iptables -D INPUT -s " + old_dynip + " -d " + local_ip + " -p tcp --dport " + port + " -j ACCEPT")
        os.system("iptables -I INPUT 2 -s " + new_dynip + " -d " + local_ip + " -p tcp --dport " + port + " -j ACCEPT")
    for udp_port in udp_ports:
        os.system("iptables -D INPUT -s " + old_dynip + " -d " + local_ip + " -p udp --dport " + port + " -j ACCEPT")
        os.system("iptables -I INPUT 2 -s " + new_dynip + " -d " + local_ip + " -p udp --dport " + port + " -j ACCEPT")
    print "iptables updated."

try:
    log = open(log_dyndns, 'r+')
except IOError:
    log = open(log_dyndns, 'w+')

last_dyndns = log.read()
cur_dyndns = socket.gethostbyname(home_dyndns)

print "Log:", last_dyndns
print "Cur:", cur_dyndns

if cur_dyndns != last_dyndns:
    updatelog(log, cur_dyndns)
    print "Log updated to new IP.", cur_dyndns
else:
    print "Adresses match, not updating log."

updateiptables(last_dyndns, cur_dyndns)
