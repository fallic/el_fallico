import discord
from discord.ext import commands

#Assigning functions to variables
client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
  print("Bot online.")

@client.command
async def hot(ctx):
  await ctx.message.channel.send("https://tenor.com/view/hog-rider-coc-clash-of-clans-gif-24053135")

@client.command(pass_context=True)
async def join(ctx):
  channel = ctx.message.author.voice.voice_channel
  await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
  server = ctx.message.server
  voice_client = client.voice_client_in(server)
  await voice_client.disconnect
