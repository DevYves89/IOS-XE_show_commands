#!/usr/bin/env python3
import paramiko
import time
import argparse
import re



parser = argparse.ArgumentParser("simple_example")
parser.add_argument("device_ip", help="An integer will be increased by 1 and printed.")
parser.add_argument("username", help="An integer will be increased by 1 and printed.")
parser.add_argument("password", help="An integer will be increased by 1 and printed.")
parser.add_argument("show_cmd", help="An integer will be increased by 1 and printed.")
parser.add_argument("regex", help="An integer will be increased by 1 and printed.")
args = parser.parse_args()

device_ip = args.device_ip
username = args.username
password = args.password
show_cmd = args.show_cmd
regex = args.regex




#print("debug: " + device_ip)
#print("debug: " + username)
#print("debug: " + password)
#print("debug: " + regex)

#print('Connecting to: ', device_ip)
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=device_ip,
               username=username,
               password=password,
               pkey=None,
               look_for_keys=False)
#print('\nExecuting command...')

remote_conn = client.invoke_shell()
remote_conn.send(show_cmd+"\n")
time.sleep(2)

#print('\n -------------- Print --------------')
output = remote_conn.recv(999999)
#print(output.decode())
#print('\n -------------- Print --------------')

#print("debug: " + output.decode())

regex2 = re.findall(regex,output.decode())
#"Version (\d\d.\d\d.\d\d.)"
print(regex2[0])
exit(0)

print('\nTask completed.')
client.close()
print('\nSSH Connection Closed.')

