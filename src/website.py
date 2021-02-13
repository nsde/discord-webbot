import os
import random

import discordbot
import discord
from discord.ext import commands
from flask import Flask, request, render_template, request

cwd = os.getcwd()
app = Flask(__name__, template_folder='html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/panel/', methods=['GET', 'POST'])
def panel():
    if request.method == 'GET':
        return f'The URL /data cant be accessed directly'
    if request.method == 'POST':
        data = request.form
        token = str(data['token'])
        print("\n\n\n==========" + data['token'])
        
        discordbot.createbot(token)
        return render_template('panel.html', data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
