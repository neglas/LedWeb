from flask import Flask, render_template, jsonify, request
import subprocess

def TurnHyperON():
    subprocess.call(['sh', '/home/neglas/Webapp/StartHDR.sh'])
    return "goodboi"

def TurnHyperOFF():
    print("OFF")
    subprocess.call(['sh', '/home/neglas/Webapp/StopHDR.sh'])
    return "goodBoi"

def TurnMovieModeON():
    print("ON")
    TurnHyperON()
    subprocess.call(['sh', '/home/neglas/Webapp/DimLightsDown.sh'])
    return "goodBoi"

def TurnMovieModeOFF():
    TurnHyperOFF()
    subprocess.call(['sh', '/home/neglas/Webapp/DimLightsUp.sh'])	

def MyFunc():
    subprocess.call(['sh', './testshell.sh'])
    return "goodBoi"

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def ExecuteFunction():
    data = request.get_json()
    print(data)
    if(data.get('buttonId')=='MyBtn'):
        if(data.get('status')=='on'):
            result = TurnHyperON()
        elif(data.get('status')=='off'):
            result = TurnHyperOFF()
    elif(data.get('buttonId')=='MviBtn'):
       
        if(data.get('status')=='on'):
            result = TurnMovieModeON()
        elif(data.get('status')=='off'):
            result = TurnMovieModeOFF()
    else:
        result = "Invalid status"
        
    return jsonify({"result": result})

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
