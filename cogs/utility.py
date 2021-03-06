import discord
from discord.ext import commands
import os
import random
import psutil
from hurry.filesize import size
import platform


class utility(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["h"])
    async def help(self, ctx):
        if ctx.guild.id in self.client.epic_servers:
            embed = discord.Embed(
                title="MOBot Help",
                colour=discord.Colour.purple()
            )
            embed.add_field(name="taq <taq>", value="Shows you the specified taq")
            embed.add_field(name="create <name> <content>", value="Creates a taq")
            embed.add_field(name="delete <taq>", value="Deletes a taq")
            embed.add_field(name="edit <name/content> <taq> <value>", value="Edits the name or the content of "
                                                                            "a taq you own")
            embed.add_field(name="list", value="Qives a list of the taqs you've created")
            embed.add_field(name="listall", value="Qives a list of the taqs (all of them)")
            embed.add_field(name="pinq", value="Qives the latency")
            embed.add_field(name="info <taq>", value="Qives info about a taq")
            embed.add_field(name="about", value="About the bot")
            embed.add_field(name="random", value="Qives a random taq")
            embed.add_field(name="credits", value="Bots credits")
            embed.add_field(name="invite", value="Invite link for MO")
            embed.add_field(name="support", value="Support server for MO")
            embed.add_field(name="vote", value="Vote link for MO")
            embed.add_field(name="patreon", value="Patreon page link for MO")
            embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/7738394075969618"
                                    "03/c32e9d106e4204ca6e68f2ec5b959c32.webp?size=1024")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="MOBot Help",
                colour=discord.Colour.purple()
            )
            embed.add_field(name="tag <tag>", value="Shows you the specified tag")
            embed.add_field(name="create <name> <content>", value="Creates a tag")
            embed.add_field(name="delete <tag>", value="Deletes a tag")
            embed.add_field(name="edit <name/content> <tag> <value>", value="Edits the name or the content of "
                                                                            "a tag you own")
            embed.add_field(name="list", value="Gives a list of the tags you've created")
            embed.add_field(name="listall", value="Gives a list of the tags (all of them)")
            embed.add_field(name="ping", value="Gives the latency")
            embed.add_field(name="info <tag>", value="Gives info about a tag")
            embed.add_field(name="about", value="About the bot")
            embed.add_field(name="random", value="Gives a random tag")
            embed.add_field(name="credits", value="Bots credits")
            embed.add_field(name="invite", value="Invite link for MO")
            embed.add_field(name="support", value="Support server for MO")
            embed.add_field(name="vote", value="Vote link for MO")
            embed.add_field(name="patreon", value="Patreon page link for MO")
            embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/7738394075969618"
                                    "03/c32e9d106e4204ca6e68f2ec5b959c32.webp?size=1024")
            await ctx.send(embed=embed)

    @commands.command(aliases=["pinq"])
    async def ping(self, ctx):
        await ctx.send(f"**{round(self.client.latency * 1000)}ms**")

    @commands.command(hidden=True)
    async def sudo(self, ctx, *args):
        if ctx.author.id in self.client.admin_ids:
            if args[0] == "reload":
                await ctx.send("reloading cogs lol")
                try:
                    for element in os.listdir("cogs"):
                        if element != "__pycache__":
                            self.client.unload_extension(f"cogs.{element.replace('.py', '')}")
                            self.client.load_extension(f"cogs.{element.replace('.py', '')}")
                    await ctx.send("done :flushed:")
                except Exception as e:
                    await ctx.send(repr(e))
            elif args[0] == "server-count" or args[0] == "servers":
                await ctx.send(len(self.client.guilds))
            elif args[0] == "fuckoff" or args[0] == "die":
                sad = ["goodbye cruel world :pensive: :v:", "why you do this to me :sob:", "bro...",
                       "fuck off i dont need you :rage:"]
                await ctx.send(random.choice(sad))
                exit()
            elif args[0] == "h":
                await ctx.send("hhhhhhhhhhhhh")
            elif args[0] == "system":
                embed = discord.Embed(
                    title="Bot System Information",
                    color=discord.Colour.purple()
                )

                embed.add_field(name="‎", value="**CPU**", inline=False)
                embed.add_field(name="CPU Usage", value=str(psutil.cpu_percent()) + "%")
                embed.add_field(name="Logical CPU Count", value=psutil.cpu_count())

                mem = psutil.virtual_memory()
                embed.add_field(name="‎", value="**Memory**", inline=False)
                embed.add_field(name="Total Memory", value=size(mem.total) + "B")
                embed.add_field(name="Available Memory", value=size(mem.available) + "B")
                embed.add_field(name="Memory Usage", value=str(mem.percent) + "%")

                disk = psutil.disk_usage("/")
                embed.add_field(name="‎", value="**Disk**", inline=False)
                embed.add_field(name="Total Space", value=size(disk.total) + "B")
                embed.add_field(name="Used Space", value=size(disk.used) + "B")
                embed.add_field(name="Free Space", value=size(disk.free) + "B")
                embed.add_field(name="Disk Usage", value=str(disk.percent) + "%")

                net = psutil.net_io_counters()
                embed.add_field(name="‎", value="**Network**", inline=False)
                embed.add_field(name="Packets Sent", value=net.packets_sent)
                embed.add_field(name="Packets Received", value=net.packets_recv)
                embed.add_field(name="Bytes Sent", value=size(net.bytes_sent) + "B")
                embed.add_field(name="Bytes Received", value=size(net.bytes_recv) + "B")

                embed.add_field(name="‎", value="**OS**", inline=False)
                embed.add_field(name="System", value=platform.system())
                if len(platform.release()) != 0:
                    embed.add_field(name="Release", value=platform.release())
                else:
                    embed.add_field(name="Release", value="???")
                if len(platform.version()) != 0:
                    embed.add_field(name="Version", value=platform.version())
                else:
                    embed.add_field(name="Release", value="???")

                await ctx.send(embed=embed)
            elif args[0] == "help":
                await ctx.send("\nthis is the list of the sudo commands:\n"
                               "reload - reloads the cogs\n"
                               "fuckoff / die - shuts the bot down\n"
                               "servers - gives the server count\n"
                               "system - gives system info")

            else:
                await ctx.send("sudo command not found :flushed:\n "
                               "\nthis is the list of the sudo commands:\n"
                               "reload - reloads the cogs\n"
                               "fuckoff / die - shuts the bot down\n"
                               "servers - gives the server count\n"
                               "system - gives system info")
        else:
            return

    @commands.command()
    async def credits(self, ctx):
        makufon = self.client.get_user(444550944110149633)
        human = self.client.get_user(429935667737264139)
        lunah = self.client.get_user(603635602809946113)
        embed = discord.Embed(
            title=":busts_in_silhouette: MOBot Credits",
            description="These are the epic people who made MOBot possible",
            colour=discord.Colour.purple()
        )
        embed.add_field(name="<:4228_discord_bot_dev:727548651001348196> Developer:", value=makufon)
        embed.add_field(name=":star: Special Thanks:", value=f"{lunah}\n{human}")
        embed.add_field(name=":computer: Library:", value=f"discord.py {discord.__version__}")
        embed.add_field(name=":floppy_disk:  DB Used:", value="SQLite")
        embed.set_footer(text="Bots name and icon by GD level MO by MenhHue and Knots (ID: 62090339)")
        await ctx.send(embed=embed)

    @commands.command()
    async def invite(self, ctx):
        await ctx.send("**You can add MO to your servers with using this link:** https://bit.ly/2UewLw5")

    @commands.command()
    async def support(self, ctx):
        await ctx.send("**Here is the invite link for the support server of MO:** https://discord.gg/6PX24ZPnDt")

    @commands.command()
    async def vote(self, ctx):
        await ctx.send("**Here is the vote link for MO:** https://top.gg/bot/773839407596961803/vote")

    @commands.command()
    async def patreon(self, ctx):
        await ctx.send("**Here is our Patreon page, I put a lot of time in the bot and would appreciate your support.**"
                       "\nhttps://www.patreon.com/mobot")


def setup(client):
    client.add_cog(utility(client))
