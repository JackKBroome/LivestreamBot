import discord
import os
import time
import asyncio
from discord.ext import commands
from discord.utils import get
from time import gmtime, strftime
intents = discord.Intents.default()
intents.presences = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print("at " + str(strftime("%a, %d %b %Y %H:%M:%S ", gmtime())))
    print('------')

    botchannel = bot.get_channel(848710769713479680) # Admin Chat
    #botchannel = bot.get_channel(831171764863631410) #Game Chat
    #await botchannel.send("I hope this Message makes it into the botcommand channel, if one of the people there could just let me know if it made it that would be great!")
    embed=discord.Embed(title="Command Buttons", description="Press the Reacts to trigger the commands without typing. \nYou will have to unreact & react again if you want to trigger the effect multiple times.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/icons/701514840010784808/67e5db18e94da1ddccd47032357411af.png?size=128")
    embed.add_field(name="Give " + "\U000025B6", value="Press " + "\U000025B6" + " to give each player in 'Not in the Game' Voice channel the 'Current Game' Role", inline=False)
    embed.add_field(name="Take " + "\U000023F9", value="Press " + "\U000023F9" + " to take the 'Current Game' Role from each player in the Server.", inline=False)
    embed.add_field(name="Update " + "\U0001F504", value="Press " + "\U0001F504" + " to remove the 'Current Game' Role from each player not in a voice channel or a Cottage",inline=False)
    embed.add_field(name="Cottages " + "\U000021AA", value="Press " + "\U000021AA" + " to send all players with the 'Current Game' Role to a unique Cottage. Any player with '(ST)' at the start of their name will be put into the same first cottage together.", inline=False)
    embed.add_field(name="Town Square " + "\U00002934", value="Press " + "\U00002934" + " to send all players with the 'Current Game' to the Town Square (From Cottages & Whisper Channels)", inline=False)
    embed.add_field(name="Fearmonger Announcement " + "\U0001F631", value="Press " + "\U0001F631" + " to post a message in #Game-Chat to announce a Fearmonger has chosen a new target.", inline=False)
    embed.add_field(name="Al-Hadikhia Announcement " + "\U0001F531", value="Press " + "\U0001F531" + " to post a message in #Game-Chat to announce an Al-Hadikhia has chosen a set of players.", inline=False)
    embed.add_field(name="Psychopath RoShamBo " + "\U0001F52A", value="Press " + "\U0001F52A" + " to post a message in #Game-Chat to play Ro Sham Bo, give a countdown & ask the 2 players to press one of the 3 Emojis, the Bot does not give the results.", inline=False)

    Setup = await botchannel.send(embed=embed)
    await Setup.add_reaction("\U000025B6")
    await Setup.add_reaction("\U000023F9")
    await Setup.add_reaction("\U0001F504")
    await Setup.add_reaction("\U000021AA")
    await Setup.add_reaction("\U00002934")
    await Setup.add_reaction("\U0001F631")
    await Setup.add_reaction("\U0001F531") 
    await Setup.add_reaction("\U0001F52A")

