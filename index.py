import discord
import os
import asyncio
from discord.ext import commands
from discord.ext.commands.errors import ExtensionNotFound


client = commands.Bot(command_prefix='!') #custom prefix for your discord bot
client.remove_command('help') #removes the built in help commmand so you can create a custom help command.


@client.command()
@commands.is_owner()
async def load(ctx, extention):
    client.load_extension(f"cogs.{extention}")
    print(f"{extention} has been loaded.")
    await ctx.send(f"{extention} has been loaded.")

@client.command()
@commands.is_owner()
async def unload(ctx, extention):
    client.unload_extension(f"cogs.{extention}")
    await ctx.send(f"{extention} has been unloaded.")
    print(f"{extention} has been unloaded.")



client.run("your_bot_taken_here")
