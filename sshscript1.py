from netmiko import ConnectHandler

iosv_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.112.11',
    'username': 'Karandeep',
    'password': 'test'
}

iosv_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.112.12',
    'username': 'Karandeep',
    'password': 'test'
}

iosv_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.112.13',
    'username': 'Karandeep',
    'password': 'test'
}

all_devices = [iosv_s1, iosv_s2, iosv_s3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    for x in range (2,101):
       print ("Creating VLAN " + str(x))
       config_commands = ['vlan ' + str(x), 'name Test_VLAN ' + str(x)]
       output = net_connect.send_config_set(config_commands)
       print (output)