@bot.event
async def on_reaction_add(reaction, user):
    SignupMessage = reaction.message
    botchannel = bot.get_channel(831171764863631410)
    ServerID = bot.get_guild(701514840010784808)
    botchannel = bot.get_channel(848710769713479680) # Admin Chat
    Gamingchannel = bot.get_channel(831171764863631410) #Game Chat 
    
    if reaction.emoji == "\U000025B6": #Give
        Access = 0
        Manager = discord.utils.get(ServerID.roles, name='Manager')
        STRole = discord.utils.get(ServerID.roles, name='ST')
        if STRole in user.roles:
            Access = 1
        if Manager in user.roles:
            Access = 1
        if str(user.id) == "107209184147185664":
            Access = 1
        if Access == 1:
            #emoji = ':jack:822101734519603210'
            #await ctx.message.add_reaction(emoji)

            WaitingMessage = await botchannel.send("-= Give Command currently in use by " + str(user.name)+ " at " + str(strftime("%a, %d %b %Y %H:%M:%S ", gmtime()) + "=-"))
            role = discord.utils.get(ServerID.roles, name='current game')
            guild = bot.get_guild(701514840010784808)
            NIG = bot.get_channel(701514840010784812)
            members = NIG.members
            for i in range(len(members)):
                member = members[i]
                await member.add_roles(role)
            print("-= The Give command was used by "+ str(user.name) + " at " + str(strftime("%a, %d %b %Y %H:%M:%S ", gmtime()) + "=-"))
        #else:
            #emoji = '\U000026D4'
            #await ctx.message.add_reaction(emoji)
            #print("-= The Give command was Stopped against "+ str(user.name) + " at " + str(strftime("%a, %d %b %Y %H:%M:%S ", gmtime()) + "=-"))
            await WaitingMessage.delete()

    elif reaction.emoji == "\U000023F9": #Take
        Access = 0
        Manager = discord.utils.get(ServerID.roles, name='Manager')
        STRole = discord.utils.get(ServerID.roles, name='ST')
        if STRole in user.roles:
            Access = 1
        if Manager in user.roles:
            Access = 1
        if str(user.id) == "107209184147185664":
            Access = 1
        if Access == 1:
            #emoji = '\U0001F504'
            #await ctx.message.add_reaction(emoji)
            WaitingMessage = await botchannel.send("-= Take Command currently in use by " + str(user.name)+ " at " + str(strftime("%a, %d %b %Y %H:%M:%S ", gmtime()) + "=-"))
    
    
            role = discord.utils.get(ServerID.roles, name='current game')
            guild = bot.get_guild(701514840010784808)

            members = role.members

            for i in range(len(members)):
                member = members[i]
                if str(member.bot) == "False":
                    await member.remove_roles(role)
     
            #await ctx.message.remove_reaction(emoji, bot.user)
            #emoji = ':jack:822101734519603210'
            #await ctx.message.add_reaction(emoji)
            print("-= The Take command was used successfully by " + str(user.name) + " at " + str(strftime("%a, %d %b %Y %H:%M:%S ", gmtime()) +"=-"))
            await WaitingMessage.delete()
        #else:
            #emoji = '\U000026D4'
            #await ctx.message.add_reaction(emoji)
            #print("-= The Take command was Stopped against "+ str(user.name) + " at " + str(strftime("%a, %d %b %Y %H:%M:%S ", gmtime()) + "=-"))

    elif reaction.emoji == "\U0001F504": #Update
        Access = 0
        Manager = discord.utils.get(ServerID.roles, name='Manager')
        STRole = discord.utils.get(ServerID.roles, name='ST')
        if STRole in user.roles:
            Access = 1
        if Manager in user.roles:
            Access = 1
        if str(user.id) == "107209184147185664":
            Access = 1
        if Access == 1:
            #emoji = '\U0001F504'
            #await ctx.message.add_reaction(emoji)
            WaitingMessage = await botchannel.send("-= Update Command currently in use by " + str(user.name)+ " at " + str(strftime("%a, %d %b %Y %H:%M:%S ", gmtime()) + "=-"))
            
    
            role = discord.utils.get(ServerID.roles, name='current game')
            guild = bot.get_guild(701514840010784808)
            #server channels (TS + Cottages)
            Players = []
            CurrentlyPlaying = discord.utils.get(ServerID.channels, id=701854998195339275)
            for i in range(len(CurrentlyPlaying.channels)):
                if CurrentlyPlaying.channels[i].name != "game-chat" and CurrentlyPlaying.channels[i].name != "botchannel":
                    #print(str(CurrentlyPlaying.channels[i].members))
                    #print(str(CurrentlyPlaying.channels[i].name))
                    Players = Players + CurrentlyPlaying.channels[i].members
            Cottages = discord.utils.get(ServerID.channels, id=732737371631517727)
            for i in range(len(Cottages.channels)):
                #print(str(Cottages.channels[i].members))
                #print(str(Cottages.channels[i].name))
                Players = Players + Cottages.channels[i].members        
        
            #print(str(Players))
            allmembers = role.members
            #print(members)
            #print("Length: " + str(len(members)))
            for i in range(len(allmembers)):
                member = allmembers[i]
                if str(member.bot) == "False":
                    if member not in Players:
                        await member.remove_roles(role)
         
            #await ctx.message.remove_reaction(emoji, bot.user)
            #emoji = ':jack:822101734519603210'
            #await ctx.message.add_reaction(emoji)
            print("-= The Update command was used successfully by " + str(user.name) + " at " + str(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()) +"=-"))
            await WaitingMessage.delete()
        #else:
            #emoji = '\U000026D4'
            #await ctx.message.add_reaction(emoji)
            #print("-= The Update command was Stopped against "+ str(user.name) + " at " + str(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()) + "=-"))

    elif reaction.emoji == "\U00002934": #Town Square
        Access = 0
        Manager = discord.utils.get(ServerID.roles, name='Manager')
        STRole = discord.utils.get(ServerID.roles, name='ST')
        if STRole in user.roles:
            Access = 1
        if Manager in user.roles:
            Access = 1
        if str(user.id) == "107209184147185664":
            Access = 1
        if Access == 1:
            #emoji = ':jack:822101734519603210'
            #await ctx.message.add_reaction(emoji)
            WaitingMessage = await botchannel.send("-= Town Square Moveer Command currently in use by " + str(user.name)+ " at " + str(strftime("%a, %d %b %Y %H:%M:%S ", gmtime()) + "=-"))
            role = discord.utils.get(ServerID.roles, name='current game')
            guild = bot.get_guild(701514840010784808)
            TS = discord.utils.get(ServerID.channels, id=838616394466721873)

            Players = role.members

            WatchParty = []
            WatchPartyChannel = bot.get_channel(906228131587821630)
            WatchPartyMembers = WatchPartyChannel.members
            for i in range(len(WatchPartyMembers)):
                WatchPartyMember = WatchPartyMembers[i]
                WatchParty.append(WatchPartyMembers[i])
            WatchPartyPlayers = list(set(Players) & set(WatchParty))
            for j in range(len(WatchPartyPlayers)):
                Players.remove(WatchPartyPlayers[j])
        
            for person in Players:
                Voice = person.voice
                if str(person.bot) == "False" and Voice != None:
                    await person.move_to(TS)

            print("-= The Town Square command was used by "+ str(user.name) + " at " + str(strftime("%a, %d %b %Y %H:%M:%S ", gmtime()) + "=-"))
            await WaitingMessage.delete()
                
    elif reaction.emoji == "\U000021AA": #Cottages
        Access = 0
        Manager = discord.utils.get(ServerID.roles, name='Manager')
        STRole = discord.utils.get(ServerID.roles, name='ST')
        if STRole in user.roles:
            Access = 1
        if Manager in user.roles:
            Access = 1
        if str(user.id) == "107209184147185664":
            Access = 1
        if Access == 1:
            #emoji = ':jack:822101734519603210'
            #await ctx.message.add_reaction(emoji)
            WaitingMessage = await botchannel.send("-= Cottage Moveer Command currently in use by " + str(user.name)+ " at " + str(strftime("%a, %d %b %Y %H:%M:%S ", gmtime()) + "=-"))
            role = discord.utils.get(ServerID.roles, name='current game')
            guild = bot.get_guild(701514840010784808)
            Players = []
            CurrentlyPlaying = discord.utils.get(ServerID.channels, id=701854998195339275) #Currently Playing catagory
            TS = discord.utils.get(ServerID.channels, id=838616394466721873)

            Cottages = discord.utils.get(ServerID.channels, id=732737371631517727) #All Cottage Catagories

            Players = role.members

            WatchParty = []
            WatchPartyChannel = bot.get_channel(906228131587821630)
            WatchPartyMembers = WatchPartyChannel.members
            for i in range(len(WatchPartyMembers)):
                WatchPartyMember = WatchPartyMembers[i]
                WatchParty.append(WatchPartyMembers[i])
            WatchPartyPlayers = list(set(Players) & set(WatchParty))
            for j in range(len(WatchPartyPlayers)):
                Players.remove(WatchPartyPlayers[j])
            
            Storytellers = []

            for person in Players:
                ST = str(person.nick)[0:4]
                if ST == "(ST)":
                    Storytellers.append(person)
                    Players.remove(person)
                    
            cottageNo = 0
            for person in Players:
                Voice = person.voice
                Occupied = (Cottages.channels[cottageNo+1]).members
                if str(person.bot) == "False" and Voice != None and cottageNo <= 9 and Occupied == []:
                    print(str(person))
                    print(str(cottageNo))
                    await person.move_to(Cottages.channels[cottageNo+1])
                cottageNo = cottageNo + 1

            print("-= The Cottages command was used by "+ str(user.name) + " at " + str(strftime("%a, %d %b %Y %H:%M:%S ", gmtime()) + "=-"))
            moveerchannel = bot.get_channel(831171764863631410)
            #await moveerchannel.send('!ymove "Town Square" "Night Phase" 1')
            await WaitingMessage.delete()

    elif reaction.emoji == "\U0001F631": #Fearmonger
        Access = 0
        Manager = discord.utils.get(ServerID.roles, name='Manager')
        STRole = discord.utils.get(ServerID.roles, name='ST')
        if STRole in user.roles:
            Access = 1
        if Manager in user.roles:
            Access = 1
        if str(user.id) == "107209184147185664":
            Access = 1
        if Access == 1:
            
            embed=discord.Embed(title="Fearmonger Announcement", description="Prepare for fear, something's happening here.", color=0xff0000)
            embed.set_thumbnail(url="https://wiki.bloodontheclocktower.com/images/6/64/Fearmonger_icon.png")
            embed.add_field(name="You hear in the dead of night:" , value="The Fearmonger has selected a new victim, better hope it's not you...", inline=False)
            await Gamingchannel.send(embed=embed)

    elif reaction.emoji == "\U0001F531": #Al-Hadikhia
        Access = 0
        Manager = discord.utils.get(ServerID.roles, name='Manager')
        STRole = discord.utils.get(ServerID.roles, name='ST')
        if STRole in user.roles:
            Access = 1
        if Manager in user.roles:
            Access = 1
        if str(user.id) == "107209184147185664":
            Access = 1
        if Access == 1:
            
            embed=discord.Embed(title="Al-Hadikhia Announcement", description="The Al-Hadikhia has selected some players for the great game of Life & Death, what will they choose?", color=0xff0000)
            embed.set_thumbnail(url="https://wiki.bloodontheclocktower.com/images/8/89/Al-Hadikhia_icon.png")
            embed.add_field(name="You hear in the dead of night:" , value="Once you count to three, you will see. Those who must choose to live and die will be...", inline=False)
            await Gamingchannel.send(embed=embed)

    elif reaction.emoji == "\U0001F52A": #Psychopath
        Access = 0
        Manager = discord.utils.get(ServerID.roles, name='Manager')
        STRole = discord.utils.get(ServerID.roles, name='ST')
        if STRole in user.roles:
            Access = 1
        if Manager in user.roles:
            Access = 1
        if str(user.id) == "107209184147185664":
            Access = 1
        if Access == 1:
            
            embed=discord.Embed(title="The Psychopath would like to play a little game.", description="The Storyteller says 'Ro Sham Bo Go' ", color=0xff0000)
            embed.set_thumbnail(url="https://wiki.bloodontheclocktower.com/images/8/89/Psycopath_icon.png")
            embed.add_field(name="Your Choice Awaits" , value="On the word 'Go' press an emoji to declare your choice. ", inline=False)

            #embed=discord.Embed(title="Title", description="Description", color=0xff0000)
            #embed.add_field(name="Title" , value="Description", inline=False)

            Psycho = await Gamingchannel.send(embed=embed)

            await Psycho.add_reaction("\U0001FAA8")#rock
            await Psycho.add_reaction("\U0001F9FE")#paper
            await Psycho.add_reaction("\U00002702")#scissors

    elif reaction.emoji == "\U0001FAA8": #Psychopath Rochambo bit
        if user.bot == False and reaction.message.author.id == 793621749345550376:
            #if user.nick == None:
            #    name = user
            #else:
            #    name = user.nick

            name = user.display_name
            
            #fetchMessage = await Gamingchannel.history().find(lambda m: m.author.id == 793621749345550376)
            await Gamingchannel.send(str(name) + " has chosen: ROCK!")

            #if fetchMessage.content != "":
            #    previousChoice = fetchMessage.content.split(":",1)[1]
            #    if previousChoice == " ROCK!":
            #        embed=discord.Embed(title="Draw", description="Technically didn't lose so the Psychopath will be fine", color=0xff0000)
            #        embed.set_thumbnail(url="https://wiki.bloodontheclocktower.com/images/8/89/Psycopath_icon.png")
            #        embed.add_field(name="The inital command will be not be re-executed" , value="So close, yet so Far...", inline=False)
            #        await Gamingchannel.send(embed=embed)
            #    elif previousChoice == " PAPER!":
            #        embed=discord.Embed(title=str(name) + " has Lost", description="Tough luck...", color=0xff0000)
            #        embed.set_thumbnail(url="https://wiki.bloodontheclocktower.com/images/8/89/Psycopath_icon.png")
            #        embed.add_field(name="It happened..." , value="Either they have gone, or they have survived...", inline=False)
            #        await Gamingchannel.send(embed=embed)
            #    elif previousChoice == " SCISSORS!":
            #        embed=discord.Embed(title=str(name) + " has Won", description="Congratualtions...", color=0xff0000)
            #        embed.set_thumbnail(url="https://wiki.bloodontheclocktower.com/images/8/89/Psycopath_icon.png")
            #        embed.add_field(name="It happened..." , value="Either they have gone, or they have survived...", inline=False)
            #        await Gamingchannel.send(embed=embed)
                

    elif reaction.emoji == "\U0001F9FE": #Psychopath Rochambo bit
        if user.bot == False and reaction.message.author.id == 793621749345550376:
            #if user.nick == None:
            #    name = user
            #else:
            #    name = user.nick

            name = user.display_name

            #fetchMessage = await Gamingchannel.history().find(lambda m: m.author.id == 793621749345550376)
            await Gamingchannel.send(str(name) + " has chosen: PAPER!")
            
            #print(fetchMessage.content)
            #if fetchMessage.content != "":
            #    previousChoice = fetchMessage.content.split(":",1)[1]
            #    if previousChoice == " PAPER!":
            #        embed=discord.Embed(title="Draw", description="Technically didn't lose so the Psychopath will be fine", color=0xff0000)
            #        embed.set_thumbnail(url="https://wiki.bloodontheclocktower.com/images/8/89/Psycopath_icon.png")
            #        embed.add_field(name="The inital command will be not be re-executed" , value="So close, yet so Far...", inline=False)
            #        await Gamingchannel.send(embed=embed)
            #    elif previousChoice == " SCISSORS!":
            #        embed=discord.Embed(title=str(name) + " has Lost", description="Tough luck...", color=0xff0000)
            #        embed.set_thumbnail(url="https://wiki.bloodontheclocktower.com/images/8/89/Psycopath_icon.png")
            #        embed.add_field(name="It happened...." , value="Either they have gone, or they have survived...", inline=False)
            #        await Gamingchannel.send(embed=embed)
            #    elif previousChoice == " ROCK!":
            #        embed=discord.Embed(title=str(name) + " has Won", description="Congratualtions...", color=0xff0000)
            #        embed.set_thumbnail(url="https://wiki.bloodontheclocktower.com/images/8/89/Psycopath_icon.png")
            #        embed.add_field(name="It happened...." , value="Either they have gone, or they have survived...", inline=False)
            #        await Gamingchannel.send(embed=embed)
                

    elif reaction.emoji == "\U00002702": #Psychopath Rochambo bit
        if user.bot == False and reaction.message.author.id == 793621749345550376:
            #if user.nick == None:
            #    name = user
            #else:
            #    name = user.nick

            name = user.display_name
            
            #fetchMessage = await Gamingchannel.history().find(lambda m: m.author.id == 793621749345550376)
            await Gamingchannel.send(str(name) + " has chosen: SCISSORS!")
            
            #print(fetchMessage.content)
            #if fetchMessage.content != "":
            #    previousChoice = fetchMessage.content.split(":",1)[1]
            #    if previousChoice == " SCISSORS!":
            #        embed=discord.Embed(title="Draw", description="Technically didn't lose so the Psychopath will be fine", color=0xff0000)
            #        embed.set_thumbnail(url="https://wiki.bloodontheclocktower.com/images/8/89/Psycopath_icon.png")
            #        embed.add_field(name="The inital command will be not be re-executed" , value="So close, yet so Far...", inline=False)
            #        await Gamingchannel.send(embed=embed)
            #    elif previousChoice == " ROCK!":
            #        embed=discord.Embed(title=str(name) + " has Lost", description="Tough luck....", color=0xff0000)
            #        embed.set_thumbnail(url="https://wiki.bloodontheclocktower.com/images/8/89/Psycopath_icon.png")
            #        embed.add_field(name="It happened..." , value="Either they have gone, or they have survived...", inline=False)
            #        await Gamingchannel.send(embed=embed)
            #    elif previousChoice == " PAPER!":
            #        embed=discord.Embed(title=str(name) + " has Won", description="Congratualtions...", color=0xff0000)
            #        embed.set_thumbnail(url="https://wiki.bloodontheclocktower.com/images/8/89/Psycopath_icon.png")
            #        embed.add_field(name="It happened..." , value="Either they have gone, or they have survived...", inline=False)
            #        await Gamingchannel.send(embed=embed)
                
        
        
    
    if str(user.bot) == "False" and str(SignupMessage.author.id) == "793621749345550376":
        await SignupMessage.remove_reaction(reaction, user)


