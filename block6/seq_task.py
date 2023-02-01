import time
import requests
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


def main(book):
    with requests.get(f'{BOOKS_URL}{book}') as response:
        soup = BeautifulSoup(response.text, 'html.parser')
        name = soup.find('h1', class_='work-title')
        author = soup.find('a', itemprop="author")
        print(f'"{name.text}", {author.text}')
        new_time = round(time.time() - start, 2)
        print(new_time)


start = time.time()

for isbn in LIST_ISBN:
    main(isbn)

print(f'The task took: {round(time.time() - start, 2)} sec')
