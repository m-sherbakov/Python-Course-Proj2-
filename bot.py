import discord
from discord.ext import commands
import random
import os
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=discord.Intents.default())

help_message = ['hello', 'help', 'nature']
with open("token.txt", "r") as file:
    TOKEN = file.readline()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def help_me(ctx):
    await ctx.send(f'Привет! Вот что я умею: {help_message}!')

@bot.command()
async def nature(ctx):
    res = random.randint(1,2)
    if res == 1:
        img_name = random.choice(os.listdir('images'))
        with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    else:
        facts = [
            'Пластиковые отходы составляют значительную часть мусора в мировых океанах, угрожая морским животным и экосистемам. Не кидай мусор в водоемы!',
            "Выбросы автомобилей и промышленных предприятий являются основными источниками загрязнения воздуха, что вредно для здоровья людей и окружающей среды. Ходите пешком ленивые существа!",
            "Незаконная вырубка лесов приводит к утрате биоразнообразия, изменению климата и уничтожению мест обитания для многих видов животных. Харэ рубить этот лес!",
            "Полифторированные соединения (ПФАС) и другие токсичные химикаты загрязняют почву и воду, угрожая здоровью людей и животных. Закрывайте уши на уроках химии!",
            "Пластиковые микрочастицы, используемые в косметике и других продуктах, накапливаются в окружающей среде, что создает проблему загрязнения водоемов и угрожает морским организмам. Мужики, харэ краситься!",
            "Пластиковые мешки и упаковка часто выбрасываются на свалки, где они могут разлагаться сотни лет, загрязняя окружающую среду. Не выбрасывай мусор, живи с ним!",
            "Выбросы парниковых газов, таких как углекислый газ, вызывают изменение климата и глобальное потепление. Крч парниковые газы - зло",
            "Нефтяные разливы на морских и сухопутных территориях наносят серьезный ущерб экосистемам и живым организмам. Нефть - черное золото",
            "Использование пестицидов и химических удобрений в сельском хозяйстве может загрязнять почву и воду, угрожая биоразнообразию и здоровью людей. Не используйте хим. удобрения, навоз для чего?",
            "Микропластик, образующийся от разложения крупных пластиковых отходов, проникает в пищевые цепи через морских животных, что может иметь негативные последствия для здоровья человека. Отказывайтесь от пластика!"
        ]
        fact = random.choice(facts)
        await ctx.send(fact)

bot.run(TOKEN)#запуск
