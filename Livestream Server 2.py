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

bot = commands.Bot(command_prefix='!JackWantsAnErrorMessage', intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print("at " + str(strftime("%a, %d %b %Y %H:%M:%S ", gmtime())))
    print('------')

@bot.event
async def on_reaction_add(reaction, user):
    SignupMessage = reaction.message
    botchannel = bot.get_channel(831171764863631410)
    ServerID = bot.get_guild(701514840010784808)
    botchannel = bot.get_channel(848710769713479680) # Admin Chat
    Gamingchannel = bot.get_channel(831171764863631410) #Game Chat
    
    
    if reaction.emoji == "\U00002934": #Town Square
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
            WaitingMessage = await botchannel.send("-= Town Square Moveer (on Bot 2) Command currently in use by " + str(user.name)+ " at " + str(strftime("%a, %d %b %Y %H:%M:%S ", gmtime()) + "=-"))
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

            count = 0
            for person in Players:
                Voice = person.voice
                if str(person.bot) == "False" and Voice != None and count >= 10:
                    
                    await person.move_to(TS)
                count = count + 1

            print("-= The Town Square (on Bot 2) command was used by "+ str(user.name) + " at " + str(strftime("%a, %d %b %Y %H:%M:%S ", gmtime()) + "=-"))
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
            WaitingMessage = await botchannel.send("-= Cottage Moveer Command (on Bot 2) currently in use by " + str(user.name)+ " at " + str(strftime("%a, %d %b %Y %H:%M:%S ", gmtime()) + "=-"))
            role = discord.utils.get(ServerID.roles, name='current game')
            guild = bot.get_guild(701514840010784808)
            Players = []
            CurrentlyPlaying = discord.utils.get(ServerID.channels, id=701854998195339275) #Currently Playing catagory
            TS = discord.utils.get(ServerID.channels, id=838616394466721873)

            Cottages = discord.utils.get(ServerID.channels, id=732737371631517727) #All Cottage Catagories

            Players = role.members
            #print("List of players: " + str(Players))

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
                #print("All Player's name: " + ST)
                if ST == "(ST)":
                    Storytellers.append(person)
                    Players.remove(person)
                    #print("ST Nickname: " + str(person.nick))
            #print("List of ST: " + str(Storytellers))
                    
            cottageNo = 0
            for person in Players:
                Voice = person.voice
                Occupied = (Cottages.channels[cottageNo+1]).members
                if str(person.bot) == "False" and Voice != None and cottageNo >= 10 and Occupied == []:
                    print(str(person))
                    print(str(cottageNo))
                    await person.move_to(Cottages.channels[cottageNo+1])
                cottageNo = cottageNo + 1

            for st in Storytellers:
                Voice = st.voice
                if str(st.bot) == "False" and Voice != None:
                    await st.move_to(Cottages.channels[0])

            print("-= The Cottages (on Bot 2) command was used by "+ str(user.name) + " at " + str(strftime("%a, %d %b %Y %H:%M:%S ", gmtime()) + "=-"))
            await WaitingMessage.delete()

bot.run('ODUyNTgwMTIxMDU5MTMxMzky.YMI5HQ.sjMlucwXgbvZ3o6jsKFcNzdDbdg')