@bot.command()
async def Shutdown(ctx):
    botchannel = bot.get_channel(848710769713479680)
    #botchannel = bot.get_channel(831171764863631410)
    await botchannel.send("Bot is Offline, once a new message is posted it will be active again")

@bot.command()
async def Townsquare(ctx):
    Access = 0
    Manager = discord.utils.get(ctx.guild.roles, name='Manager')
    STRole = discord.utils.get(ServerID.roles, name='ST')
    if STRole in user.roles:
        Access = 1
    if Manager in ctx.author.roles:
        Access = 1
    if str(ctx.author.id) == "107209184147185664":
        Access = 1
    if Access == 1:
        emoji = ':jack:822101734519603210'
        await ctx.message.add_reaction(emoji)
        role = discord.utils.get(ctx.guild.roles, name='current game')
        guild = bot.get_guild(701514840010784808)
        Players = []
        CurrentlyPlaying = discord.utils.get(ctx.guild.channels, id=701854998195339275) #Currently Playing catagory
        TS = discord.utils.get(ctx.guild.channels, id=838616394466721873)
        for i in range(len(CurrentlyPlaying.channels)):
            if CurrentlyPlaying.channels[i].name != "game-chat" and CurrentlyPlaying.channels[i].name != "moveeradmin":
                #print(str(CurrentlyPlaying.channels[i].members))
                #print(str(CurrentlyPlaying.channels[i].name))
                Players = Players + CurrentlyPlaying.channels[i].members
        Cottages = discord.utils.get(ctx.guild.channels, id=732737371631517727) #All Cottage Catagories
        for i in range(len(Cottages.channels)):
            #print(str(Cottages.channels[i].members))
            #print(str(Cottages.channels[i].name))
            Players = Players + Cottages.channels[i].members        
        
        for person in Players:
            await person.move_to(TS)

