import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions
from datetime import datetime
from config import PFP


class Roles(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['r'])
    @commands.has_permissions(administrator=True)
    async def role(self, ctx, user: discord.Member = None, *, role: discord.Role = None):
        if user is None:
            em = discord.Embed(title="**🔴 Please who you want to give the role to!**",
                               description="❓ Type +help role for information about this command.",
                               color=discord.Color.dark_orange())
            timestamp = datetime.now()
            em.set_footer(text="Role | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)
            
            await ctx.send(embed=em)
            return

        if role is None:
            em = discord.Embed(title="**🔴 Please which role you want to give!**",
                               description="❓ Type +help role for information about this command.",
                               color=discord.Color.dark_orange())
            timestamp = datetime.now()
            em.set_footer(text="Role | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)
            
            await ctx.send(embed=em)
            return

        if role in user.roles:
            await user.remove_roles(role)
            em = discord.Embed(title=f"Removed {role} from {user.name}", color=discord.Color.dark_orange())
            timestamp = datetime.now()
            em.set_footer(text="Role | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)
            
            await ctx.send(embed=em)
        else:
            await user.add_roles(role)
            em = discord.Embed(title=f"Added {role} to {user.name}", color=discord.Color.blurple())
            timestamp = datetime.now()
            em.set_footer(text="Role | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)
            
            await ctx.send(embed=em)

    @commands.command(aliases=['+n'])
    @commands.has_permissions(administrator=True)
    async def nick(self, ctx, member: discord.Member = None, *, nickname=None):
        if member is None:
            em = discord.Embed(title="**🔴 Please specify the member you want to nickname!**",
                               description="❓ Type +help nick for information about this command.",
                               color=discord.Color.dark_orange())
            timestamp = datetime.now()
            em.set_footer(text="Nick | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)
            
            await ctx.send(embed=em)
            return

        if nickname is None:
            em = discord.Embed(title="**🔴 Please specify the nickname!**",
                               description="❓ Type +help nick for information about this command.",
                               color=discord.Color.dark_orange())
            timestamp = datetime.now()
            em.set_footer(text="Nick | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)
            
            await ctx.send(embed=em)
            return

        await member.edit(nick=nickname)

        em = discord.Embed(title=f"**{member.name}'s nickname has been changed to {nickname}**",
                           color=discord.Color.blurple())
        timestamp = datetime.now()
        em.set_footer(text="Nick | " + timestamp.strftime(r"%I:%M %p"))
        
        em.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
        await ctx.send(embed=em)

    @role.error
    async def role_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            em = discord.Embed(title="**🔴 You do not have permission to use this command!**",
                               description="❓ Type +help for information about this command.",
                               color=discord.Color.dark_orange())
            timestamp = datetime.now()
            em.set_footer(text="Role Error | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)

            await ctx.send(embed=em)

    @commands.command(aliases=['u'])
    async def user(self, ctx, member: discord.Member = None):
        if member is None:
            em = discord.Embed(title="**🔴 Please specify the user!**",
                               description="❓ Type +user for information about this command.",
                               color=discord.Color.dark_orange())
            timestamp = datetime.now()
            em.set_footer(text="Join | " + timestamp.strftime(r"%I:%M %p"))
            em.set_author(name="Aesthetic", icon_url=PFP)
            await ctx.send(embed=em)
            return

        em = discord.Embed(title=f"**About {member.name}:**", color=discord.Color.blurple())

        em.add_field(name="Created at", value=member.created_at.strftime("%A, %B %d %Y"), inline=False)
        em.add_field(name="Joined server at", value=member.joined_at.strftime("%A, %B %d %Y"), inline=False)

        message = ""
        numRoles = 0
        for role in member.roles:
            if role.name == '@everyone':
                continue
            message += role.name + "\n"
            numRoles += 1

        if numRoles == 0:
            message = "None"

        em.add_field(name="Roles", value=message, inline=False)
        em.add_field(name="Nickname", value=member.nick, inline=False)
        em.add_field(name="Status", value=str(member.status), inline=False)

        em.set_author(name=member.display_name, icon_url=member.avatar)
        em.set_thumbnail(url=str(member.avatar.url))

        await ctx.send(embed=em)


async def setup(client):
    await client.add_cog(Roles(client))
