import threading
import multiprocessing
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


if __name__ == "__main__":
     
    
    start = time.time()
    multiprocess= []

    for root, dirs, files in os.walk(MY_PATH):
        for file in files:
            t = multiprocessing.Process(target=searchfile, args=(file,))
            multiprocess.append(t)
            t.start()
            

    for t in multiprocess:
        t.join()
    print(f'{time.time()  - start}')