@bot.command()
async def Cottages(ctx):
    Access = 0
    Manager = discord.utils.get(ctx.guild.roles, name='Manager')
    STRole = discord.utils.get(ServerID.roles, name='ST')
    if STRole in user.roles:
        Access = 1
    if Manager in ctx.author.roles:
        Access = 1
    if str(ctx.author.id) == "107209184147185664":
        Access = 1
    if Access == 1:
        emoji = ':jack:822101734519603210'
        await ctx.message.add_reaction(emoji)
        role = discord.utils.get(ctx.guild.roles, name='current game')
        guild = bot.get_guild(701514840010784808)
        Players = []
        CurrentlyPlaying = discord.utils.get(ctx.guild.channels, id=701854998195339275) #Currently Playing catagory
        TS = discord.utils.get(ctx.guild.channels, id=838616394466721873)
        for i in range(len(CurrentlyPlaying.channels)):
            if CurrentlyPlaying.channels[i].name != "game-chat" and CurrentlyPlaying.channels[i].name != "botchannel":
                #print(str(CurrentlyPlaying.channels[i].members))
                #print(str(CurrentlyPlaying.channels[i].name))
                Players = Players + CurrentlyPlaying.channels[i].members
        Cottages = discord.utils.get(ctx.guild.channels, id=732737371631517727) #All Cottage Catagories
        for i in range(len(Cottages.channels)):
            #print(str(Cottages.channels[i].members))
            #print(str(Cottages.channels[i].name))
            Players = Players + Cottages.channels[i].members        
        
        for person in Players:
            await person.move_to(Cottages.channels[person])

