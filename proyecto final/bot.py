import discord
from discord.ext import commands
from pr import maq, map, cho

permisos=discord.Intents.default()
permisos.message_content=True
permisos.members=True

bot=commands.Bot(command_prefix='¿',intents=permisos)

@bot.event
async def on_ready():
    print('Im here :I')

@bot.command()
async def hola(ctx):
    await ctx.send(f"Hola, ¿como estas?, ¿¿en que necesitas ayuda?? {ctx.author.name} escribe menu para más opciones")

@bot.command()
async def menu(ctx):
    await ctx.send("maquetas para el cole= mc, maquetas personales= mp, consejos para el hogar= ch")

@bot.command()
async def mc(ctx):
    await ctx.send(f"Algunos consejos para maquetas escolares serian: {maq()}")

@bot.command()
async def mp(ctx):
        await ctx.send(f"Algunos consejos para maquetas personales serian: {map()}")

@bot.command()
async def ch(ctx):
    await ctx.send(f"Algunos consejos para disminuir la contaminacion en el hogar: {cho()}")

@bot.command()
async def gracias(ctx):
    await ctx.send(f"¡Con gusto, {ctx.author.name}! 🌟")

@bot.command()
async def ayuda(ctx):
    await ctx.send(f"{ctx.author.name}, Escribe menu para más opciones 😊")

@bot.command()
async def ok(ctx):
    await ctx.send(f"¿Qué ‘ok’ de qué? Dime ‘gracias’, mij@.")

bot.run(".")