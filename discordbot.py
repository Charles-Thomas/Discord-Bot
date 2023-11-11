import discord
import random
import requests
import json
import config

def get_meme():# gets meme from api 
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

prompts = ['Sup loser, have a beatiful day', 
           'Hi! I love you<3','Yall look like bofa...like YALL BOFA NEED A HUG',
           'im here for you','im listening','Help when you can!', 'Start recycling.']

class MyClient(discord.Client): # starts the interaction with the dicord api 
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    guild_count =  0

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$Migi'):# responds with random string from prompts list
            await message.channel.send(random.choice(prompts))
        
        if message.content.startswith('$meme'): #gets meme from get_meme funtion 
            await message.channel.send(get_meme())


intents = discord.Intents.default() #dicord bot permissons 
intents.message_content = True

client = MyClient(intents=intents)
client.run(config.api_key) #api key

