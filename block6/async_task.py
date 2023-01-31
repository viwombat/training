import aiohttp
import asyncio
import time
from bs4 import BeautifulSoup

# GOOGLE_BOOKS_URL = f"https://www.googleapis.com/books/vl/volumes?q=isbn:" doesn't work
BOOKS_URL = 'https://openlibrary.org/isbn/'
LIST_ISBN = [
    '9780002005883',
    '9780002238304',
    '9780002261982',
    '9780006163831',
    '9780006178736',
    '9780006280897',
    '9780006280934',
    '9780006353287',
    '9780006380832',
    '9780006470229',
]


async def fetch(client, book):
    async with client.get(f'{BOOKS_URL}{book}') as response:
        return await response.text()


async def main():
    start = time.time()

    async with aiohttp.ClientSession() as client:

        info = await asyncio.gather(*(fetch(client, isbn) for isbn in LIST_ISBN))

        for html in info:
            soup = BeautifulSoup(html, 'html.parser')
            name = soup.find('h1', class_='work-title')
            author = soup.find('a', itemprop="author")
            print(f'"{name.text}", {author.text}')
            new_time = round(time.time() - start, 2)
            print(new_time)

    print(f'The task took: {round(time.time() - start, 2)} sec')

asyncio.run(main())
# loop = asyncio.new_event_loop()
# loop.run_until_complete(main())
# loop.close()
