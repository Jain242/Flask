import random
import multiprocessing
import time

array = [random.randint(1, 100) for _ in range(1000000)]
RESULT =[]

def summer(arr, i):
    summa = sum(arr)
    global RESULT
    RESULT.append(summa)
    print(f'Сумма {i} процесса = {summa}')

if __name__ == '__main__':
    PROCESSES = 10
    processes = []

    start = time.time()

    for i in range(PROCESSES):
        s_ind = i * 100000
        e_ind = s_ind + 100000 if i < PROCESSES - 1 else len(array)
        p = multiprocessing.Process(target=summer, args=(array[s_ind:e_ind],i))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()

    print(f'Время работы кода: {time.time() - start}')
    print(f'Сумма равна: {sum(RESULT)}')
