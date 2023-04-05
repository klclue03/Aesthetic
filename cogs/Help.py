import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime
import googletrans
from config import PFP


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="help", description="Find information about the commands Aesthetic supports!")
    async def help(self, interaction: discord.Interaction, command: str = None):
        if command is None:
            em = discord.Embed(title="**Support has arrived!**",
                               description="**Use +help [command] for more information on a command**",
                               color=discord.Color.random())

            em.add_field(name="**Administrative**", value="kick, ban, unban, ban_list", inline=False)
            em.add_field(name="**Games**", value="coin_toss, rps, scramble, wordle", inline=False)
            em.add_field(name="**Generator**", value="joke, meme, animal", inline=False)
            em.add_field(name="**Music**", value="join, disconnect, play, pause, resume, stop", inline=False)
            em.add_field(name="**Roles**", value="role, user, nick", inline=False)
            em.add_field(name="**Utilities**", value="translate, calculator, poll, timer, reminder", inline=False)

            timestamp = datetime.now()
            em.set_footer(text="Help | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await interaction.response.send_message(embed=em)
        elif command == "kick":
            em = discord.Embed(title="**Kick**", color=discord.Color.random())
            em.add_field(name="What is it?", value="Kicks a specified member (must have administrative permissions)",
                         inline=False)
            em.add_field(name="How to run", value="+kick [member]", inline=False)
            em.add_field(name="Aliases", value="+k", inline=False)

            timestamp = datetime.now()
            em.set_footer(text="Help | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await interaction.response.send_message(embed=em)
        elif command == "ban":
            em = discord.Embed(title="**Ban**", color=discord.Color.random())
            em.add_field(name="What is it?", value="Bans a specified member (must have administrative permissions)",
                         inline=False)
            em.add_field(name="How to run", value="+ban [member]", inline=False)
            em.add_field(name="Aliases", value="+b", inline=False)

            timestamp = datetime.now()
            em.set_footer(text="Help | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await interaction.response.send_message(embed=em)
        elif command == "unban":
            em = discord.Embed(title="**Unban**", color=discord.Color.random())
            em.add_field(name="What is it?", value="Unbans a specified user that was previously banned "
                                                   "(must have administrative permissions)",
                         inline=False)
            em.add_field(name="How to run", value="+unban [user]", inline=False)
            em.add_field(name="Aliases", value="+ub", inline=False)

            timestamp = datetime.now()
            em.set_footer(text="Help | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await interaction.response.send_message(embed=em)
        elif command == "ban_list":
            em = discord.Embed(title="**Ban List**", color=discord.Color.random())
            em.add_field(name="What is it?", value="Displays a list of current bans in the server (limit 2000)",
                         inline=False)
            em.add_field(name="How to run", value="+ban_list", inline=False)
            em.add_field(name="Aliases", value="+bl", inline=False)

            timestamp = datetime.now()
            em.set_footer(text="Help | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await interaction.response.send_message(embed=em)
        elif command == "coin_toss":
            em = discord.Embed(title="**Coin Toss**", color=discord.Color.random())
            em.add_field(name="What is it?", value="Flips a coin which lands either heads or tails",
                         inline=False)
            em.add_field(name="How to run", value="+coin_toss", inline=False)
            em.add_field(name="Aliases", value="+coin, +toss, +ct", inline=False)

            timestamp = datetime.now()
            em.set_footer(text="Help | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await interaction.response.send_message(embed=em)
        elif command == "rps":
            em = discord.Embed(title="**Rock, Paper, Scissors**", color=discord.Color.random())
            em.add_field(name="What is it?", value="Play Rock, Paper, Scissors against Aesthetic"
                                                   "(Enter either rock, paper, or scissors)",
                         inline=False)
            em.add_field(name="How to run", value="+rps [move]", inline=False)
            em.add_field(name="Aliases", value="None", inline=False)

            timestamp = datetime.now()
            em.set_footer(text="Help | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await interaction.response.send_message(embed=em)
        elif command == "scramble":
            em = discord.Embed(title="**Scramble**", color=discord.Color.random())
            em.add_field(name="What is it?", value="Unscramble a random word to win!",
                         inline=False)
            em.add_field(name="How to run", value="+scramble", inline=False)
            em.add_field(name="Aliases", value="+scram", inline=False)

            timestamp = datetime.now()
            em.set_footer(text="Help | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await interaction.response.send_message(embed=em)
        elif command == "wordle":
            em = discord.Embed(title="**Wordle**", color=discord.Color.random())
            em.add_field(name="What is it?", value="Play Wordle using discord"
                                                   "\n**Bolded** letters mean the letter is in the spot"
                                                   "\n__Underlined__ letters mean the letter is in the word, "
                                                   "but in a different spot",
                         inline=False)
            em.add_field(name="How to run", value="+wordle", inline=False)
            em.add_field(name="Aliases", value="+wd", inline=False)

            timestamp = datetime.now()
            em.set_footer(text="Help | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await interaction.response.send_message(embed=em)
        elif command == "joke":
            em = discord.Embed(title="**Joke**", color=discord.Color.random())
            em.add_field(name="What is it?", value="Generates a random joke",
                         inline=False)
            em.add_field(name="How to run", value="+joke", inline=False)
            em.add_field(name="Aliases", value="+j", inline=False)

            timestamp = datetime.now()
            em.set_footer(text="Help | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await interaction.response.send_message(embed=em)
        elif command == "meme":
            em = discord.Embed(title="**Meme**", color=discord.Color.random())
            em.add_field(name="What is it?", value="Generates a random meme from r/memes",
                         inline=False)
            em.add_field(name="How to run", value="+meme", inline=False)
            em.add_field(name="Aliases", value="+m", inline=False)

            timestamp = datetime.now()
            em.set_footer(text="Help | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await interaction.response.send_message(embed=em)
        elif command == "animal":
            em = discord.Embed(title="**Animal**", color=discord.Color.random())
            em.add_field(name="What is it?", value="Generates a random photo of an animal from r/aww",
                         inline=False)
            em.add_field(name="How to run", value="+animal", inline=False)
            em.add_field(name="Aliases", value="+a, +an", inline=False)

            timestamp = datetime.now()
            em.set_footer(text="Help | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await interaction.response.send_message(embed=em)
        elif command == "disconnect":
            em = discord.Embed(title="**Disconnect**", color=discord.Color.random())
            em.add_field(name="What is it?", value="Aesthetic disconnects from your current voice channel",
                         inline=False)
            em.add_field(name="How to run", value="+disconnect", inline=False)
            em.add_field(name="Aliases", value="+dc", inline=False)

            timestamp = datetime.now()
            em.set_footer(text="Help | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await interaction.response.send_message(embed=em)
        elif command == "play":
            em = discord.Embed(title="**Play**", color=discord.Color.random())
            em.add_field(name="What is it?", value="Plays audio in a voice channel from a specific url",
                         inline=False)
            em.add_field(name="How to run", value="+play [url]", inline=False)
            em.add_field(name="Aliases", value="+p", inline=False)

            timestamp = datetime.now()
            em.set_footer(text="Help | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await interaction.response.send_message(embed=em)
        elif command == "pause":
            em = discord.Embed(title="**Pause**", color=discord.Color.random())
            em.add_field(name="What is it?", value="Pauses currently playing audio in voice channel",
                         inline=False)
            em.add_field(name="How to run", value="+pause", inline=False)
            em.add_field(name="Aliases", value="None", inline=False)

            timestamp = datetime.now()
            em.set_footer(text="Help | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await interaction.response.send_message(embed=em)
        elif command == "resume":
            em = discord.Embed(title="**Resume**", color=discord.Color.random())
            em.add_field(name="What is it?", value="Resumes currently paused audio in voice channel",
                         inline=False)
            em.add_field(name="How to run", value="+resume", inline=False)
            em.add_field(name="Aliases", value="None", inline=False)

            timestamp = datetime.now()
            em.set_footer(text="Help | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await interaction.response.send_message(embed=em)
        elif command == "stop":
            em = discord.Embed(title="**Stop**", color=discord.Color.random())
            em.add_field(name="What is it?", value="Stops currently playing audio in voice channel",
                         inline=False)
            em.add_field(name="How to run", value="+stop", inline=False)
            em.add_field(name="Aliases", value="None", inline=False)

            timestamp = datetime.now()
            em.set_footer(text="Help | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await interaction.response.send_message(embed=em)
        elif command == "role":
            em = discord.Embed(title="**Role**", color=discord.Color.random())
            em.add_field(name="What is it?", value="Gives a role to a specified member "
                                                   "(run command again to remove the role)",
                         inline=False)
            em.add_field(name="How to run", value="+role [member] [role]", inline=False)
            em.add_field(name="Aliases", value="+r", inline=False)

            timestamp = datetime.now()
            em.set_footer(text="Help | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await interaction.response.send_message(embed=em)
        elif command == "user":
            em = discord.Embed(title="**User**", color=discord.Color.random())
            em.add_field(name="What is it?", value="Displays information about a specified member:"
                                                   "\nDate user created, date joined, roles, nicknames, and status",
                         inline=False)
            em.add_field(name="How to run", value="+user [member]", inline=False)
            em.add_field(name="Aliases", value="+u", inline=False)

            timestamp = datetime.now()
            em.set_footer(text="Help | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await interaction.response.send_message(embed=em)
        elif command == "nick":
            em = discord.Embed(title="**Nickname**", color=discord.Color.random())
            em.add_field(name="What is it?", value="Nickname a specified member",
                         inline=False)
            em.add_field(name="How to run", value="+nick [member] [member]", inline=False)
            em.add_field(name="Aliases", value="+n", inline=False)

            timestamp = datetime.now()
            em.set_footer(text="Help | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await interaction.response.send_message(embed=em)
        elif command == "translate":
            em = discord.Embed(title="**Translate**", color=discord.Color.random())
            em.add_field(name="What is it?", value="Translate a phrase into another language\n"
                                                   "Run +help language_codes for information about language codes",
                         inline=False)
            em.add_field(name="How to run", value="+translate [language code] [phrase]", inline=False)
            em.add_field(name="Aliases", value="+trans", inline=False)

            timestamp = datetime.now()
            em.set_footer(text="Help | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await interaction.response.send_message(embed=em)
        elif command == "language_codes":
            content = ""
            for language in googletrans.LANGUAGES:
                content += f"\n{language}: {googletrans.LANGUAGES[language]}"

            em = discord.Embed(title="**Supported language codes:**",
                               description=content,
                               color=discord.Color.random())
            timestamp = datetime.now()
            em.set_footer(text="Help | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await interaction.response.send_message(embed=em)
        elif command == "calculator":
            em = discord.Embed(title="**Translate**", color=discord.Color.random())
            em.add_field(name="What is it?", value="Add, subtract, multiply, or divide two decimal numbers\n"
                                                   "**Supported operations:** +, -, *, /",
                         inline=False)
            em.add_field(name="How to run", value="+calculator [number 1] [operation] [number 2]", inline=False)
            em.add_field(name="Aliases", value="+calc, +c", inline=False)

            timestamp = datetime.now()
            em.set_footer(text="Help | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await interaction.response.send_message(embed=em)
        elif command == "poll":
            em = discord.Embed(title="**Poll**", color=discord.Color.random())
            em.add_field(name="What is it?", value="Make a poll with two options (react to vote)",
                         inline=False)
            em.add_field(name="How to run", value="+poll [option 1] [option 2] [question]", inline=False)
            em.add_field(name="Aliases", value="None", inline=False)

            timestamp = datetime.now()
            em.set_footer(text="Help | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await interaction.response.send_message(embed=em)
        elif command == "timer":
            em = discord.Embed(title="**Timer**", color=discord.Color.random())
            em.add_field(name="What is it?", value="Set a timer in seconds (Will ping you when time is up)",
                         inline=False)
            em.add_field(name="How to run", value="+timer [seconds]", inline=False)
            em.add_field(name="Aliases", value="+t, +time", inline=False)

            timestamp = datetime.now()
            em.set_footer(text="Help | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await interaction.response.send_message(embed=em)
        elif command == "reminder":
            em = discord.Embed(title="**Reminder**", color=discord.Color.random())
            em.add_field(name="What is it?", value="Set a reminder (Will ping you when time is up)",
                         inline=False)
            em.add_field(name="How to run", value="+reminder [seconds] [description]", inline=False)
            em.add_field(name="Aliases", value="+remind", inline=False)

            timestamp = datetime.now()
            em.set_footer(text="Help | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await interaction.response.send_message(embed=em)
        else:
            em = discord.Embed(title="**🔴 Command of that name doesn't exists**",
                               description="**❓ Run +help for a list of commands**",
                               color=discord.Color.random())
            timestamp = datetime.now()
            em.set_footer(text="Help Error | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await interaction.response.send_message(embed=em)


async def setup(client):
    await client.add_cog(Help(client))
