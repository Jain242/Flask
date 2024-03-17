import threading
import os
import pathlib
import time

MY_PATH ='D:/123'

def searchfile(file_):
    full_path = os.path.join(MY_PATH, file_)
    with open (full_path, 'r', encoding='utf-8') as f:
        content = f.read()
        count = len(content.split())
        print(count)
        return count

    


start = time.time()
threads = []

for root, dirs, files in os.walk(MY_PATH):
    for file in files:
        t = threading.Thread(target=searchfile, args=(file,))
        threads.append(t)
        t.start()

for t in threads:
    t.join()

print(f'Вркмя выполнения {time.time() - start}')
