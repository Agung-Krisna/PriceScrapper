import asyncio
import aiohttp

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://www.tokopedia.com") as response:
            print("Status", response.status)
            print("Content-type", response.headers['content-type'])
            html = await response.text()
            print("Body", html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())