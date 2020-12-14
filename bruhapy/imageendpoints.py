import bruhapy
import aiohttp
import json
async def taco():
  async with aiohttp.ClientSession() as req:
    response = await req.get(f'https://bruhapi.xyz/taco')
    if response.status != 200:
      raise bruhapy.RequestError("The endpoint is having an error, either it was moved or it is currently offline.")
    rej = json.loads(await response.text())
    return rej['res']