from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__,static_url_path='')

CORS(app)
Com_port_json = {
"com_devices":{
"1":"COM1 Arduino/Genuino Uno R3",
"2":"COM2",
"3":"COM3 Arduino Leonardo",
"4":"COM4 Generic USB mouse"
},
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

@app.route("/", methods = ["GET", "POST"])
def json_test():
    
    sost = 1

    if request.method == 'POST':
        
        value = request.json
        
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


if __name__=="__main__":
    app.run(host='0.0.0.0')