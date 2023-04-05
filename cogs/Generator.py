import discord
from discord.ext import commands
import requests
import json
import praw
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_PASSWORD, PFP
from datetime import datetime


class Generator(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['j'])
    async def joke(self, ctx):
        def jokes(x):
            data = requests.get(x)
            tt = json.loads(data.text)
            return tt

        f = r"https://official-joke-api.appspot.com/random_joke"
        a = jokes(f)

        em = discord.Embed(title=a["setup"], description="**" + a["punchline"] + "**",
                           color=discord.Color.green())
        timestamp = datetime.now()
        em.set_footer(text="Joke | " + timestamp.strftime(r"%I:%M %p"))
        em.set_author(name="Aesthetic", icon_url=PFP)

        await ctx.send(embed=em)

    @commands.command(aliases=['m'])
    async def meme(self, ctx):
        reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID, client_secret=REDDIT_CLIENT_SECRET,
                             username="pqsitive", password=REDDIT_PASSWORD, user_agent="meme")

        subreddit = reddit.subreddit("memes")
        submission = subreddit.random()

        while True:
            if submission.domain == 'i.redd.it':
                break

            submission = subreddit.random()

        name = submission.title
        url = submission.url

        em = discord.Embed(title=f"**{name}**", color=discord.Color.green())
        em.set_image(url=url)
        timestamp = datetime.now()
        em.set_footer(text="Meme | " + timestamp.strftime(r"%I:%M %p"))
        em.set_author(name="Aesthetic", icon_url=PFP)

        await ctx.send(embed=em)

    @commands.command(aliases=['a', 'an'])
    async def animal(self, ctx):
        reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID, client_secret=REDDIT_CLIENT_SECRET,
                             username="pqsitive", password=REDDIT_PASSWORD, user_agent="animals")

        subreddit = reddit.subreddit("aww")
        submission = subreddit.random()

        while True:
            if submission.domain == 'i.redd.it':
                break

            submission = subreddit.random()

        url = submission.url

        em = discord.Embed(color=discord.Color.green())
        em.set_image(url=url)
        timestamp = datetime.now()
        em.set_footer(text="Animal | " + timestamp.strftime(r"%I:%M %p"))
        em.set_author(name="Aesthetic", icon_url=PFP)

        await ctx.send(embed=em)


async def setup(client):
    await client.add_cog(Generator(client))