@bot.command()
async def give(ctx):
    Access = 0
    Manager = discord.utils.get(ctx.guild.roles, name='Manager')
    STRole = discord.utils.get(ServerID.roles, name='ST')
    if STRole in user.roles:
        Access = 1
    if Manager in ctx.author.roles:
        Access = 1
    if str(ctx.author.id) == "107209184147185664":
        Access = 1
    if Access == 1:
        emoji = ':jack:822101734519603210'
        await ctx.message.add_reaction(emoji)
        role = discord.utils.get(ctx.guild.roles, name='current game')
        guild = bot.get_guild(701514840010784808)
        NIG = bot.get_channel(701514840010784812)
        #print(str(Channel))

        members = NIG.members
        #print(str(members))
        #print("Length: " + str(len(members)))
        for i in range(len(members)):
            member = members[i]
            await member.add_roles(role)
     
        #await ctx.message.remove_reaction(emoji, bot.user)
        print("-= The Give command was used by "+ str(ctx.author.name) + " at " + str(strftime("%a, %d %b %Y %H:%M:%S ", gmtime()) + "=-"))
    else:
        emoji = '\U000026D4'
        await ctx.message.add_reaction(emoji)
        print("-= The Give command was Stopped against "+ str(ctx.author.name) + " at " + str(strftime("%a, %d %b %Y %H:%M:%S ", gmtime()) + "=-"))
    
