import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageOps
import io
import requests
import os

intents = discord.Intents.default()
intents.members = True 
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_member_join(member):
    # ايدي قناة الترحيب في سيرفر zi_9ni
    channel = bot.get_channel(1488155769617649715)
    if not channel: return

    # تحميل صورة الخلفية من رابط (عشان ما تحفظها في الجهاز)
    # حط رابط صورة الشبح هنا
    bg_url = "رابط_صورة_الشبح_المباشر" 
    bg_data = requests.get(bg_url).content
    background = Image.open(io.BytesIO(bg_data)).convert("RGBA")
    
    # سحب صورة بروفايل العضو
    pfp_url = member.display_avatar.url
    pfp_data = requests.get(pfp_url).content
    pfp = Image.open(io.BytesIO(pfp_data)).convert("RGBA")
    pfp = pfp.resize((200, 200))

    # دمج الصور
    background.paste(pfp, (400, 50), pfp)

    with io.BytesIO() as image_binary:
        background.save(image_binary, 'PNG')
        image_binary.seek(0)
        await channel.send(f"حياك الله {member.mention} في سيرفر zi_9ni!", file=discord.File(fp=image_binary, filename='welcome.png'))

# تقدر تحط التوكن هنا مباشرة أو كـ Environment Variable
bot.run('MTQ4ODYwMjU4MzAzMDQzNjAwMg.GjZNAw.OZn1wyOHSb_BTK2gdgggzvS6Zh4bGYcribJMy4')
