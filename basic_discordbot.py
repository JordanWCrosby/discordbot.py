#your imports 
import discord
from discord.ext import commands
import os
import random
from discord.utils import get


#command Prefix(common ones are / - ! ? . )
client = commands.Bot(command_prefix = 'special_character_here')

#this is related to cogs
#@client.command()
#async def load(ctx, extension):
   # client.load_extension(f'cogs.{extension}')

# prints to console that the bot has logged in
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# checks server for a channel name and welcomes a user in that channel when they join.
@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "Your_channel_name_here": # We check to make sure we are sending the message in the general channel
            await channel.send(f"""Ahoy hoy {member.mention}""")

# rolls a 20 sided die
@client.command(aliases=['role20', 'd20'])
async def rolld20(ctx):
    result = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
    await ctx.send(f'You Rolled a {random.choice(result)}')

#embeds a post in regards to self-assigning roles ro a specific discord channel
@client.command(pass_context=True)
#setting a specific role lock on this command.
@commands.has_role('your_role_name_here')
async def rolls(ctx):
    channel = client.get_channel(your_channel_id_here)
     embed = discord.Embed(
            title = "Your Embed title",
            description = "Your Embed description",
            colour = discord.Colour.green()
        )
    embed.set_author(name="ROLES HERE, GET YOUR ROLES:", icon_url='https://cdn.discordapp.com/attachments/732933689901711481/732960583464517683/419_REpWIExBVSAzMDUtOTE.jpg')
    embed.add_field(name="To Add Minecraft Role:", value="react with <:minecraft:732946372759650435> to add the minecraft role", inline=False)
    embed.add_field(name="To Add Switch Role:", value="react with <:switch:732946283026972813> to add the switch role", inline=False)
    embed.add_field(name="To Add Animal Crossing Role:", value="react with <:animalcrossing:732946235258044530> to add the animalcrossing role", inline=False)
    await channel.send(embed=embed)
#error handler for someone trying to use this command without permissions    
@rolls.error
async def roll_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingRole):
        await ctx.send('You do not have permissions to use this command.')
# help command.
@client.command()
async def h(ctx):
    embed = discord.Embed(
            title = "Your Embed title",
            description = "Your Embed description",
            colour = discord.Colour.green()
        )
    embed.add_field(name="Add roles:", value="Visit the channel #role-assign and react with the appropriate emote", inline=False)
    embed.add_field(name="Commands:", value="COMMAND LIST", inline=False)
    embed.add_field(name="!h", value="that's how you access this that you're reading right now!", inline=False)
    embed.add_field(name="!d20", value="rolls a twenty sided die", inline=False)
    embed.add_field(name="!coin", value="millybot tosses a coin", inline=False)

    await ctx.send(embed=embed)


#flips a coin and returns an emoji of either the heads or tails face of a Canadian nickel(note you will need to add these customer emoji to your server)
@client.command()
async def coin(ctx):
#emote ids can be found by typing "\:emoji:" in discord, however you can just used text in this as well.
    faces = ['your_heads_emote_id', 'your_tails_emote_id']
    flip = random.choice(faces)

    await ctx.send(str(flip))

#clears a user defined number of messages.
@client.command()
@commands.has_role('Your_admin_role_here')
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)

#assigns a role based on the name of the emoji on reaction to a specific message.
@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == your_message_id_here:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
        if payload.emoji.name == 'emoji_name_here':
            role = discord.utils.get(guild.roles, name='role_name_here')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                print("done")
            else:
                print("member not found.")
        else:
            print("role note found.")

#unassigns a role based on the name of the emoji on reaction to a specific message.
@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == your_message_id_here:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
        if payload.emoji.name == 'emoji_name_here':
            role = discord.utils.get(guild.roles, name='role_name_here')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
                print("done")
            else:
                print("member not found.")
        else:
            print("role note found.")
            
#this is related to cogs
#for filename in os.listdir('.\cogs'):
    #if filename.endswith('.py'):
     #   client.load_extension(f'cogs.{filename[:-3]}')


#this is where you put your API call generated at discord.com
client.run('TOKEN GOES HERE')