@bot.command()
async def take(ctx):

    Access = 0
    Manager = discord.utils.get(ctx.guild.roles, name='Manager')
    STRole = discord.utils.get(ServerID.roles, name='ST')
    if STRole in user.roles:
        Access = 1
    if Manager in ctx.author.roles:
        Access = 1
    if str(ctx.author.id) == "107209184147185664":
        Access = 1
    if Access == 1:
        emoji = '\U0001F504'
        await ctx.message.add_reaction(emoji)
    
    
        role = discord.utils.get(ctx.guild.roles, name='current game')
        guild = bot.get_guild(701514840010784808)

        members = role.members
        #print(str(members))
        #print(members)
        #print("Length: " + str(len(members)))
        for i in range(len(members)):
            member = members[i]
            if str(member.bot) == "False":
                await member.remove_roles(role)
     
        await ctx.message.remove_reaction(emoji, bot.user)
        emoji = ':jack:822101734519603210'
        await ctx.message.add_reaction(emoji)
        print("-= The Take command was used successfully by " + str(ctx.author.name) + " at " + str(strftime("%a, %d %b %Y %H:%M:%S ", gmtime()) +"=-"))

    else:
        emoji = '\U000026D4'
        await ctx.message.add_reaction(emoji)
        print("-= The Take command was Stopped against "+ str(ctx.author.name) + " at " + str(strftime("%a, %d %b %Y %H:%M:%S ", gmtime()) + "=-"))

