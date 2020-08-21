import random
import discord
import discord.ext
from discord.ext import commands

# invite: https://discord.com/oauth2/authorize?client_id=706864322445312021&scope=bot&permissions=8

client = commands.Bot(command_prefix='.')  # woah trendy

# defines a few emojis for reactions
thumbemoji = "👍"
roflemoji = "🤣"
whatemoji = "❓"

# says when the bot is ready
@client.event
async def on_ready() :
    print('Bot is ready. Logged in as Keyboard Rewritten#2166')

@client.event
async def on_message(message) :
    if message.content == ".help" :
        embed = discord.Embed(title="Help on Keyboard Rewritten", description="Some useful commands")
        embed.add_field(name=".memes", value=" Get some fresh memes straight into your DMs! Updated daily.")
        embed.add_field(name=".invite", value="Invite the bot to your server!")
        embed.add_field(name=".subscribe", value="Road to 50 subs :sunglasses:")
        embed.add_field(name=".donate", value="Help a friend out!")
        await message.channel.send(content=None, embed=embed)




    elif message.content.find(".subscribe") != -1 :
        await message.channel.send("Ayo! Click here to sub to my youtube channel! https://bit.ly/Tic_Sub :ok_hand: ")



    # react to certain messages
    elif message.content.find("nice") != -1 :
        await message.add_reaction(thumbemoji)
        print('Reacted to message containing nice')
    elif message.content.find("lmao") != -1 :
        await message.add_reaction(roflemoji)
        print('Reacted to message containing lmao')



    # who pinged me
    elif message.content.find("Keyboard Rewritten") != -1 :
        await message.channel.send("https://i.kym-cdn.com/photos/images/newsfeed/001/366/521/ac3.gif")
        print('wtf someone pinged me')


    # USES LINE BREAKS - \n --- how to code?
    elif message.content.find("how to code?") != -1 :
        await message.channel.send(
            "`if life = true \nthen  set.life = 0\nelse \n      print (oh shit he's already dead)`:flushed:` \n end`")
        await message.add_reaction(whatemoji)



    # discord activity commands

    elif message.content.find("!status play") != -1 :
        await client.change_presence(activity=discord.Game(name='Roblox'))
        await message.channel.send(":white_check_mark: Set playing status. ")
        print('Changed to playing status.')

    elif message.content.find("!status watch") != -1 :
        activity = discord.Activity(name='code being written', type=discord.ActivityType.watching)
        await client.change_presence(activity=activity)
        await message.channel.send(":white_check_mark: Set main watching status. ")
        print('Changed to main watching status.')


    elif message.content.find("!status ad") != -1 :
        activity = discord.Activity(name='TicTacTNT on youtube!', type=discord.ActivityType.watching)
        await client.change_presence(activity=activity)
        await message.channel.send(":white_check_mark: Set advertisement status. ")
        print('Changed to ad status.')


    elif message.content.find("!status listen") != -1 :
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Spotify"))
        await message.channel.send(":white_check_mark: Set listening status. ")
        print('Changed to listening status.')


    # invite the bot [dms]
    elif message.content.find(".invite") != -1 :
        await message.channel.send(":white_check_mark: Check your dms, I sent you a bot invite link!")
        await message.author.send(
            'Here is the invite you requested: https://discord.com/oauth2/authorize?client_id=706864322445312021&scope=bot&permissions=8 ')

    # hq memes delivered to ur dms :clap:
    elif message.content.find(".memes") != -1 :
        await message.channel.send("Sent you some high quality memes, check your DMs!")
        await message.author.send(
            'https://i.pinimg.com/originals/16/6b/c3/166bc3d89b01f32a69f0d0e1c9a96529.jpg https://i.pinimg.com/originals/d2/d6/46/d2d646ef93598e0f62d37693e71624b1.png https://i.pinimg.com/236x/e8/19/cb/e819cb507d0504c2ee88c47ebc045411--just-do-it-meme.jpg ')

    # dm stuff [beta]
    elif message.content.find("!dm") != -1 :
        await message.author.send('test')




    elif message.content == ".botpresence" :
        embed = discord.Embed(title="Status Activities", description="Change the bot's status. ")
        embed.add_field(name="!status play", value=":video_game: Sets playing status.")
        embed.add_field(name="!status watch", value=" :tv: Sets main watching status.")
        embed.add_field(name="!status ad", value=" :^) woah no way free ads!1!!1")
        embed.add_field(name="!status listen", value=" :headphones: Sets listening status.")
        await message.channel.send(content=None, embed=embed)


    elif message.content == ".donate" :
        embed = discord.Embed(title="Donate", description="Help a friend out! ")
        embed.add_field(name="PayPal", value="alecpay1@iname.com")
        embed.add_field(name="Bitcoin", value="19tsKT5FDTQaHaqy6ZQhsDzVd7M5meSMeo")

        await message.channel.send(content=None, embed=embed)


client.run("p")


