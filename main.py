import discord
import os
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()


intents = discord.Intents.default()
intents.members = True  

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ Logged in as {client.user}')

@client.event
async def on_member_join(member):
    try:
        gif_url = "https://media0.giphy.com/media/ZLLv3zATTcMiuQ6dZn/giphy.gif"
        embed = discord.Embed(title=f"👋 Welcome {member.mention}!")
        embed.set_image(url=gif_url)
        await member.send(embed=embed)
        print(f"✅ Sent welcome DM to {member.name}")
    except discord.Forbidden:
        print(f"⚠️ Can't DM {member.name} — DMs might be off")

keep_alive()
client.run(os.environ['BOT_TOKEN'])

