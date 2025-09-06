import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def topla(ctx, *sayilar: int):
    if not sayilar:
        await ctx.send("En az bir sayı girmelisin!")
        return

    toplam = sum(sayilar)
    await ctx.send(f"Girdiğin sayıların toplamı: {toplam}")

@bot.command()
async def karar(ctx, *secenekler):
    if not secenekler:
        await ctx.send("Seçenek girmelisin dostum!")
        return
    
    secim = random.choice(secenekler)
    await ctx.send(f"Bence **{secim}** 👍")



bot.run("")
