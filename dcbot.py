import discord
import random
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

fikirler={
    "pet_sise":[
        "paket yapma",
        "3d yazıcı için flament",
        "ambalaj malzemesi",
        "kalemlik",
        "saksı",
    ],
    "kapak":[
        "mozaik pano",
        "elektirikli sandalye",
        "oyuncak araba",
    ],
    "yogurt_kabi":[
        "düzenleyici",
        "saksı",
        "kale",
        "yumurta kabı"

    ],


}

@bot.command()
async def fikir(ctx, kategori: str=None):
    if not kategori:
        await ctx.send("kategori yazmalısın. Örn: '-fikir pet_sise'")
        return
    if kategori not in fikirler:
        await ctx.send("böyle bir kategori yok")
        return
    fikir=random.choice(fikirler[kategori])
    await ctx.send(f"**Fikir:**{fikir}")


@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

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

@bot.command()
async def meme1(ctx):
    memes = ["images/meme1.jpg", "images/meme2.png"]
    secim = random.choice(memes)
    with open(secim, "rb") as f:
        await ctx.send(file=discord.File(f, secim.split("/")[-1]))

# Grup 2 (meme3, meme4)
@bot.command()
async def meme2(ctx):
    memes = ["images/meme3.jpg", "images/meme4.jpg"]
    secim = random.choice(memes)
    with open(secim, "rb") as f:
        await ctx.send(file=discord.File(f, secim.split("/")[-1]))


def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)



bot.run(">token<")
