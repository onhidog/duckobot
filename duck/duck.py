import discord
import random
import time
import os

client = discord.Client()
client.time_stamp_wisdom=time.time()
client.time_stamp_bad=time.time()
client.time_stamp_wisdom-=60

bad_words=['fuck','merda']

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    elif message.content.split(' ')[0]=='!commands':
        cmd_list = open('duck/cmd_list.txt','r')
        msg = cmd_list.read()
        cmd_list.close()
        await client.send_message(message.channel, msg)

    # if 'bot' in message.content:
    #     msg = 'Oi? boi! Tas a falar de mim?? --__ {0.author.mention}'.format(message)
    #     await client.send_message(message.channel, msg)
    #
    # if any(word in message.content for word in bad_words):
    #     msg = 'Olha a linguagem!! Bem... --__ {0.author.mention}'.format(message)
    #     await client.send_message(message.channel, msg)

    # if message.content.startswith('!members'):
    #     # msg=''
    #     # for x in chan.members:
    #     #     msg += 'x.userID'.format(message)
    #     msg='Welcome {0.mention} to {1.name}!'.format(message)
    #     await client.send_message(message.channel, msg)

    elif message.content.split(' ')[0]=='!hello':
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    elif message.content.split(' ')[0]=='!duck':
        msg = '--__'.format(message)
        await client.send_message(message.channel, msg)

    elif message.content.split(' ')[0]=='!duckest':
        msg = '<@434695524634066955> is the duckest of all ducks!!'.format(message)
        await client.send_message(message.channel, msg)

    elif message.content.split(' ')[0]=='!quack':
        msg = 'QUACK!!. QUACK!!.'.format(message)
        await client.send_message(message.channel, msg, tts=True)

    elif message.content.split(' ')[0]=='!quackmf':
        msg = 'QUACK, QUACK! MOTHER FUCKER QUACK!!'.format(message)
        await client.send_message(message.channel, msg, tts=True)

    elif message.content.split(' ')[0]=='!guess':
        await client.send_message(message.channel, 'Guess a number between 1 to 10')

        def guess_check(m):
            return m.content.isdigit()

        guess = await client.wait_for_message(timeout=5.0, author=message.author, check=guess_check)
        answer = random.randint(1, 10)
        if guess is None:
            fmt = 'Sorry, you took too long. It was {}.'
            await client.send_message(message.channel, fmt.format(answer))
            return
        if int(guess.content) == answer:
            await client.send_message(message.channel, 'You are right!')
        else:
            await client.send_message(message.channel, 'Sorry. It is actually {}.'.format(answer))

    elif message.content.split(' ')[0]=='!tableflip':
        msg = '(╯°°___）╯︵ ┻━┻'.format(message)
        await client.send_message(message.channel, msg)

    elif message.content.split(' ')[0]=='!wisdom':
        if time.time() < client.time_stamp_wisdom + 60:
            msg = 'Master <@434695524634066955> is coming up with his next piece of wisdom. Please wait a bit.'
        else:
            msg = random.choice(list(open('duck/quotes.txt'))).format(message)
            client.time_stamp_wisdom = time.time()
        await client.send_message(message.channel, msg)


###########################################################################################
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


token = os.environ['DISCORD_TOKEN']
client.run(token)
