import asyncio
import aiohttp
import os


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def main():
    API_key = os.environ['API_TOKEN']
    city_names = ['Moscow']
    urls = []

    for city in city_names:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric'
        urls.append(fetch(url))

    result = await asyncio.gather(*urls)

    for res in result:
        print(f'{res["name"]} - {res["main"]["temp"]}°С')


if __name__ == '__main__':
    asyncio.run(main())
