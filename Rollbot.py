import discord
import re
import asyncio
import random

client = discord.Client()

token = "REDACTED"

@client.event
@asyncio.coroutine
def on_ready():
    print("I'm in")
    print(client.user)

@client.event
@asyncio.coroutine
def on_message(message):
    if message.author != client.user:
        if (message.content.startswith("Rollbot") or message.content.startswith("rollbot")):

            output = ""

            msg = message.content.lower()
            roll = re.search('(\d*)(d)(\d*)', msg)

            multiplier = int(roll.group(1))
            dice = int(roll.group(3))

            if dice == 0:

                output = "You try rolling a zero-sided die, rube."
                yield from client.send_message(message.channel, output)
                return

            if multiplier != 1:

                full_roll = []
                totalresult = 0

                for x in range(multiplier):
                    result = random.randint(1, dice)
                    totalresult += result
                    full_roll.append(result)

                for value in full_roll:
                    output += str(value) + " + "

                output = output.rstrip(' + ')
                output += ' = ' + str(totalresult)

            else:

                output = random.randint(1, dice)

            yield from client.send_message(message.channel, output)

client.run(token)

