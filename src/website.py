import os
import random

import discordbot
import discord
from discord.ext import commands
from flask import Flask, request, render_template, request

cwd = os.getcwd()
app = Flask(__name__, template_folder='frontend')

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
        print("\n\n\n====== TOKEN: " + data['token'] + " ======")
        discordbot.createbot(token)
        return render_template('panel.html', data=data)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(308)
def permanent_redirect(e):
    return render_template('308.html'), 308

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
