import discord
from discord.abc import Messageable
from discord.errors import Forbidden
from discord.ext import commands
from discord.ext.commands.core import Command, command

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True) #People with permission kick_member can only use this command
    async def kick(self,ctx,member:discord.Member,*,reason=None):
        target = member
        if reason == None: #if no reason is provided
            reason = "No Reason Provided" #this will be the reason
        if not member: #if no member is provided
            embed=discord.Embed(title="",
            description="You actually need to mention someone to kick them.```!kick Levent#9690 reason```",
            color=discord.Colour.red())
            await ctx.send(embed=embed)
            return
        if member == ctx.author: #If the mentioned member is the message sender.
            embed=discord.Embed(title="",
            description="You cannot kick yourself.",
            color=discord.Colour.red())
            await ctx.send(embed=embed)
            return
        if target.top_role > ctx.author.top_role: #If the highest role of the target is greater than the sender.
            embed=discord.Embed(title="Role Heirachy",
            description="You cannot kick someone with a role higher than you or equal than you.",
            color=discord.Colour.red())
            await ctx.send(embed=embed)
            return
        if member == self.client.user: #if target is the bot itself
            embed=discord.Embed(title="",
            description="I cannot kick myself.",
            color=discord.Colour.red())
            await ctx.send(embed=embed)
            return
        else: 
            try:
                await member.kick()
                embed=discord.Embed(title="",
                description=f"{member.mention} has been kicked by {ctx.author.mention}. **Reason** : {reason}",
                color=discord.Colour.teal())
                await ctx.send(embed=embed)
            except Forbidden:
                embed=discord.Embed(title="Forbidden",
                description="This error usually appears when the target has higher role than me or if the targer is server owner.",
                color=discord.Colour.red())
                await ctx.send(embed=embed)
        
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self,ctx,member:discord.Member,*,reason=None):
        target = member
        if reason == None:
            reason = "No Reason Provided"
        if not member:
            embed=discord.Embed(title="",
            description="You actually need to mention someone to ban them.```!kick Levent#9690 reason```",
            color=discord.Colour.red())
            await ctx.send(embed=embed)
            return
        if member == ctx.author:
            embed=discord.Embed(title="",
            description="You cannot ban yourself.",
            color=discord.Colour.red())
            await ctx.send(embed=embed)
            return
        if target.top_role > ctx.author.top_role:
            embed=discord.Embed(title="Role Heirachy",
            description="You cannot ban someone with a role higher than you or equal than you.",
            color=discord.Colour.red())
            await ctx.send(embed=embed)
            return
        if member == self.client.user:
            embed=discord.Embed(title="",
            description="I cannot ban myself.",
            color=discord.Colour.red())
            await ctx.send(embed=embed)
            return
        else:
            try:
                await member.kick()
                embed=discord.Embed(title="",
                description=f"{member.mention} has been banned by {ctx.author.mention}. **Reason** : {reason}",
                color=discord.Colour.teal())
                await ctx.send(embed=embed)
            except Forbidden:
                embed=discord.Embed(title="Forbidden",
                description="This error usually appears when the target has higher role than me or if the targer is server owner.",
                color=discord.Colour.red())
                await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Moderation(client))
