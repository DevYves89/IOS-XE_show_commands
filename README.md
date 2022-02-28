# IOS-XE_show_commands
this package lets your OP5 or NAGIOS do checks with show commands on IOS-XE 


Just run it with python 3.6 

Run the .py file with the following parameters:

10.1.0.1 username mypassword "sh ver | i Cisco IOS XE Software, Version" "Version (\d\d.\d\d.\d\d.)"

output in this example would be: 

/root/PycharmProjects/op5check/venv/bin/python /root/PycharmProjects/op5check/main.py 10.1.0.1 username mypassword "sh ver | i Cisco IOS XE Software, Version" "Version (\d\d.\d\d.\d\d.)"
16.12.05b

Process finished with exit code 0
