import discord 
from discord.ext import commands
from pr import gene, coin, emoji

#configuraciondelbot
permisos=discord.Intents.default()
permisos.message_content=True
permisos.members=True

bot=commands.Bot(command_prefix='-',intents=permisos)

@bot.event
async def on_ready():
    print('Estoy aqui :D')

@bot.command()
async def hola(ctx):
    await ctx.send(f"Hola, ¿como estas? {ctx.author.name}")
@bot.command()
async def generador(ctx):
    await ctx.send(f"Tu contraseña generada es: {gene(10)}")

@bot.command()
async def carita(ctx):
    await ctx.send(f"Tu emoji es: {emoji()}")

@bot.command()
async def moneda(ctx):
    await ctx.send(f"La moneda salio: {coin()}")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('BIENVENIDO TU')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome {member.mention} to {guild.name}!'
            await guild.system_channel.send(to_send)


client = MyClient(intents=permisos)
bot.run("La tuya")
