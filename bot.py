import json
import disnake
from disnake.ext import commands

try:
    with open("config.json") as f:
        config = json.load(f)
except FileNotFoundError:
    print("config.json not found!")
    exit(1)

if not config["BOT_TOKEN"]:
    print("BOT_TOKEN not found!")
    exit(1)

if not config["BOT_PREFIX"]:
    print("BOT_PREFIX not found!")
    exit(1)

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix=config["BOT_PREFIX"], intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    embed = disnake.Embed(title="Pong!", description="My ping is {0}ms".format(round(bot.latency * 1000)), color=0x00FF00)
    await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
    embed = disnake.Embed(title="Help", description="This is a help command", color=0x00FF00)
    embed.add_field(name="!ping", value="Returns the bot's latency", inline=False)
    await ctx.send(embed=embed)

bot.run(config["BOT_TOKEN"])