from flask import Flask, render_template, request

app = Flask(__name__)

def MyFunc():
    return "Button press success!"
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def ExecuteFunction():
    if request.method == 'POST':
        result = MyFunc()
        return result

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')