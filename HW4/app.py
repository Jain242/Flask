import random
import threading
import time
array = [random.randint(1,100) for _ in range(1000000)]
RESULT =[]

def summer(arr,i):
    summa = sum(arr)
    global RESULT
    RESULT.append( summa)
    print(f'Сумма {i} потока = {summa} ')


THREADS = 10
threads = []

start= time.time()


for i in range(THREADS):
    s_ind = i*100000
    e_ind = s_ind + 100000 if i<THREADS-1 else len(array)
    t = threading.Thread(target=summer, args = (array[s_ind:e_ind],i,))
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()


print( f'Время работы кода:  {time.time() -start }')
print(f'Сумма равна: {sum(RESULT)}')