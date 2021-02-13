import os
import random
from flask import Flask, request, render_template, request

cwd = os.getcwd()
app = Flask(__name__, template_folder='html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/panel/', methods=['GET', 'POST'])
def panel():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        return render_template('panel.html', form_data=form_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
