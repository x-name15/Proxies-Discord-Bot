import discord, json
import ctypes, webbrowser
import requests, os, time, datetime, random
from discord import Game, Embed, File
from dhooks import Webhook, Embed
from discord.ext.commands.cooldowns import BucketType
import datetime as DT 
from time import sleep
from discord.ext import commands

with open("config.json") as f:
    config = json.load(f)
token = config.get("token")
prefix = config.get("prefix")
RPC = config.get("RPC")
hook = Webhook(config.get("hook"))
version_stable = config.get("version_stable")
rate = config.get("rate")
per = config.get("per")
t = BucketType.default

os.system("cls")
webbrowser.open_new_tab("https://github.com/x-name15")

ctypes.windll.kernel32.SetConsoleTitleW("Proxies Discord Bot By Chirimoya | Enjoy the tool | Version {}".format(version_stable))
botStartTime = DT.datetime.now()

px = commands.Bot(command_prefix=prefix)
px.remove_command('help')

input("Hey welcome to the tool\nThis tool is for educational purposes\nI will not be responsible for the misuse of the program\nWith that said, hit ENTER to continue")

@px.event
async def on_ready():
    print("-------------------------------")
    print("Im ready, to work in the server")
    print("Logged in: {}".format(px.user.name))
    print("My prefix is: {}".format(prefix))
    print("Discord Version: {}".format(discord.__version__))
    print("Version of the program: {}".format(version_stable))
    print("ID of the Bot: {}".format(px.user.id))
    print("Current Rich Presence: {}".format(RPC))
    print("Server time is: {}".format(DT.datetime.now()))
    print("-------------------------------")
    print("-------------COMMANDS LOGGER---------")
    await px.change_presence(status=discord.Status.online, activity=discord.Game(RPC))

@px.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=discord.Embed(title='Cooldown',description='{}'.format(error)))
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Are u sure do u type correctly the command?")
    if isinstance(error, commands.errors.NoPrivateMessage):
        await ctx.send("You cant generate on my DMs\n:x:")

@px.command()
@commands.guild_only()
async def ping(ctx):
    await ctx.send("Pong\nLatency: {}".format(px.latency))
    print(" > User {} used the PING command".format(ctx.author))
    embed = Embed(description='Ignore me Im just logging the commands', color=0x5CDBF0, timestamp='now')
    image1 = 'https://cdn.discordapp.com/attachments/839645806448476221/841003337515663380/images.png'
    embed.set_author(name='💣 Command EXECUTED 💣')
    embed.add_field(name="**Who used the command**", value="```{}```".format(ctx.author), inline=True)
    embed.add_field(name='**Command Executed**', value='```ping```', inline=True)
    embed.add_field(name='**Channel ID?**', value='```<#{}>```'.format(ctx.channel.id), inline=True)
    embed.add_field(name='**Time?**', value='```{}```'.format(datetime.datetime.now()), inline=True)
    embed.set_footer(text='Discord Proxies Bot by Chirimoya | WebHook Log | Version: {}'.format(version_stable))
    embed.set_thumbnail(image1)
    hook.send(embed=embed)

