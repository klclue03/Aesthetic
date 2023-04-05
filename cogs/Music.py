import discord
from discord.ext import commands
import yt_dlp
from discord import FFmpegPCMAudio
from datetime import datetime
from config import PFP


class Music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['dc'])
    async def disconnect(self, ctx):
        voice_client = discord.utils.get(self.client.voice_clients, guild=ctx.guild)

        if not voice_client:
            em = discord.Embed(title="**🔴 Bot is not in your voice channel!**",
                               description="❓ Type +help disconnect for information about this command.",
                               color=discord.Color.yellow())
            timestamp = datetime.now()
            em.set_footer(text="Disconnect | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await ctx.send(embed=em)
            return

        await ctx.voice_client.disconnect()

        em = discord.Embed(description="**Bot disconnected!**", color=discord.Color.yellow())
        em.set_author(name="Aesthetic", icon_url=PFP)
        timestamp = datetime.now()
        em.set_footer(text="Disconnect | " + timestamp.strftime(r"%I:%M %p"))

        await ctx.send(embed=em)

    @commands.command(aliases=['p'])
    async def play(self, ctx, url=None):
        if url is None:
            em = discord.Embed(title="**🔴 Please specify a youtube url to play from**",
                               description="❓ Type +help play for information about this command.",
                               color=discord.Color.yellow())
            timestamp = datetime.now()
            em.set_footer(text="Play | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await ctx.send(embed=em)
            return

        if not url.startswith('https://www.youtube.com/watch?'):
            em = discord.Embed(title="**🔴 please specify a youtube url to play from**",
                               description="❓ Type +help play for information about this command.",
                               color=discord.Color.yellow())
            timestamp = datetime.now()
            em.set_footer(text="Play | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await ctx.send(embed=em)
            return

        if ctx.author.voice is None:
            em = discord.Embed(title="**🔴 Join a voice channel to run this command**",
                               description="❓ Type +help play for information about this command.",
                               color=discord.Color.yellow())
            timestamp = datetime.now()
            em.set_footer(text="Play | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await ctx.send(embed=em)

        voice_channel = ctx.author.voice.channel
        voice_client = discord.utils.get(self.client.voice_clients, guild=ctx.guild)

        if not voice_client:
            await voice_channel.connect()

        if ctx.voice_client.is_playing():
            em = discord.Embed(title="**🔴 Run the +stop command to play another song**",
                               description="❓ Type +help play for information about this command.",
                               color=discord.Color.yellow())
            timestamp = datetime.now()
            em.set_footer(text="Play | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await ctx.send(embed=em)
            return

        voice = ctx.guild.voice_client

        YTDLP_OPTIONS = {
            'format': 'bestaudio/best',
            'extractaudio': True,
            'audioformat': 'mp3',
            'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
            'restrictfilenames': True,
            'noplaylist': True,
            'nocheckcertificate': True,
            'ignoreerrors': False,
            'logtostderr': False,
            'quiet': True,
            'no_warnings': True,
            'default_search': 'ytsearch',
            'source_address': '0.0.0.0',
        }

        with yt_dlp.YoutubeDL(YTDLP_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            playUrl = info['url']

        source = FFmpegPCMAudio(source=playUrl,
                                before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
                                options="-vn")
        await voice.play(source)

    @commands.command()
    async def pause(self, ctx):
        if not ctx.voice_client.is_playing():
            em = discord.Embed(title="**🔴 Song is already paused!**",
                               description="❓ Type +help pause for information about this command.",
                               color=discord.Color.yellow())
            timestamp = datetime.now()
            em.set_footer(text="Pause | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)

            await ctx.send(embed=em)
            return

        em = discord.Embed(description="**Audio paused!**", color=discord.Color.yellow())
        em.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
        timestamp = datetime.now()
        em.set_footer(text="Pause | " + timestamp.strftime(r"%I:%M %p"))

        await ctx.send(embed=em)
        await ctx.voice_client.pause()

    @commands.command()
    async def resume(self, ctx):
        if ctx.voice_client.is_playing():
            em = discord.Embed(title="**🔴 Song is already playing!**",
                               description="❓ Type +help resume for information about this command.",
                               color=discord.Color.yellow())
            timestamp = datetime.now()
            em.set_footer(text="Resume | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)

            await ctx.send(embed=em)
            return

        em = discord.Embed(description="**Audio resumed!**", color=discord.Color.yellow())
        em.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
        timestamp = datetime.now()
        em.set_footer(text="Resume | " + timestamp.strftime(r"%I:%M %p"))

        await ctx.send(embed=em)
        await ctx.voice_client.resume()

    @commands.command()
    async def stop(self, ctx):
        if not ctx.voice_client.is_playing():
            em = discord.Embed(title="**🔴 Song is already stopped!**",
                               description="❓ Type +help stop for information about this command.",
                               color=discord.Color.yellow())
            timestamp = datetime.now()
            em.set_footer(text="Stop | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)

            await ctx.send(embed=em)
            return

        em = discord.Embed(description="**Audio stopped!**", color=discord.Color.yellow())
        em.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
        timestamp = datetime.now()
        em.set_footer(text="Stop | " + timestamp.strftime(r"%I:%M %p"))

        await ctx.send(embed=em)
        await ctx.voice_client.stop()


async def setup(client):
    await client.add_cog(Music(client))
