import argparse
import configparser
import json
import subprocess
import os
import sys
import paramiko
from scp import SCPClient
import time as timer


def createSSHClient(server, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    if password.split(".")[1] == "pem":
        client.connect(server,username='ec2-user', key_filename=password)
    elif password.split(".")[1] == "johnny":
        client.connect(server,username='johnny')
    else:
        client.connect(server,username='xiang')
    client_scp = SCPClient(client.get_transport())
    return client_scp, client


scp_list_1=[]
ssh_list_1=[]
scp_list_2=[]
ssh_list_2=[]

server_list1=[("128.46.74.171",".xiang"),("128.46.74.172",".xiang"),("128.46.74.173",".xiang"),("128.46.74.95",".xiang")]
server_list2=[("128.46.32.175",".johnny")]
#server_list1=[("128.46.74.95",".xiang")]
for each in server_list1:
    scp,ssh = createSSHClient(each[0],each[1])
    scp_list_1.append(scp)
    ssh_list_1.append(ssh)

print(ssh_list_1)

for each in ssh_list_1:
    each.exec_command("source ~/.bashrc")
    time.sleep(2)
    each.exec_command("python /home/xiang/mtec/governer.py")

for each in server_list2:
    scp,ssh = createSSHClient(each[0],each[1])
    scp_list_2.append(scp)
    ssh_list_2.append(ssh)

# client = paramiko.SSHClient()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client_scp = SCPClient(client.get_transport())
for each in ssh_list_2:
    each.exec_command("source ~/.bashrc")
    time.sleep(2)
    each.exec_command("python /home/johnny/metc/governer.py")