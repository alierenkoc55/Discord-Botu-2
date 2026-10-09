
import discord
from discord.ext import commands
import random
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık!')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')
@bot.command()
async def heh(ctx, count_heh: int = 5):
    if count_heh < 1 or count_heh > 100:
        await ctx.send("1 ile 100 arasında bir sayı gir!")
        return
    await ctx.send("he" * count_heh)
@bot.command()
async def yazitura(ctx):
    sonuc = random.choice(["Yazı", "Tura"])
    await ctx.send(f"🪙 Sonuç: {sonuc}!")
@bot.command()
async def zar(ctx):
    sonuc = random.randint(1, 6)
    await ctx.send(f"🎲 Zar sonucu: {sonuc}")
@bot.command()
async def sayi(ctx, alt: int = 1, ust: int = 100):
    if alt > ust:
        await ctx.send("Alt sınır, üst sınırdan büyük olamaz!")
        return
    await ctx.send(f"🎯 Rastgele sayın: {random.randint(alt, ust)}")
@bot.command()
async def saka(ctx):
    sakalar = [
        "Bilgisayar neden doktora gitmiş? Virüs kapmış! 😂",
        "Kitap neden üzgünmüş? Çünkü çok sayfası varmış! 📚",
        "Matematik kitabı neden ağlamış? Çok problemi varmış! 😄"
    ]
    await ctx.send(random.choice(sakalar))
@bot.command()
async def profil(ctx, uye: discord.Member = None):
    uye = uye or ctx.author
    embed = discord.Embed(title=f"👤 {uye.display_name}", color=discord.Color.blue())
    embed.set_thumbnail(url=uye.display_avatar.url)
    embed.add_field(name="Kullanıcı adı", value=str(uye), inline=False)
    embed.add_field(name="Sunucuya katılma", value=uye.joined_at.strftime("%d.%m.%Y") if uye.joined_at else "Bilinmiyor", inline=False)
    await ctx.send(embed=embed)
bot.run("BOTUN TOKENİ BURDA OLACAK!!")
