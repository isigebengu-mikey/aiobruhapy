import requests
import json
import aiohttp
class Translation(object):
  """The translation object"""
  def __init__(self,dictionary):
    self.lang = dictionary['lang']
    self.tr = dictionary['text']
    self.original = dictionary['original']

async def joke():
  async with aiohttp.ClientSession() as session:
    response = await session.get(f'https://bruhapi.xyz/joke/')
    rej = json.loads(await response.text())
    return rej['res']

async def translate(text):
  async with aiohttp.ClientSession() as session:
    response = await session.get(f'https://bruhapi.xyz/translate/{text}')
    rej = json.loads(await response.text())
    return Translation(rej)