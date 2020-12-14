import json
import aiohttp

class Response(object):
  """The translation object"""
  def __init__(self,dictionary):
    self.res = dictionary['res']
    self.query = dictionary['query']

async def cb(text):
  async with aiohttp.ClientSession() as session:
    response = await session.get(f'https://bruhapi.xyz/cb/{text}')
    rej = json.loads(await response.text())
    return Response(rej)

async def sponge(text):
  async with aiohttp.ClientSession() as session:
    response = await session.get(f'https://bruhapi.xyz/sponge/{text}')
    rej = json.loads(response.text)
    return rej['res']

async def tts(text):
  async with aiohttp.ClientSession() as session:
    response = await session.get(f'https://bruhapi.xyz/tts/{text}')
    rej = json.loads(response.text)
    return rej['res']