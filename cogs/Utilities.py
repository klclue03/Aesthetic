import discord
import googletrans
from discord.ext import commands
from googletrans import Translator
from datetime import datetime
import asyncio
from config import PFP


class Utilities(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['trans'])
    async def translate(self, ctx, language=None, *, word=None):
        if language is None:
            em = discord.Embed(title="**🔴 Please specify the language code of the language**",
                               description="❓ Type +help language_codes for information about this command.",
                               color=discord.Color.purple())
            timestamp = datetime.now()
            em.set_footer(text="Translate | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)
            
            await ctx.send(embed=em)
            return

        inCodes = False
        if language in googletrans.LANGUAGES:
            inCodes = True

        if not inCodes:
            em = discord.Embed(title="**🔴 Invalid language code!**",
                               description="❓ Type +help language_codes for information about this command.",
                               color=discord.Color.purple())
            timestamp = datetime.now()
            em.set_footer(text="Translate | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await ctx.send(embed=em)
            return

        if word is None:
            em = discord.Embed(title="**🔴 Please specify the word you want to translate!**",
                               description="❓ Type +help translate for information about this command.",
                               color=discord.Color.purple())
            timestamp = datetime.now()
            em.set_footer(text="Translate | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await ctx.send(embed=em)
            return
        
        translator = Translator()
        translated = translator.translate(word, dest=language)

        em = discord.Embed(title=f"\"{word}\" in {googletrans.LANGUAGES[language].capitalize()}:",
                           description=translated.text,
                           color=discord.Color.purple())
        timestamp = datetime.now()
        em.set_footer(text="Translate | " + timestamp.strftime(r"%I:%M %p"))

        em.set_author(name="Aesthetic", icon_url=PFP)
        await ctx.send(embed=em)

    @commands.command(aliases=['calc', 'c'])
    async def calculator(self, ctx, a=None, operation=None, b=None):
        if (a is None) or (b is None):
            em = discord.Embed(title="**🔴 Please specify the numbers, or put a space between the"
                                     " operation and the numbers!**",
                               description="❓ Type +help calculator for information about this command.",
                               color=discord.Color.purple())
            timestamp = datetime.now()
            em.set_footer(text="Calculator | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)
            
            await ctx.send(embed=em)
            return

        if operation is None:
            em = discord.Embed(title="**🔴 Please specify the operation!**",
                               description="❓ Type +help calculator for information about this command.",
                               color=discord.Color.purple())
            timestamp = datetime.now()
            em.set_footer(text="Calculator | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)
            
            await ctx.send(embed=em)
            return

        if operation == "+":
            answer = round(float(a) + float(b), 3)

            em = discord.Embed(title=f"{a} + {b} =", 
                               description=f"**{answer}**",
                               color=discord.Color.purple())
            timestamp = datetime.now()
            em.set_footer(text="Calculator | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await ctx.send(embed=em)
        elif operation == "-":
            answer = round(float(a) - float(b), 3)

            em = discord.Embed(title=f"{a} - {b} =",
                               description=f"**{answer}**",
                               color=discord.Color.purple())
            timestamp = datetime.now()
            em.set_footer(text="Calculator | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await ctx.send(embed=em)
        elif operation == "*":
            answer = round(float(a) * float(b), 3)

            em = discord.Embed(title=f"{a} * {b} =",
                               description=f"**{answer}**",
                               color=discord.Color.purple())
            timestamp = datetime.now()
            em.set_footer(text="Calculator | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await ctx.send(embed=em)
        elif operation == "/":
            answer = round(float(a) / float(b), 3)

            em = discord.Embed(title=f"{a} / {b} =",
                               description=f"**{answer}**",
                               color=discord.Color.purple())
            timestamp = datetime.now()
            em.set_footer(text="Calculator | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await ctx.send(embed=em)

    @commands.command()
    async def poll(self, ctx, choice1=None, choice2=None, *, question=None):
        if (choice1 is None) or (choice2 is None):
            em = discord.Embed(title="**🔴 Please specify the choices!**",
                               description="❓ Type +help poll for information about this command.",
                               color=discord.Color.purple())
            timestamp = datetime.now()
            em.set_footer(text="Poll | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await ctx.send(embed=em)
            return

        if question is None:
            em = discord.Embed(title="**🔴 Please specify the question!**",
                               description="❓ Type +help poll for information about this command.",
                               color=discord.Color.purple())
            timestamp = datetime.now()
            em.set_footer(text="Poll | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await ctx.send(embed=em)
            return

        em = discord.Embed(title=f"**{question}**")
        em.add_field(name="choices:", value=f"🔴 {choice1}\n🔵 {choice2}")
        timestamp = datetime.now()
        em.set_footer(text="Timer | " + timestamp.strftime(r"%I:%M %p"))
        em.set_author(name="poll by " + ctx.author.display_name, icon_url=ctx.author.avatar)

        message = await ctx.send(embed=em)

        await message.add_reaction('🔴')
        await message.add_reaction('🔵')

    @commands.command(aliases=['t', 'time'])
    async def timer(self, ctx, seconds=None):
        if seconds is None:
            em = discord.Embed(title="**🔴 Please specify a time in seconds!**",
                               description="❓ Type +help timer for information about this command.",
                               color=discord.Color.purple())
            timestamp = datetime.now()
            em.set_footer(text="Timer | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await ctx.send(embed=em)
            return

        try:
            numSeconds = int(seconds)
            if numSeconds > 86400:
                em = discord.Embed(title="**🔴 Cannot set a timer for more than 86400 seconds!**",
                                   description="❓ Type +help timer for information about this command.",
                                   color=discord.Color.purple())
                timestamp = datetime.now()
                em.set_footer(text="Timer | " + timestamp.strftime(r"%I:%M %p"))
                em.set_author(name="Aesthetic", icon_url=PFP)

                await ctx.send(embed=em)
                return
            if numSeconds <= 0:
                em = discord.Embed(title="**🔴 Cannot set a timer for less than one second!**",
                                   description="❓ Type +help timer for information about this command.",
                                   color=discord.Color.purple())
                timestamp = datetime.now()
                em.set_footer(text="Timer | " + timestamp.strftime(r"%I:%M %p"))
                em.set_author(name="Aesthetic", icon_url=PFP)

                await ctx.send(embed=em)
                return

            em = discord.Embed(title=f"**Timer: {numSeconds}**",
                               color=discord.Color.purple())
            em.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
            message = await ctx.send(embed=em)

            while True:
                numSeconds -= 1
                if numSeconds == 0:
                    em = discord.Embed(title=f"**Ended!**",
                                       color=discord.Color.purple())
                    em.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)

                    await message.edit(embed=em)
                    await ctx.send(f"{ctx.author.mention}")
                    break

                em = discord.Embed(title=f"**Timer: {numSeconds}**",
                                   color=discord.Color.purple())
                em.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)

                await message.edit(embed=em)
                await asyncio.sleep(1)
        except ValueError:
            em = discord.Embed(title="**Value must be a number!**",
                               description="❓ Type +help timer for information about this command.",
                               color=discord.Color.purple())
            timestamp = datetime.now()
            em.set_footer(text="Timer | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await ctx.send(embed=em)

    @commands.command(aliases=['remind'])
    async def reminder(self, ctx, time=None, *, reminder=None):
        if time is None:
            em = discord.Embed(title="**🔴 Please specify the time of the reminder!**",
                               description="❓ Type +help reminder for information about this command.",
                               color=discord.Color.purple())
            timestamp = datetime.now()
            em.set_footer(text="Reminder | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await ctx.send(embed=em)
            return

        user = ctx.message.author
        numSeconds = int(time)

        if reminder is None:
            em = discord.Embed(title="**🔴 Please specify what your reminder will be!**",
                               description="❓ Type +help reminder for information about this command.",
                               color=discord.Color.purple())
            timestamp = datetime.now()
            em.set_footer(text="Reminder | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await ctx.send(embed=em)
            return

        if numSeconds >= 604800:
            em = discord.Embed(title="**🔴 Time cannot be for over a week!**",
                               description="❓ Type +help reminder for information about this command.",
                               color=discord.Color.purple())
            timestamp = datetime.now()
            em.set_footer(text="Reminder | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await ctx.send(embed=em)
            return

        if numSeconds <= 0:
            em = discord.Embed(title="**🔴 Time cannot be less than one second!**",
                               description="❓ Type +help reminder for information about this command.",
                               color=discord.Color.purple())
            timestamp = datetime.now()
            em.set_footer(text="Reminder | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await ctx.send(embed=em)
            return

        em = discord.Embed(title=f"Ok, i will remind you about:",
                           description=f"**{reminder}**",
                           color=discord.Color.purple())
        timestamp = datetime.now()
        em.set_footer(text="Reminder | " + timestamp.strftime(r"%I:%M %p"))
        em.set_author(name="Aesthetic", icon_url=PFP)

        await ctx.send(embed=em)
        await asyncio.sleep(numSeconds)

        em = discord.Embed(title=f"Hey {user.name}, you wanted me to remind you about:",
                           description=f"**{reminder}**",
                           color=discord.Color.purple())
        timestamp = datetime.now()
        em.set_footer(text="Reminder | " + timestamp.strftime(r"%I:%M %p"))
        em.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)

        await ctx.send(embed=em)
        await ctx.send(f"{ctx.author.mention}")


async def setup(client):
    await client.add_cog(Utilities(client))
