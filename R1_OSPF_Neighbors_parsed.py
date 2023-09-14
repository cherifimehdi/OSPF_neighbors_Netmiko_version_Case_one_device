# Import the ConnectHandler Function to create an Object for R1
from netmiko import ConnectHandler
from pprint import pprint

# Parameters of R1
password = "cisco"

R1 = {
    "device_type": "cisco_ios",
    "host": "192.168.1.251",
    "username": "Admin",
    "password": password,
}
# Connect to R1 via SSH
net_connect = ConnectHandler(**R1)

# Retrieve the result of "show ip ospf neighbor" command
output = net_connect.send_command('show ip ospf neighbor', use_textfsm=True)

# Display the result
pprint(output)

# End the SSH session for R1
net_connect.disconnect()
