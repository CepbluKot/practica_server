from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import serial
import threading
import os
import serial.tools.list_ports



from tkinter import *
from tkinter import ttk
import webbrowser

window = Tk()
window.title("Умная дача СКБ-4 > веб-интерфейс > сервер")
window.geometry('400x250')
imgicon = PhotoImage(file=os.path.join(os.path.realpath('icon.png')))
#imgicon = PhotoImage("")
window.tk.call('wm', 'iconphoto', window._w, imgicon)

new = 1
url = "http://localhost:5000"

ports = serial.tools.list_ports.comports()

def openweb():
    webbrowser.open(url,new=new)

Btn = Button(window, text = "Открыть веб-интерфейс",command=openweb)
Btn.pack()

app = Flask(__name__,static_url_path='')
CORS(app)

cors = CORS(app, resources={r"/*": {"origins": "http://localhost:5000"}})

Com_port_json = {
   "com_devices":[],

"com_speed":[
    50,
    75,
    110,
    150,
    300,
    600,
    1200,
    2400,
    4800,
    9600,
    19200,
    38400,
    57600,
    115200
]
}
#looking for devices
n = 0
for port, desc, hwid in sorted(ports):
        Com_port_json["com_devices"].append( { "id":n, "port":port, "name":port + "/"+ desc}) 
        n+=1

connect_data = {"port":0, "speed":0}

terminal_chat = [
    {
        "id":1,
        "type": "device",
        "name":"COM1 device",
        "message":"Waiting for command..."
    },
    {
        "id":2,
        "type": "user",
        "name":"admin",
        "message":"set btn1 action wake"
    },
    {
        "id":3,
        "type": "device",
        "name":"COM1 device",
        "message":"success"
    },
]

@app.route("/terminal/echo", methods = ["GET"])
def echo_terminal_chat():
    return jsonify(terminal_chat)

@app.route("/checkworking", methods = ["GET"])
def checkworking():
    checkworking = {"server_working": "tru"}
    return jsonify(checkworking)

@app.route("/com/connect", methods = ["GET", "POST"])
def connect():
    
    print("lol")
    if request.method == 'POST':
        
        value = request.json
        print(value)
            
        return jsonify(value)



@app.route("/", methods = ["GET", "POST"])
def json_test():
    print(jsonify(request.json))
    return jsonify(request.json)

@app.route("/com/show", methods = ["GET", "POST"])
def func():
    return jsonify(Com_port_json)


@app.errorhandler(500)
def internal_error(error):

    return "500 error"

@app.errorhandler(404)
def not_found(error):
    return "404 error"

@app.errorhandler(400)
def not_found(error):
    return "400 error"


def flask_start():
    app.run('0.0.0.0', port='5000')

def tkinter_start():
    window.mainloop()

if __name__ == "__main__":
    flt = threading.Thread(target=flask_start)
    flt.daemon = True
    flt.start() 
    tkinter_start() 