from flask import Flask, render_template, request

app = Flask(__name__)

def MyFunc():
    print("ButtonPressed!")
    return "goodBoi"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def ExecuteFunction():
    result = MyFunc()
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')