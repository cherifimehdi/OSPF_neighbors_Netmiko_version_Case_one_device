# Here how to check R1 type
from netmiko import ConnectHandler


R1 = {
    "device_type": "cisco_ios",
    "host": "192.168.1.251",
    "username": "Admin",
    "password": password,
}

net_connect = ConnectHandler(**R1)
net_connect.disconnect()
