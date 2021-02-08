import os
import random
from flask import Flask, request, render_template, request

cwd = os.getcwd()
app = Flask(__name__, template_folder='html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/panel.html', methods=['GET', 'POST'])
def home_post():
    if request.method == 'POST': 
        text = request.form['text']
        return text
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
