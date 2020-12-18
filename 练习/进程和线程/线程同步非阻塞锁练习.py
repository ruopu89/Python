import threading
import logging
import time

FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

def worker(tasks):
    for task in tasks:
        time.sleep(0.001)
        if task.lock.acquire(False):
            logging.info('{} {} begin to start'.format(threading.current_thread(), task.name))
        else:
            logging.info('{} {} is working'.format(threading.current_thread(), task.name))

class Task:
    def __init__(self, name):
        self.name = name
        self.lock = threading.Lock()

tasks = [Task('task-{}'.format(x)) for x in range(10)]

for i in range(5):
    threading.Thread(target=worker, name='worker-{}'.format(i), args=(tasks,)).start()