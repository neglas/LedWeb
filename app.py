from flask import Flask, render_template, jsonify, request
import subprocess

def TurnHyperON():
    subprocess.call(['sh', '/home/neglas/Webapp/StartHDR.sh'])
    return "goodboi"
def TurnMovieModeON():
    print("ON")
    TurnHyperON()
    subprocess.call(['sh', '/home/neglas/Webapp/DimLightsDown.sh'])
    return "goodBoi"

def TurnHyperOff():
    print("OFF")
    subprocess.call(['sh', '/home/neglas/Webapp/StopHDR.sh'])
    subprocess.call(['sh', '/home/neglas/Webapp/DimLightsUp.sh'])
    return "goodBoi"


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

    if(data.get('status')=='on'):
        if(data.get('buttonId')=='MyBtn'):
            result = TurnHyperON()
        elif(data.get('buttonId')=='MovieModeBtn'):
            TurnMovieModeON()
    elif(data.get('status')=='off'):
        result = TurnHyperOff()
    elif(data.get('status')=='movie_mode'):
        result = TurnMovieModeON()
    else:
        result = "Invalid status"
        
    return jsonify({"result": result})

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
