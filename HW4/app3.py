import random
import asyncio
import time

array = [random.randint(1, 100) for _ in range(1000000)]
RESULT = []

async def summer(arr, i):
    summa = sum(arr)
    global RESULT
    RESULT.append(summa)
    print(f'Сумма {i} задачи = {summa}')

async def main():
    PROCESSES = 10
    tasks = []

    start = time.time()

    for i in range(PROCESSES):
        s_ind = i * 100000
        e_ind = s_ind + 100000 if i < PROCESSES - 1 else len(array)
        task = asyncio.create_task(summer(array[s_ind:e_ind], i))
        tasks.append(task)

    await asyncio.gather(*tasks)

    print(f'Время работы кода: {time.time() - start}')
    print(f'Сумма равна: {sum(RESULT)}')

if __name__ == '__main__':
    asyncio.run(main())
