import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from config import banned_words, PFP
import datetime
from datetime import datetime


class UserManaging(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        for i in range(len(banned_words)):
            if message.content == banned_words[i]:
                await message.delete()

                em = discord.Embed(title="🔴 **Message has been deleted**",
                                   description="Reason: **banned word included in message**)",
                                   color=discord.Color.blurple())
                timestamp = datetime.now()
                em.set_footer(text="Kick | " + timestamp.strftime(r"%I:%M %p"))
                em.set_author(name="Aesthetic", icon_url=PFP)

                await message.channel.send(embed=em)

    @commands.command(aliases=['k'])
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member = None, *, reason=None):
        if not member:
            em = discord.Embed(title="**🔴 You must specify a user to kick!**",
                               description="❓ Type +help kick for information about this command.",
                               color=discord.Color.blurple())
            timestamp = datetime.now()
            em.set_footer(text="Kick | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await ctx.send(embed=em)
            return

        if not reason:
            em = discord.Embed(title="**🔴 You must specify a reason to kick!**",
                               description="❓ Type +help ban for information about this command.",
                               color=discord.Color.blurple())
            timestamp = datetime.now()
            em.set_footer(text="Kick| " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await ctx.send(embed=em)
            return

        if member == ctx.message.author:
            em = discord.Embed(title="**🔴 You cannot kick yourself!**",
                               description="❓ Type +help kick for information about this command.",
                               color=discord.Color.blurple())
            timestamp = datetime.now()
            em.set_footer(text="Kick | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await ctx.send(embed=em)
            return

        em = discord.Embed(title="**You have been kicked from " + ctx.message.guild.name +
                                 "**\nReason: " + reason,
                           color=discord.Color.blurple())
        timestamp = datetime.now()
        em.set_footer(text="Kick | " + timestamp.strftime(r"%I:%M %p"))
        em.set_author(name="Aesthetic", icon_url=PFP)

        await member.send(embed=em)

        await member.kick(reason=reason)

        em = discord.Embed(title=f"{ctx.message.author.display_name} has kicked {member}",
                           color=discord.Color.blurple())
        timestamp = datetime.now()
        em.set_footer(text="Kick | " + timestamp.strftime(r"%I:%M %p"))
        em.set_author(name="Aesthetic", icon_url=PFP)

        await ctx.send(embed=em)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            em = discord.Embed(title="**🔴 You do not have the required permissions for that command!**",
                               description="❓ Type +help kick for information about this command.",
                               color=discord.Color.blurple())
            timestamp = datetime.now()
            em.set_footer(text="Kick Error | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await ctx.send(embed=em)

    @commands.command(aliases=['b'])
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, *, reason=None):
        if not member:
            em = discord.Embed(title="**🔴 You must specify a user to ban!**",
                               description="❓ Type +help ban for information about this command.",
                               color=discord.Color.blurple())
            timestamp = datetime.now()
            em.set_footer(text="Ban | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await ctx.send(embed=em)
            return

        if not reason:
            em = discord.Embed(title="**🔴 You must specify a reason to ban!**",
                               description="❓ Type +help ban for information about this command.",
                               color=discord.Color.blurple())
            timestamp = datetime.now()
            em.set_footer(text="Ban | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await ctx.send(embed=em)
            return

        if member == ctx.message.author:
            em = discord.Embed(title="**🔴 You cannot ban yourself!**",
                               description="❓ Type +help ban for information about this command.",
                               color=discord.Color.blurple())
            timestamp = datetime.now()
            em.set_footer(text="Ban | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await ctx.send(embed=em)
            return

        em = discord.Embed(title="**You have been banned from " + ctx.message.guild.name + "**",
                           description=f"Reason: **{reason}**",
                           color=discord.Color.blurple())
        timestamp = datetime.now()
        em.set_footer(text="Ban | " + timestamp.strftime(r"%I:%M %p"))
        em.set_author(name="Aesthetic", icon_url=PFP)

        await member.send(embed=em)
        await member.ban(reason=reason)

        em = discord.Embed(title=f"Aesthetic has banned {member}", color=discord.Color.blurple())
        timestamp = datetime.now()
        em.set_footer(text="Ban | " + timestamp.strftime(r"%I:%M %p"))
        em.set_author(name="Aesthetic", icon_url=PFP)
        await ctx.send(embed=em)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            em = discord.Embed(title="**🔴 You do not have the required permissions for that command!**",
                               description="❓ Type +help ban for information about this command.",
                               color=discord.Color.blurple())
            timestamp = datetime.now()
            em.set_footer(text="Ban | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await ctx.send(embed=em)

    # add help
    @commands.command(aliases=['bl'])
    async def ban_list(self, ctx):
        bans = [entry async for entry in ctx.guild.bans(limit=2000)]

        em = discord.Embed(title="Ban Logs", colour=discord.Color.blurple())

        times = 0
        for ban in bans:
            em.add_field(name=f"Name ", value=f"{ban.user}")
            em.add_field(name="Reason: ", value=f"{ban.reason}")
            times += 1

        if times == 0:
            em = discord.Embed(title="**🔴 Nobody is currently banned!**",
                               description="❓ Type +help ban_list for information about this command.",
                               color=discord.Color.blurple())
            timestamp = datetime.now()
            em.set_footer(text="Ban List | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await ctx.send(embed=em)
            return

        timestamp = datetime.now()
        em.set_footer(text="Ban List | " + timestamp.strftime(r"%I:%M %p"))
        em.set_author(name="Aesthetic", icon_url=PFP)

        await ctx.send(embed=em)

    # add help
    @commands.command(aliases=['ub'])
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, user=None):
        if user is None:
            em = discord.Embed(title="**🔴 You must specify a user to ban!**",
                               description="❓ Type +help unban for information about this command.",
                               color=discord.Color.blurple())
            timestamp = datetime.now()
            em.set_footer(text="Unban | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await ctx.send(embed=em)
            return

        banned_users = ctx.guild.bans()
        member_name, member_discriminator = user.split("#")

        async for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)

                em = discord.Embed(title=f"Aesthetic has unbanned {user.name}!", color=discord.Color.blurple())
                timestamp = datetime.now()
                em.set_footer(text="Unban | " + timestamp.strftime(r"%I:%M %p"))
                em.set_author(name="Aesthetic", icon_url=PFP)

                await ctx.send(embed=em)
                return

        em = discord.Embed(title="**🔴 User is not currently banned!**",
                           description="❓ Type +help unban for information about this command.",
                           color=discord.Color.blurple())
        timestamp = datetime.now()
        em.set_footer(text="Ban List | " + timestamp.strftime(r"%I:%M %p"))
        em.set_author(name="Aesthetic", icon_url=PFP)

        await ctx.send(embed=em)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            em = discord.Embed(title="**🔴 You do not have permissions to run this command!**",
                               description="❓ Type +help for information about this command.",
                               color=discord.Color.blurple())
            timestamp = datetime.now()
            em.set_footer(text="Command Error | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await ctx.send(embed=em)


async def setup(client):
    await client.add_cog(UserManaging(client))