@px.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def https(ctx):
    f = open("proxies/https-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/v2/?request=getproxies&amp;protocol=http&amp;timeout=10000&amp;country=all&amp;ssl=all&amp;anonymity=all')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.author.send("```HTTPS Proxies from ProxyScrape Free```")
    await ctx.author.send(file=File("proxies/https-proxies.txt"))
    num_lines1 = sum(1 for line in open('proxies/https-proxies.txt'))
    await ctx.author.send(embed=discord.Embed(title='About the proxies',description="Length: {}".format(num_lines1)))
    await ctx.send("```Check DMs```")
    print(" > User {} has scraped some HTTPS Proxies".format(ctx.author))
    embed = Embed(description='Ignore me Im just logging the commands', color=0x5CDBF0, timestamp='now')
    image1 = 'https://cdn.discordapp.com/attachments/839645806448476221/841003337515663380/images.png'
    embed.set_author(name='💣 Command EXECUTED 💣')
    embed.add_field(name="**Who used the command?**", value="```{}```".format(ctx.author), inline=True)
    embed.add_field(name='**Command Executed**', value='```https```', inline=True)
    embed.add_field(name='**Type of Proxies**', value='```HTTPS Proxies```', inline=True)
    embed.add_field(name='**Length of the File**', value='```{}```'.format(num_lines1), inline=True)
    embed.add_field(name='**File Sended?**', value='```Yes!```', inline=True)
    embed.add_field(name='**Channel ID?**', value='```<#{}>```'.format(ctx.channel.id), inline=True)
    embed.add_field(name='**Time?**', value='```{}```'.format(datetime.datetime.now()), inline=True)
    embed.set_footer(text='Discord Proxies Bot by Chirimoya | WebHook Log | Version: {}'.format(version_stable))
    embed.set_thumbnail(image1)
    hook.send(embed=embed)

@px.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def socks4(ctx):
    f = open("proxies/socks4-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/v2/?request=getproxies&amp;protocol=socks4&amp;timeout=10000&amp;country=all')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.author.send("```Socks4 Proxies From ProxyScrape Free```")
    await ctx.author.send(file=File("proxies/socks4-proxies.txt"))
    num_lines2 = sum(1 for line in open('proxies/socks4-proxies.txt'))
    await ctx.author.send(embed=discord.Embed(title='About the proxies',description="Length: {}".format(num_lines2)))
    await ctx.send("```Check DMs```")
    print(" > User {} has scraped some Socks4 Proxies".format(ctx.author))
    embed = Embed(description='Ignore me Im just logging the commands', color=0x5CDBF0, timestamp='now')
    image1 = 'https://cdn.discordapp.com/attachments/839645806448476221/841003337515663380/images.png'
    embed.set_author(name='💣 Command EXECUTED 💣')
    embed.add_field(name="**Who used the command?**", value="```{}```".format(ctx.author), inline=True)
    embed.add_field(name='**Command Executed**', value='```socks4```', inline=True)
    embed.add_field(name='**Type of Proxies**', value='```Socks4 Proxies```', inline=True)
    embed.add_field(name='**Length of the File**', value='```{}```'.format(num_lines2), inline=True)
    embed.add_field(name='**File Sended?**', value='```Yes!```', inline=True)
    embed.add_field(name='**Channel ID?**', value='```<#{}>```'.format(ctx.channel.id), inline=True)
    embed.add_field(name='**Time?**', value='```{}```'.format(datetime.datetime.now()), inline=True)
    embed.set_footer(text='Discord Proxies Bot by Chirimoya | WebHook Log | Version: {}'.format(version_stable))
    embed.set_thumbnail(image1)
    hook.send(embed=embed)

@px.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def socks5(ctx):
    f = open("proxies/socks5-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/v2/?request=getproxies&amp;protocol=socks5&amp;timeout=10000&amp')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.author.send("```Socks5 Proxies from ProxyScrape Free```")
    num_lines3 = sum(1 for line in open('proxies/socks5-proxies.txt'))
    await ctx.author.send(embed=discord.Embed(title='About the proxies',description="Length: {}".format(num_lines3)))
    await ctx.author.send(file=File("proxies/socks5-proxies.txt"))
    await ctx.send("```Check DMs```")
    print(" > User {} has scraped some Socks5 Proxies".format(ctx.author))
    embed = Embed(description='Ignore me Im just logging the commands', color=0x5CDBF0, timestamp='now')
    image1 = 'https://cdn.discordapp.com/attachments/839645806448476221/841003337515663380/images.png'
    embed.set_author(name='💣 Command EXECUTED 💣')
    embed.add_field(name="**Who ran the command?**", value="```{}```".format(ctx.author), inline=True)
    embed.add_field(name='**Command Executed**', value='```socks5```', inline=True)
    embed.add_field(name='**Type of Proxies**', value='```Socks5 Proxies```', inline=True)
    embed.add_field(name='**Length of the File**', value='```{}```'.format(num_lines3), inline=True)
    embed.add_field(name='**File Sended?**', value='```Yes!```', inline=True)
    embed.add_field(name='**Channel ID?**', value='```<#{}>```'.format(ctx.channel.id), inline=True)
    embed.add_field(name='**Time?**', value='```{}```'.format(datetime.datetime.now()), inline=True)
    embed.set_footer(text='Discord Proxies Bot by Chirimoya | WebHook Log | Version: {}'.format(version_stable))
    embed.set_thumbnail(image1)
    hook.send(embed=embed)

@px.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def mixed(ctx):
    f = open("proxies/mixed-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=all&timeout=5000')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.author.send("```Mixed Proxies from ProxyScrape Free```")
    await ctx.author.send(file=File("proxies/mixed-proxies.txt"))
    num_lines4 = sum(1 for line in open('proxies/mixed-proxies.txt'))
    await ctx.author.send(embed=discord.Embed(title='About the proxies',description="Length: {}".format(num_lines4)))
    await ctx.send("```Check DMs```")
    print(" > User {} has scraped some Mixed Proxies".format(ctx.author))
    embed = Embed(description='Ignore me Im just logging the commands', color=0x5CDBF0, timestamp='now')
    image1 = 'https://cdn.discordapp.com/attachments/839645806448476221/841003337515663380/images.png'
    embed.set_author(name='Command EXECUTED')
    embed.add_field(name="**Who ran the command?**", value="```{}```".format(ctx.author), inline=True)
    embed.add_field(name='**Command Executed**', value='```mixed```', inline=True)
    embed.add_field(name='**Type of Proxies**', value='```Mixed Proxies```', inline=True)
    embed.add_field(name='**Length of the File**', value='```{}```'.format(num_lines4), inline=True)
    embed.add_field(name='**File Sended?**', value='```Yes!```', inline=True)
    embed.add_field(name='**Channel ID?**', value='```<#{}>```'.format(ctx.channel.id), inline=True)
    embed.add_field(name='**Time?**', value='```{}```'.format(datetime.datetime.now()), inline=True)
    embed.set_footer(text='Discord Proxies Bot by Chirimoya | WebHook Log | Version: {}'.format(version_stable))
    embed.set_thumbnail(image1)
    hook.send(embed=embed)

@px.command()
@commands.guild_only()
async def help(ctx):
    embed = Embed(title="Commands", description="Hey.", color=0x5CDBF0)
    embed.add_field(name="{}help".format(prefix), value="Displays all available commands", inline=False)
    embed.add_field(name="{}https".format(prefix), value="Sends fresh https proxy list", inline=False)
    embed.add_field(name="{}socks4".format(prefix), value="Sends fresh socks4 proxy list", inline=False)
    embed.add_field(name="{}socks5".format(prefix), value="Sends fresh socsk5 proxy list", inline=False)
    embed.add_field(name="{}mixed".format(prefix), value="Sends fresh http, https, socks4 and socks5 proxy list", inline=False)
    await ctx.send(embed=embed)
    print(" > User {} has used the HELP command".format(ctx.author))
    embed = Embed(description='Ignore me Im just logging the commands', color=0x5CDBF0, timestamp='now')
    image1 = 'https://cdn.discordapp.com/attachments/839645806448476221/841003337515663380/images.png'
    embed.set_author(name='💣 Command EXECUTED 💣')
    embed.add_field(name="**Who used the command**", value="```{}```".format(ctx.author), inline=True)
    embed.add_field(name='**Command Executed**', value='```help```', inline=True)
    embed.add_field(name='**Channel ID?**', value='```<#{}>```'.format(ctx.channel.id), inline=True)
    embed.add_field(name='**Time?**', value='```{}```'.format(datetime.datetime.now()), inline=True)
    embed.set_footer(text='Discord Proxies Bot by Chirimoya | WebHook Log | Version: {}'.format(version_stable))
    embed.set_thumbnail(image1)
    hook.send(embed=embed)



px.run(token)