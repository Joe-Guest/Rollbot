import discord
import re
import asyncio
import random

#Setup client and connect to servers that have granted access to Rollbot
client = discord.Client()

token = "Your Token Here"

@client.event
@asyncio.coroutine
def on_ready():
    print("I'm in")
    print(client.user)

#Listen to messages on all channels for mention of Rollbot
@client.event
@asyncio.coroutine
def on_message(message):
    if message.author != client.user:
        if (message.content.startswith("Rollbot") or message.content.startswith("rollbot")):

            output = ""

            msg = message.content.lower()
            roll = re.search('(\d*)(d)(\d*)', msg) #Search message for formatted roll like 1d20

            multiplier = int(roll.group(1)) #First int represents the number of dice to roll
            dice = int(roll.group(3)) #Second int represents how many sides the dice have

            #I added this if statement because my friends were being cheeky and tried to break the bot
            if dice == 0: 

                output = "You try rolling a zero-sided die, rube."
                yield from client.send_message(message.channel, output)
                return

            #Only go into loops if there are multiple dice being rolled
            if multiplier != 1:

                full_roll = [] #Array of rolled results
                totalresult = 0 #Sum of rolled results
                
                for x in range(multiplier):
                    result = random.randint(1, dice) #Generates a random number between 1 and the number of sides the dice have
                    totalresult += result 
                    full_roll.append(result)

                for value in full_roll:
                    output += str(value) + " + " #Formats output string but the second for loop is probably unnecessary 

                #Final formatting of string: roll 1 + roll 2 + roll n = total
                output = output.rstrip(' + ') 
                output += ' = ' + str(totalresult)

            #If only one die is being rolled Rollbot just generates and prints a random number
            else:

                output = random.randint(1, dice)

            yield from client.send_message(message.channel, output)

client.run(token)

