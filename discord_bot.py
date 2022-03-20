import discord
from discord.ext import commands
import os
client = discord.Client()
connected = False
voice_channel = []
bot = commands.Bot(command_prefix='&')

def switch_connection():
    connected = not connected
@bot.command(pass_context = True)
async def leave(ctx):
        server = ctx.message.server
        voice_client = bot.voice_client_int(server)
        await voice_client.disconnect() 

 

@bot.command()
async def sr(ctx):
    ctx.voice_client.stop_recording() # Stop the recording, finished_callback will shortly after be called
    await ctx.respond("Stopped!")
@client.event 
async def on_ready():
    print(' bot funcionando com sucesso!')

@client.event 
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('&help'):
        await message.channel.send('Eu transcrevo textos em portguês gravados nos canais de voz. para me chamar em um canal de voz, digite: $invite')
    if message.content.startswith('&join'):
        try:
            channel = message.author.voice.channel
            voice_channel.append(channel)
            await channel.connect().start_recording()

            switch_connection()
        except discord.ClientException:
            await message.channel.send('já estou conectado a um canal de voz!')
    if message.content.startswith('&leave'):
        if connected:
            channel = voice_channel[0]
            await channel.disconnect()
            switch_connection()
    if message.content.startswith('&rec'):
        

        print('recording...')



client.run(os.getenv('TOKEN'))