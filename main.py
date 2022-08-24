import nextcord
from nextcord import *
from conf import *
import datetime
import asyncio
from PIL import Image, ImageDraw, ImageFont
import colorama
from colorama import *

bot = nextcord.Client()

@bot.event
async def on_ready():
    print(Fore.BLUE + Style.BRIGHT + f"The BOT {bot.user.name} is online!" + Style.RESET_ALL)
    await bot.change_presence(activity=nextcord.Game(name="https://youtu.be/wXtfdAmGmZM"))

@bot.slash_command(name="test")
async def test(int: Interaction):
    await int.send("funk! funk!")

@bot.slash_command(name="help")
async def help(int: Interaction):
    one = nextcord.Embed(title="Die Hilfe vom Bot!", description="Dieser Command wird dir Helfen dich bei den Befehlen rechtzufinden.", color=0x73ED28)
    one.add_field(name="Test Command", value="funk! funk!")
    one.add_field(name="about_me Command", value="In diesem Command wird was über den Bot erzählt.", inline=False)
    one.add_field(name="embed Command", value="Der Command kann ein benutzerdefiniertes Embed erstellen.", inline=False)
    one.add_field(name="userinfo Command", value="Erzählt was über den Angegebenen User.", inline=False)
    one.add_field(name="create_post Command", value="Erstellt einen Antrag auf ein Postfach.", inline=False)
    one.set_thumbnail(url="https://cdn.discordapp.com/attachments/1011232327558516827/1011234129628643358/slash_commands.png")
    await int.send(embed=one)

@bot.slash_command(name="about_me")
async def about_me(int: Interaction):
    t = datetime.datetime.now()
    embed = nextcord.Embed(title="Über mich - About me", description="Hallo, dieser befehl wird ein bisschen über den Bot erzählen. Also, leeets goooo!", color=0x00eeff)
    embed.add_field(name="Erstellt:", value="Ich bin <t:1661000430:R> erstellt worden.", inline=False)
    embed.add_field(name="Datum:", value=t.strftime("%x"), inline=True)
    embed.add_field(name="Wohnsitz:", value="next Support Server", inline=True)
    embed.set_author(name="next", url="https://discord.gg/2dnzYDUV8s", icon_url="https://cdn.discordapp.com/avatars/1009888414453219520/2927530103041db91a3b88682d6c0d18.webp?size=100")    
    await int.send(embed=embed, ephemeral=True)

@bot.slash_command(name="embed")
async def embed(int: Interaction, title: str, description: str):
    embed = nextcord.Embed(title=title, description=description, color=0x73ED28)
    embed.set_author(name=int.user.name, icon_url=int.user.avatar.url)
    await int.send(embed=embed)

@bot.slash_command(name="userinfo")
async def userinfo(int: Interaction, user: Member):
    embed = nextcord.Embed(title=f"{user.name}'s Userinfo!", color=0x00eeff)
    embed.set_thumbnail(url=user.avatar.url)
    embed.add_field(name="User ID", value=f"||{user.id}||")
    embed.add_field(name="Server ID", value=f"||{user.guild.id}||", inline=False)
    embed.add_field(name="Username", value=f"{user.name}")
    await int.send(embed=embed)
    
@bot.slash_command(name="create_post")
async def create_post(int: Interaction):
    ch = bot.get_channel(1008815264386785291)
    one = nextcord.Embed(title="Erfolgreich!", description="Dein Antrag auf ein Postfach wurde gestellt!\r\nDein Antrag wird in kürze bearbeitet", color=0x73ED28)
    one.set_thumbnail(url=int.user.avatar.url)
    two = nextcord.Embed(title="Neuer Antrag auf ein Postfach!", description=f"{int.user.mention} hat einen Antrag auf ein Postfach gemacht!", color=0x73ED28)
    await int.send(embed=one)
    await ch.send(embed=two)

bot.run(token)
