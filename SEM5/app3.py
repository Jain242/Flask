import asyncio
import os
import aiofiles
import time

MY_PATH ='D:/123/'

async def searchfile(file_):
    full_path = os.path.join(MY_PATH, file_)
    async with aiofiles.open (full_path, 'r', encoding='utf-8') as f:
        content = await f.read()
        count = len(content.split())
        print(f'Слов в {file_} : {count}')

async def main():
    for root, dirs, files in os.walk(MY_PATH):
        for file in files:
            task = asyncio.create_task(searchfile(file))
            await task




if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    print(f'{time.time()  - start}')
