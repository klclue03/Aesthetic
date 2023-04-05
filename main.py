import discord
from discord.ext import commands
from config import BOT_TOKEN, COMMANDS, PFP
import os
import asyncio
from datetime import datetime

client = commands.Bot(command_prefix="+", intents=discord.Intents.all())
client.remove_command("help")


@client.event
async def on_ready():
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)

    await client.change_presence(status=discord.Status.idle, activity=discord.Game("your server"))


@client.event
async def on_message(message):
    if message.content.startswith("+"):
        ok = False
        words = message.content.split(" ")

        for command in COMMANDS:
            if command == words[0]:
                ok = True
                break

        if not ok:
            em = discord.Embed(title="**🔴 Command doesn't exist. Try again!**",
                               description="**❓ Run +help for a list of commands**",
                               color=discord.Color.random())
            timestamp = datetime.now()
            em.set_footer(text="Command Error | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await message.channel.send(embed=em)

    await client.process_commands(message)


async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")


async def main():
    async with client:
        await load()
        await client.start(BOT_TOKEN)

asyncio.run(main())
