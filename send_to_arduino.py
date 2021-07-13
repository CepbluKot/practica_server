import serial
import serial.tools.list_ports
import time
ports = serial.tools.list_ports.comports()

com_list = {
    "com_devices":[]
}

n = 0
for port, desc, hwid in sorted(ports):
        com_list["com_devices"].append( { "id":n, "port":port, "name":desc}) 
        n+=1

Arduino_coms = {
    "arduino_devices":[]
}
count = 0
id = 0
while count != n:
    if com_list["com_devices"][count]["name"] == 'Arduino Uno':
        Arduino_coms["arduino_devices"].append({ "id":id, "port":com_list["com_devices"][count]["port"], "name":com_list["com_devices"][count]["name"]}     )
        id +=1
    count+=1

#print(Arduino_coms)



ser  = serial.Serial(port = Arduino_coms["arduino_devices"][0]["port"], baudrate=9600)

ser.write(bytes(b'butt'))

received = ""
ser.write(b'begin\n')
time.sleep(5)


ser.write(b'butt 1\r\n')
ser.write(b'butt 2\r\n')
time.sleep(1)
while ser.inWaiting() > 0:
    line = ser.readline()
    if line:

        print(line.decode().strip())


print(received)