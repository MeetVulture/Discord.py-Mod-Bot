import discord
import random 
import json
import time
import math
import datetime
import choice
import os
from asyncio import sleep
from keep_alive import keep_alive
from discord.ext import commands


def get_prefix(client, message):
  with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)

  return prefixes[str(message.guild.id)]


client = commands.Bot(command_prefix = get_prefix)





@client.event
async def on_guild_join(guild):
      with open ('prefixes.json', 'r') as f:
            prefixes = json.load(f)
 
      prefixes[str(guild.id)] = '.'

      with open ('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
      with open ('prefixes.json', 'r') as f:
            prefixes = json.load(f)

            prefixes.pop(str(guild.id))

            with open ('prefixes.json', 'w') as f:
                  json.dump(prefixes, f, indent=4)

@client.command()
async def changeprefix(ctx, prefix):
      with open ('prefixes.json', 'r') as f:
            prefixes = json.load(f)

      prefixes[str(ctx.guild.id)] = prefix


      with open ('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

      await ctx.send(f'Prefix changed to: {prefix}')



@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.listening(f'To MeetVulture on Github'))
    print('0NLINE❗')

@client.command()
async def K(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.message.add_reaction('🥶')
    await ctx.send (f'Kicked {member.mention}')


@client.command()
async def B(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.message.add_reaction('🤐')
    await ctx.send(f'Banned {member.mention}')
@client.command()
async def U(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name,member_discriminator):
            await ctx.guild.unban(user)
            await ctx.message.add_reaction('😯')
            await ctx.send(f'Unbanned {user.mention}')
            return



@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.message.add_reaction('🤔')
        await ctx.send('Invaild command used type **`command_prefix helop`** for command sheet!')



@client.command()
async def ping(ctx):
    await ctx.message.add_reaction('📺')
    await ctx.send(f'Pong! {round (client.latency *1000)}ms')





tell = ['Hey..',"whats'up", 'hola!','hello','Hi!','good day','greetings','hey','hi']
@client.command()
async def hi(ctx):
  await ctx.message.add_reaction('👋')
  await ctx.send(f'{random.choice(tell)}')

@client.command()
async def spam(ctx):
    await ctx.message.add_reaction('❗')
    await ctx.send('Warning Alert!')
    time.sleep(2)
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**') 





        



tell = ['Bye',"Bye, Have a great day", 'Bye, Hope your day went as you thought']
@client.command()
async def bye(ctx):
  await ctx.send(f'{random.choice(tell)}')


		


@client.command()
async def info(ctx):
    await ctx.send('INSERT BOT INFO')
    





keep_alive()
client.run('bot token')
