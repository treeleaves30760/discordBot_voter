import discord
from discord.ext import commands
token = "TOKEN"
bot = commands.Bot(command_prefix='>')

class Voter:
    def __init__(self, id, data):
        self.id = id
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
    for i in voteList:
        if i.id == ctx.channel.id:
            await ctx.send('Vote existed \\ 已經存在投票了')
    voteList.append(Voter(ctx.channel.id, option))
    await ctx.send('Start Vote! \\ 開始投票')

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
            for opt in range(votes.num):
                if votes.data[opt] in choice:
                    votes.reason[opt] += 1
                    await ctx.send(f'You Vote {votes.data[opt]} \\ 你投了 {votes.data[opt]}')
            break
    else:
        await ctx.send("No Vote in this channel!! \\ 這個頻道沒有投票!!")

@bot.command()
async def countreason(ctx, *cmd):
    idV = ctx.channel.id
    for votes in voteList:
        if votes.id == idV:
            max = 0
            for opt in range(votes.num):
                if '-a' in cmd:
                    await ctx.send(f'option {votes.data[opt]} gain {votes.reason[opt]} votes \\ 選項 {votes.data[opt]} 獲得了 {votes.reason[opt]} 票')
                if votes.reason[opt] > votes.reason[max]:
                    max = opt

            await ctx.send(f'The max vote option {votes.data[max]} gain {votes.reason[max]} votes \\ 獲得最高票的選項 {votes.data[max]} 獲得了 {votes.reason[max]} 票')

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


while True:
    bot.run(token)