import threading

from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command(name='ping', help='Test the bot.')
async def ping(ctx):
      await ctx.send(response)

def createbot(token):
  def runbot():
    bot.run(token)
  bot_thread = threading.Thread(target=runbot)