@bot.command()
async def removeCG(ctx):
    
    role = discord.utils.get(ctx.guild.roles, name='current game')
    await ctx.author.remove_roles(role)
    emoji = ':jack:822101734519603210'
    await ctx.message.add_reaction(emoji)

@bot.command()
async def jack(ctx):
    
    emoji = ':jack:822101734519603210'
    await ctx.message.add_reaction(emoji)

@bot.command()
async def update(ctx):

    Access = 0
    Manager = discord.utils.get(ctx.guild.roles, name='Manager')
    STRole = discord.utils.get(ServerID.roles, name='ST')
    if STRole in user.roles:
        Access = 1
    if Manager in ctx.author.roles:
        Access = 1
    if str(ctx.author.id) == "107209184147185664":
        Access = 1
    if Access == 1:
        emoji = '\U0001F504'
        await ctx.message.add_reaction(emoji)
    
        role = discord.utils.get(ctx.guild.roles, name='current game')
        guild = bot.get_guild(701514840010784808)
        #server channels (TS + Cottages)
        Players = []
        CurrentlyPlaying = discord.utils.get(ctx.guild.channels, id=701854998195339275)
        for i in range(len(CurrentlyPlaying.channels)):
            if CurrentlyPlaying.channels[i].name != "game-chat" and CurrentlyPlaying.channels[i].name != "moveeradmin":
                #print(str(CurrentlyPlaying.channels[i].members))
                #print(str(CurrentlyPlaying.channels[i].name))
                Players = Players + CurrentlyPlaying.channels[i].members
        Cottages = discord.utils.get(ctx.guild.channels, id=732737371631517727)
        for i in range(len(Cottages.channels)):
            #print(str(Cottages.channels[i].members))
            #print(str(Cottages.channels[i].name))
            Players = Players + Cottages.channels[i].members        
        
        #print(str(Players))
        allmembers = role.members
        #print(members)
        #print("Length: " + str(len(members)))
        for i in range(len(allmembers)):
            member = allmembers[i]
            if str(member.bot) == "False":
                if member not in Players:
                    await member.remove_roles(role)
     
        await ctx.message.remove_reaction(emoji, bot.user)
        emoji = ':jack:822101734519603210'
        await ctx.message.add_reaction(emoji)
        print("-= The Update command was used successfully by " + str(ctx.author.name) + " at " + str(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()) +"=-"))

    else:
        emoji = '\U000026D4'
        await ctx.message.add_reaction(emoji)
        print("-= The Update command was Stopped against "+ str(ctx.author.name) + " at " + str(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()) + "=-"))

