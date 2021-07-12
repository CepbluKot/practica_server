from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import json
import serial
import threading
import os

from tkinter import *
from tkinter import ttk
import webbrowser

window = Tk()
window.title("Умная дача СКБ-4 > веб-интерфейс > сервер")
window.geometry('400x250')
imgicon = PhotoImage(file=os.path.join(os.path.realpath('icon.png')))
window.tk.call('wm', 'iconphoto', window._w, imgicon)

new = 1
url = "http://localhost:8080"

def openweb():
    webbrowser.open(url,new=new)

Btn = Button(window, text = "Открыть веб-интерфейс",command=openweb)
Btn.pack()

app = Flask(__name__,static_url_path='')

CORS(app)

Com_port_json = {
   "com_devices":[
      {
         "id":1,
         "port":"COM1",
         "name":"COM1 Arduino/Genuino Uno R3"
      },
      {
         "id":2,
         "port":"COM2",
         "name":"COM2"
      },
      {
         "id":3,
         "port":"COM3",
         "name":"COM3 Arduino Leonardo"
      },
      {
         "id":4,
         "port":"COM4",
         "name":"COM4 Generic USB mouse"
      }
   ],

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
connect_data = {"port":0, "speed":0}

@app.route("/checkworking", methods = ["GET"])
def checkworking():
    checkworking = {"server_working": "tru"}
    return jsonify(checkworking)

@app.route("/connect", methods = ["GET", "POST"])
def connect():
    
    
    if request.method == 'POST':
        
        value = request.json
        print(value)
        speed = "0"
        port = "0"
        parse_data = json.loads(json.dumps(value))
        if "port" in parse_data:

            connect_data["port"] = parse_data["port"]
        if "speed" in parse_data:
            
            connect_data["speed"] = parse_data["speed"]
        
        return jsonify(value)



@app.route("/", methods = ["GET", "POST"])
def json_test():
    ser  = serial.Serial(connect_data["port"], baudrate=connect_data["speed"])
    if request.method == 'POST':
        
        value = request.json
        print(value)

        parse_data = json.loads(json.dumps(value))
        
        print(value)
        
        
        return jsonify(value)

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
