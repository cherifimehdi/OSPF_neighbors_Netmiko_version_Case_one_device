# Import the ConnectHandler Function to create an Object for R1
from netmiko import ConnectHandler

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

# Retrieve the parsed result of "show ip ospf neighbor" command
output = net_connect.send_command('show ip ospf neighbor', use_textfsm=True)

# For each neighbor N: access to its ID, Interface, Address and State
for N in output:
    Id, Interface, Address, State=N.get('neighbor_id'), N.get('interface'), N.get('address'), ((N.get('state')).split('/'))[1]
    print(f"Neighbor {Id}\n     - Connected to it via the interface: {Interface} having the address: {Address}, its state is {State}")


# End the SSH session for R1
net_connect.disconnect()
