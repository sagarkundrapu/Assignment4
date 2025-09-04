from flask import Flask, render_template
from flask import request, redirect
import requests
app = Flask(__name__)

@app.route('/', methods=['GET'])
def todo():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form.to_dict()
    requests.post('http://localhost:5000/submittodoitem', data=data)
    return ""

if __name__ == '__main__':
    app.run(debug=True, port=3000, host='0.0.0.0')