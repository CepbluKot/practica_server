
import serial.tools.list_ports
import time
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import json
import serial


app = Flask(__name__,static_url_path='')
ports = serial.tools.list_ports.comports()
CORS(app)
com_list = {
    "com_devices":[]
}

n = 0
for port, desc, hwid in sorted(ports):
        com_list["com_devices"].append( { "id":n, "port":port, "name":desc}) 
        n+=1

# Arduino_coms = {
#     "arduino_devices":[]
# }
# count = 0
# id = 0
# while count != n:
#     if com_list["com_devices"][count]["name"] == 'Arduino Uno':
#         Arduino_coms["arduino_devices"].append({ "id":id, "port":com_list["com_devices"][count]["port"], "name":com_list["com_devices"][count]["name"]}     )
#         id +=1
#     count+=1

#print(Arduino_coms)


connect_data = {"port":0, "speed":0}

@app.route("/check", methods = ["GET"])
def check():
    if request.method == "GET":
        return jsonify(com_list)


@app.route("/connect", methods = ["GET", "POST"])
def connect():
    
    
    if request.method == 'POST':
        
        value = request.json
        speed = "0"
        port = "0"
        parse_data = json.loads(json.dumps(value))
        if "port" in parse_data:

            connect_data["port"] = parse_data["port"]
        if "speed" in parse_data:
            
            connect_data["speed"] = parse_data["speed"]
        
        return jsonify("accepted")



@app.route("/datalink", methods = ["GET", "POST"])
def datalink():
    
    print(connect_data["port"], " ", connect_data["speed"])
    ser  = serial.Serial(port = connect_data["port"], baudrate=connect_data["speed"])
    ser.write(b'\n')
    time.sleep(3)
    
    if request.method == 'POST':
        value = request.json
        parse_data = json.loads(json.dumps(value))
        
        if "cmd" in parse_data:
            ser.write(bytes(parse_data["cmd"].encode()) + b'\r\n')
        
        time.sleep(1)
        recieved = ""
        while ser.inWaiting() > 0:
            line = ser.readline()
            if line:

                recieved += line.decode().strip()

        
        return jsonify(recieved)

            


if __name__=="__main__":
    app.run(host='0.0.0.0')




