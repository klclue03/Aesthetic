import discord
from discord.ext import commands
from config import BANNER, country_dict, PFP
from datetime import datetime


class Enter(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        em = discord.Embed(title=f"**Welcome to {member.guild.name}!**")
        em.set_image(url=member.guild.icon.url)
        timestamp = datetime.now()
        em.set_footer(text="Join | " + timestamp.strftime(r"%I:%M %p"))
        em.set_author(name="Aesthetic", icon_url=PFP)

        await member.send(embed=em)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                em = discord.Embed(title="**Thanks for adding Aesthetic to your server!**")
                em.set_image(url=BANNER)
                timestamp = datetime.now()
                em.set_footer(text="Bot Add | " + timestamp.strftime(r"%I:%M %p"))
                em.set_author(name="Aesthetic", icon_url=PFP)

                await channel.send(embed=em)
                break

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        keys = country_dict.keys()

        for country in keys:
            if country in message.content.lower():
                await message.add_reaction(country_dict[country])


async def setup(client):
    await client.add_cog(Enter(client))
