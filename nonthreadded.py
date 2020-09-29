#!/usr/bin/env python3
from __future__ import print_function
import logging
import sys, os, time
from netmiko import ConnectHandler
from netmiko import Netmiko


"""
This is a way to SSH into a list of devices. The script will read a "hosts_file" and split
the IPs or FQDNs line by line. This is not threaded so it will do one device at a time. 
There is no error handling in this code. 
"""

#Logger to check for any errors on script. It creates a test.log file in the same directory.
logging.basicConfig(filename="test.log", level=logging.DEBUG)
logger = logging.getLogger("netmiko")


#this is not used. It allows to read a list of commands from a file.
#with open('commands_file') as f:
#    commands_list = f.read().splitlines()
#commands = commands_list


with open('host_file') as f:
    hosts_list = f.read().splitlines()


#Creates a border for better separation.
def boarder():
    print('+'*60)
    print('\n')

username = 'supersecureusername'
password = 'supersecurepassword'
os = 'juniper_junos'


boarder()
for host in hosts_list:
    print(host)
    device = Netmiko(device_type=os, ip=host, username=username, password=password)
    output = device.send_command('show ethernet-switching table | match xx:xx:xx:xx', delay_factor=5)
    #output = device.send_command_expect("show ethernet-switching table | match 24:db:ad")
    print(output)
    print(host,output, file=open("output.txt", "a"))
    device.disconnect()
    boarder()

exit()

#Code to just do one device. 
# core = {
 #       'host': '0.0.0.0',
  #  'username': 'supersecureusername',
   # 'password': 'supersecurepassword',
   # 'device_type': 'juniper_junos',
   # }

#seperator()
#net_connect = Netmiko(**core)
#output = net_connect.send_command("show system uptime | match up")
#print(output, file=open("output.txt", "a"))
