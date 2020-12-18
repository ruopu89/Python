import threading
import time

lock = threading.RLock()
print(lock.acquire())
print('------------------------------------')
print(lock.acquire(blocking=False))
print(lock.acquire())
print(lock.acquire(timeout=3.55))
print(lock.acquire(blocking=False))
lock.release()
lock.release()
lock.release()
lock.release()
print('main thread {}'.format(threading.current_thread().ident))
print("lock in main thread {}".format(lock))
lock.release()
print('=========================================')
print()

print(lock.acquire(blocking=False))
lock.release()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print()

print(lock.acquire())
def sub(l):
    print('{}: {}'.format(threading.current_thread(), l.acquire()))
    print('{}: {}'.format(threading.current_thread(), l.acquire(False)))
    print('lock in sub thread {}'.format(lock))
    l.release()
    print('sub 1')
    l.release()
    print('sub 2')

threading.Timer(2, sub, args=(lock,)).start()
print('+++++++++++++++++++++++++++++++++++++++')
print()

print(lock.acquire())
lock.release()
time.sleep(5)
print('释放主线程锁')
lock.release()