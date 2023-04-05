import asyncio
import discord
from discord.ext import commands
import random
from random import shuffle
from config import words, wordle_list, PFP
from datetime import datetime


class SmallGames(commands.Cog, discord.ui.View):
    def __init__(self, client):
        super().__init__()
        self.client = client

    @commands.command(aliases=['coin', 'toss', 'ct'])
    async def coin_toss(self, ctx):
        rand = random.randint(1, 2)
        face = ""

        if rand == 1:
            face = "**Heads!**"
        elif rand == 2:
            face = "**Tails!**"

        em = discord.Embed(title=face, color=discord.Color.red())
        timestamp = datetime.now()
        em.set_footer(text="Coin Toss | " + timestamp.strftime(r"%I:%M %p"))
        em.set_author(name="Aesthetic", icon_url=PFP)
        
        await ctx.send(embed=em)

    @commands.command()
    async def rps(self, ctx, move=None):
        if move is None:
            em = discord.Embed(title="**🔴 Enter a move in order to play!** (rock, paper, or scissors)",
                               description="**❓ Run +help rps for a list of commands**",
                               color=discord.Color.red())
            timestamp = datetime.now()
            em.set_footer(text="Rock Paper Scissors | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)
            
            await ctx.send(embed=em)
            return

        rand = random.randint(1, 3)
        counter = "."
        outcome = "."

        if rand == 1:
            counter = "rock"
        elif rand == 2:
            counter = "paper"
        elif rand == 3:
            counter = "scissors"

        if move == "rock" or move == "paper" or move == "scissors":
            if move == counter:
                outcome = "**it\'s a tie!**"
            elif move == "rock" and counter == "paper":
                outcome = "**You lose!**"
            elif move == "rock" and counter == "scissors":
                outcome = "**You win!**"
            elif move == "paper" and counter == "scissors":
                outcome = "**You lose!**"
            elif move == "paper" and counter == "rock":
                outcome = "**You win!**"
            elif move == "scissors" and counter == "rock":
                outcome = "**You lose!**"
            elif move == "scissors" and counter == "paper":
                outcome = "**You win!**"
        else:
            em = discord.Embed(title="**🔴 Make sure you typed your move in lowercase and spelled it correctly!**",
                               description="**❓ Run +help rps for a list of commands**",
                               color=discord.Color.red())
            timestamp = datetime.now()
            em.set_footer(text="Rock Paper Scissors | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await ctx.send(embed=em)
            return

        em = discord.Embed(title=outcome,
                           description=f"Your move: **{move}**\nOpponent\'s move: **{counter}**",
                           color=discord.Color.red())
        timestamp = datetime.now()
        em.set_footer(text="Rock Paper Scissors | " + timestamp.strftime(r"%I:%M %p"))
        em.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
        
        await ctx.send(embed=em)

    @commands.command(aliases=['scram'])
    async def scramble(self, ctx):
        rand = random.randint(0, len(words) - 1)
        word = words[rand]
        list_scrambled = list(word)
        shuffle(list_scrambled)
        output = "".join(list_scrambled)

        em = discord.Embed(title=f"**The scrambled word is: {output}**",
                           description="Unscramble the word to win!",
                           color=discord.Color.red())
        timestamp = datetime.now()
        em.set_footer(text="Scramble | " + timestamp.strftime(r"%I:%M %p"))
        em.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)

        await ctx.send(embed=em)

        def check(m):
            return m.author == ctx.author

        try:
            msg = await self.client.wait_for("message", check=check, timeout=60)
        except asyncio.TimeoutError:
            em = discord.Embed(title="🔴 Response too late (Time limit: 60 seconds)",
                               color=discord.Color.red())
            timestamp = datetime.now()
            em.set_footer(text="Scramble | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)

            await ctx.send(embed=em)
            return

        if msg.content.lower() == word:
            em = discord.Embed(title=f"**You win! the word was: {word}**", color=discord.Color.red())
            timestamp = datetime.now()
            em.set_footer(text="Scramble | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)

            await ctx.send(embed=em)
        else:
            lose_embed = discord.Embed(title=f"**🔴 Sorry, the word was: {word}**", color=discord.Color.red())
            timestamp = datetime.now()
            em.set_footer(text="Scramble | " + timestamp.strftime(r"%I:%M %p"))
            lose_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)

            await ctx.send(embed=lose_embed)

    @commands.command(aliases=['wd'])
    async def wordle(self, ctx):
        em = discord.Embed(title="**Thanks for playing Wordle!**",
                           description="**Bolded** letters mean the letter is in the spot"
                                       "\n__Underlined__ letters mean the letter is in the word, "
                                       "but in a different spot",
                           color=discord.Color.red())
        timestamp = datetime.now()
        em.set_footer(text="Wordle | " + timestamp.strftime(r"%I:%M %p"))
        em.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)

        await ctx.send(embed=em)

        rand = random.randint(0, len(wordle_list) - 1)
        word = wordle_list[rand].lower()

        def check(m):
            return m.author == ctx.author

        attempts = 5
        while attempts > 0:
            try:
                msg = await self.client.wait_for("message", check=check, timeout=60)
            except asyncio.TimeoutError:
                em = discord.Embed(title="🔴 Response too late (Time limit: 60 seconds)",
                                   color=discord.Color.red())
                timestamp = datetime.now()
                em.set_footer(text="Wordle | " + timestamp.strftime(r"%I:%M %p"))
                em.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)

                await ctx.send(embed=em)
                return

            output = ""
            if len(msg.content) != 5:
                em = discord.Embed(title="**🔴 Your guess must be 5 letters long!**",
                                   description="**❓ Run +help wordle for a list of commands**",
                                   color=discord.Color.red())
                timestamp = datetime.now()
                em.set_footer(text="Wordle | " + timestamp.strftime(r"%I:%M %p"))
                em.set_author(name="Aesthetic", icon_url=PFP)
                await ctx.send(embed=em)
                continue

            guess = str(msg.content).lower()

            if guess == word:
                em = discord.Embed(title="**🎉 Congratulations! You won!**",
                                   description="The word was: " + word,
                                   color=discord.Color.red())
                timestamp = datetime.now()
                em.set_footer(text="Wordle | " + timestamp.strftime(r"%I:%M %p"))
                em.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)

                await ctx.send(embed=em)
                return

            correct_letters = {
                letter for letter, correct in zip(guess, word) if letter == correct
            }

            misplaced_letters = set(guess) & set(word) - correct_letters

            for i in range(5):
                found = False

                if guess[i] == word[i]:
                    output += f"**{guess[i].upper()}** "
                    found = True
                else:
                    if guess[i] in misplaced_letters:
                        output += f"__{guess[i].upper()}__ "
                        misplaced_letters.remove(guess[i])
                        found = True

                if not found:
                    output += guess[i].upper() + " "

            attempts -= 1

            if attempts > 0:
                em = discord.Embed(description=f"{output}\n\n**Bolded** letters mean the letter is in the spot"
                                               "\n__Underlined__ letters mean the letter is in the word, "
                                               "but in a different spot",
                                   color=discord.Color.red())
                em.add_field(name="Attempts left", value=attempts)
                timestamp = datetime.now()
                em.set_footer(text="Wordle | " + timestamp.strftime(r"%I:%M %p"))
                em.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)

                await ctx.send(embed=em)

        em = discord.Embed(title="**🔴 You ran out of attempts! Try again next time!**",
                           description="The word was: " + word,
                           color=discord.Color.red())
        timestamp = datetime.now()
        em.set_footer(text="Wordle | " + timestamp.strftime(r"%I:%M %p"))
        em.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)

        await ctx.send(embed=em)


async def setup(client):
    await client.add_cog(SmallGames(client))
