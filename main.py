import discord
import sys

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(intents=intents)

@bot.event
async def on_message_delete(message):
    await bot.get_channel(int(sys.argv[2])).send('User <@'+str(message.author.id)+'> had their message deleted in <#'+str(message.channel.id)+'>: ```'+message.content+'```')

bot.run(sys.argv[1])