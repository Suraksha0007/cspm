import os
from flask import Flask, render_template, request, send_file
import subprocess 
import json
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    text = request.form['text']
    print("hello")
    # Call the subprocess with the cleaned JSON string
    process = subprocess.Popen(['python', 'myfile.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate(input=text.encode())
    print(out)
    file_path = os.path.join('output', 'iam-report-example.html')
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        return html_content
    else:
        return 'HTML file not found.'

if __name__ == '__main__':
    app.run(debug=True)