@bot.command()
async def cg(ctx):
    await ctx.message.author.send("Hey there Stream Member, it appears you've tried an old command. Sucks you're not as cool as Jack, but who is..."
                                  "\r\n Try !helpme for the current commands")

@bot.command()
async def helpme(ctx):
    embed=discord.Embed(title="BOTCS rolebot", description="A List of commands for both Admins & Users", color=0xe100ff)
    embed.set_thumbnail(url="https://bloodontheclocktower.com/wiki/images/8/85/Mayor_Icon.png")
    embed.add_field(name="!give (Requires Manager)", value='Assigns the "Current Game" role to each player currently connected to the "Not in the Game" Voice Channel', inline=False)
    embed.add_field(name="!take (Requires Manager)", value='Removes the "Current Game" role from each player in the Server', inline=False)
    embed.add_field(name="!update (Requires Manager)", value='Removes the "Current Game" role from each player not connected to a Whisper room or Cottage', inline=False)
    embed.add_field(name="!removeCG", value='If you currently have & want the "Current Game" role removing (please do not do this during a game as it will restrict your ability to move voice channels & stop Moveer from moving you) then you can remove the role yourself with this command', inline=False)
    embed.add_field(name="!helpme", value="Sends a DM of this message to the player who typed the command", inline=False)
    embed.add_field(name="!jack", value="Reacts, because why the Heck not ? (created as a joke, Might remove)", inline=False)
    await ctx.message.author.send(embed=embed)

@bot.command()
async def PostHelp(ctx):
    embed=discord.Embed(title="BOTCS rolebot", description="A List of commands for both Admins & Users", color=0xe100ff)
    embed.set_thumbnail(url="https://bloodontheclocktower.com/wiki/images/8/85/Mayor_Icon.png")
    embed.add_field(name="!give (Requires Manager)", value='Assigns the "Current Game" role to each player currently connected to the "Not in the Game" Voice Channel', inline=False)
    embed.add_field(name="!take (Requires Manager)", value='Removes the "Current Game" role from each player in the Server', inline=False)
    embed.add_field(name="!update (Requires Manager)", value='Removes the "Current Game" role from each player not connected to a Whisper room or Cottage', inline=False)
    embed.add_field(name="!removeCG", value='If you currently have & want the "Current Game" role removing (please do not do this during a game as it will restrict your ability to move voice channels & stop Moveer from moving you) then you can remove the role yourself with this command', inline=False)
    embed.add_field(name="!helpme", value="Sends a DM of this message to the player who typed the command", inline=False)
    embed.add_field(name="!jack", value="Reacts, because why the Heck not ? (created as a joke, Might remove)", inline=False)
    await ctx.send(embed=embed)
    
    
bot.run('NzkzNjIxNzQ5MzQ1NTUwMzc2.X-u72Q.7bU7VwqA0mtZvCaI1tI9wk_eIIw')
