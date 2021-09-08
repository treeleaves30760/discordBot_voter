import discord
from discord.ext import commands
token = "TOKEN"
bot = commands.Bot(command_prefix='>')

class Voter:
    def __init__(self, id, name, data):
        self.id = id
        self.name = name
        self.data = data
        self.reason = [0 for i in data]
        self.num = len(data)

voteList = []

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def createvote(ctx, *option):
    option = list(option)
    name = option[0]
    option = option[1:]
    for i in voteList:
        if i.id == ctx.channel.id:
            await ctx.send('Vote existed \\ 已經存在投票了')
    voteList.append(Voter(ctx.channel.id, name, option))
    embed=discord.Embed(title="Start Vote! 開始投票 ", description=f'開始 {name} 投票\nstart {name} vote', color=0xff8433)
    embed.set_author(name="Voter")
    for words in option:
        embed.add_field(name=f'選項:{words}', value=f'option:{words}', inline=False)
    embed.set_footer(text='可以使用 >voteOne 一次投一個或是 >voteSome 一次投多個(用空白間隔)\nYou can use >voteOne for one option or >voteSome for multiple options (with space between)')
    await ctx.send(embed=embed)

@bot.command()
async def deletevote(ctx):
    for i in range(len(voteList)):
        if voteList[i].id == ctx.channel.id:
            voteList.pop(i)
            break
    await ctx.send('Delete Vote! \\ 刪除投票')

@bot.command()
async def voteOne(ctx, choice: str):
    idV = ctx.channel.id
    for votes in voteList:
        if votes.id == idV:
            for opt in range(votes.num):
                if choice == votes.data[opt]:
                    votes.reason[opt] += 1
                    await ctx.send(f'You Vote {choice} \\ 你投了 {choice}')
                    break
            else:
                await ctx.send("No this option!! \\ 沒有這個選項")
            break
    else:
        await ctx.send("No Vote in this channel!! \\ 這個頻道沒有投票!!")

@bot.command()
async def voteSome(ctx, *choice):
    idV = ctx.channel.id
    for votes in voteList:
        if votes.id == idV:
            embed=discord.Embed(title="You Voted!! 你投票啦 ", description=f'你投了那些選項\nThe options you voted', color=0xff8433)
            embed.set_author(name="Voter")

            for opt in range(votes.num):
                if votes.data[opt] in choice:
                    votes.reason[opt] += 1
                    embed.add_field(name=f"選項: {votes.data[opt]}", value=f"Options: {votes.data[opt]}", inline=False)
            embed.set_footer(text="感謝投票 \n Thank for voting!!")
            await ctx.send(embed=embed)
            break
    else:
        await ctx.send("No Vote in this channel!! \\ 這個頻道沒有投票!!")

@bot.command()
async def countreason(ctx, *cmd):
    idV = ctx.channel.id
    embed=discord.Embed(title="投票結果 Vote reason", description="名稱： \nName:", color=0xff8433)
    embed.set_author(name="Voter")
    embed.set_footer(text="感謝參與~")
    for votes in voteList:
        if votes.id == idV:
            max = 0
            for opt in range(votes.num):
                if '-a' in cmd:
                    embed.add_field(name=f"選項： {votes.data[opt]} 獲得了 {votes.reason[opt]} 票", value=f"Options: {votes.data[opt]} Get {votes.reason[opt]} Votes", inline=False)
                if votes.reason[opt] > votes.reason[max]:
                    max = opt
            if '-a' in cmd:
                embed.add_field(name=f"-----我是分隔線-----", value=f"-----hr-----", inline=False)
            embed.add_field(name=f"選項： {votes.data[max]} 獲得了最高票，他獲得了 {votes.reason[max]} 票", value=f"Options: {votes.data[max]} Get the Max vote, it get {votes.reason[max]} Votes", inline=False)
            await ctx.send(embed=embed)

@bot.command()
async def v_status(ctx):
    for i in voteList:
        if i.id == ctx.channel.id:
            await ctx.send(f'目前有投票')
            break
    else:
        await ctx.send(f'目前沒有投票')

@bot.command()
async def getChannelId(ctx):
    await ctx.send(f'頻道ID: {ctx.channel.id}')

@bot.command()
async def gCI(ctx):
    await ctx.send(f'頻道ID: {ctx.channel.id}')

@bot.command()
async def intro(ctx):
    embed=discord.Embed(title="自我介紹 Self introduction", url="https://github.com/treeleaves30760/discordBot_voter", description="這是自我介紹訊息 This is the self introduction message", color=0xff8433)
    embed.set_author(name="NightTangerine")
    embed.add_field(name="這個機器人是提供投票系統", value="This Bot offer a system to Vote in Discord", inline=False)
    embed.add_field(name="我的YT頻道 My Youtube channel", value="https://www.youtube.com/c/%E5%A4%9C%E6%A9%98%E5%AF%A6%E6%B3%81", inline=False)
    embed.add_field(name="我的Twitch My twitch", value="https://www.twitch.tv/treeleaves30760", inline=False)
    embed.set_footer(text="謝謝使用")
    await ctx.send(embed=embed)


while True:
    bot.run(token)