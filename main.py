import discord
from keys import *
from paipitasse_libs import *

#### INIT CLIENT ####
default_intents = discord.Intents.default()
default_intents.members = True
client = discord.Client(intents=default_intents)

# Bot is started
@client.event
async def on_ready():
    current_guild=None

    for guild in client.guilds:
        if guild.name == GUILD:
            current_guild=guild

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name} [id: {guild.id}]'
        f'current_guild: {current_guild}'
    )


# When member join the guild
@client.event
async def on_member_join(member):
    welcome_chan=client.get_channel(WELCOME)
    general_chan=client.get_channel(GENERAL)
    await welcome_chan.send(f"{member.display_name} a rejoint le serveur !")
    await general_chan.send(member_join_guild_random_response())
    await general_chan.send(member_join_guild_random_announce(str(member.display_name)))

# When member leave the guild
@client.event
async def on_member_remove(member):
    goodbye_chan=client.get_channel(GOODBYE)
    await goodbye_chan.send(f"{member.display_name} s'est barré du serveur !")
    await goodbye_chan.send(member_leave_guild_random_response())

# Catch when member write in channel/DM
@client.event
async def on_message(message):
    if message.content == "ping":
        await message.channel.send("pong")

    if message.content == "a combien":
        await message.channel.send("A 80 à l'heure qu'on était")
        await message.channel.send("Wrrraaaaaoooooonnnnnn")

    if message.content.lower() in ["paipitasse", "le bot", "server", "/server", "serveur", "/serveur"]:
        await message.channel.send(tag_paipitasse_random_response())


client.run(TOKEN)