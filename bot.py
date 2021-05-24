import discord
from discord import member
from discord.ext import commands
from discord.raw_models import RawReactionActionEvent

client = commands.Bot(command_prefix = "!") 

@client.event
async def on_ready():
    print('Running')
    await client.change_presence(status=discord.Status.online, activity=discord.Game('!about'))

@client.command()
async def Totallysecret(ctx):
    await ctx.send("Wow you have found a secret that was totally secret!")

@client.command()
async def ping(ctx):
    await ctx.send(f"**Ping :** {round(client.latency * 1000)}**MS**")

@client.command()
async def about(ctx):
    await ctx.send("Hello! This bot was made by KnowZbox and R4FÆL in the Python coding language. Type !help to see all commands.")

@client.command()
async def kick(ctx, member : discord.Member, *, reason):
    await member.kick(reason=reason)
    await ctx.send(f"{member} was kicked for {reason}")

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"{member} Was banned for {reason}")

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):

            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return 

@client.command()
async def embed(ctx):
    embed=discord.Embed(title="Simple EMBED",  description="Hi", color=0xFF5733)
    embed.add_field(name="Field 1 Title", value="This is the value for field 1. This is NOT an inline field.", inline=False)
    embed.add_field(name="Field 2 Title", value="It is inline with Field 3", inline=True)
    embed.add_field(name="Field 3 Title", value="It is inline with Field 2", inline=True)
    embed.set_thumbnail(url="https://dwglogo.com/wp-content/uploads/2019/09/Discord_logo.png")
    embed.set_footer(text="This is the footer. It contains text at the bottom of the embed")
    await ctx.send(embed=embed)

@client.command()
async def clear(ctx, ammount=5):
    await ctx.channel.purge(limit=ammount)

client.run("ODQ0OTc0NTA2NTY0OTExMTA1.YKaN1Q.AIz7LMS_rjmaJHHqNQT6cxXaeZA")