from flask import Flask, render_template, jsonify, request
import subprocess

def TurnHyperON():
    print("ON")
    subprocess.call(['sh', '/home/neglas/Webapp/StartHDR.sh'])
    return "goodBoi"

def TurnHyperOff():
    print("OFF")
    subprocess.call(['sh', '/home/neglas/Webapp/StopHDR.sh'])
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
        result = TurnHyperON()
    elif(data.get('status')=='off'):
        result = TurnHyperOff()
    else:
        result = "Invalid status"
        
    return jsonify({"result": result})

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')