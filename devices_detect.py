import serial.tools.list_ports
ports = serial.tools.list_ports.comports()

com_list = {
    "com_devices":[]
}

n = 0
for port, desc, hwid in sorted(ports):
        com_list["com_devices"].append( { "id":n, "port":port, "name":port + " "+ desc}) 
        n+=1

print(com_list)
