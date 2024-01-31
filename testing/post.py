import aiohttp
import asyncio

async def post_request():
    url = "http://uxhebxje.ddns.net:1199"
    data = {"key": "value"}

    async with aiohttp.ClientSession() as session:
        response = await session.post(url, json=data)
        print(await response.json())

asyncio.run(post_request())