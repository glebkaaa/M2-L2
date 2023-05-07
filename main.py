import discord
from emoji import emojize
from random import choice
from credits import bot_token
from discord.ext import commands
from data import about_env, channels, advice, data

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command()
async def show(ctx):
    await ctx.send('Привет! Я думаю, если ты зашел сюда, то ты хочешь изменить мир к лучшему 🌅' + '\n' + 'Вот список того, что я умею: ' + '\n' + '$about - коротко о проблеме загрязнения окружающей среды 🌎' + '\n' + '$should - несколько советов как можно помочь окружающей среде 🙋' + '\n' + emojize('$info - немного статистики :information:') + '\n' + '$channel - случайная ссылка на полезное сообщество про экологию 🔗')


@bot.command()
async def channel(ctx):
    await ctx.send(f'{choice(channels)}' + '\n' + 'Канал англоязычный, используй субтитры, русскую озвучку(при помощи нейросети) 🗽')


@bot.command()
async def info(ctx):
    await ctx.send(emojize('Случайный факт из мира статистики: :information:') + '\n' + choice(data))


@bot.command()
async def about(ctx):
    await ctx.send(about_env)


@bot.command()
async def should(ctx):
    await ctx.send('Случайный совет, который поможет подросткам уменьшить выброс мусора 🗑️:' + '\n' + choice(advice))


bot.run(bot_token)
