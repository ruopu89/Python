# import logging
# import datetime
# import threading
#
# logging.basicConfig(level=logging.INFO, format="%(thread)s %(message)s")
# start = datetime.datetime.now()
#
# def calc():
#     sum = 0
#     for _ in range(100000000):
#         sum += 1

# calc()
# calc()
# calc()
# calc()
# calc()

# t1 = threading.Thread(target=calc)
# t2 = threading.Thread(target=calc)
# t3 = threading.Thread(target=calc)
# t4 = threading.Thread(target=calc)
# t5 = threading.Thread(target=calc)
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
# t1.join()
# t2.join()
# t3.join()
# t4.join()
# t5.join()
#
# delta = (datetime.datetime.now() - start).total_seconds()
# logging.info(delta)
# =============================================================
import threading
import random
import logging
logging.basicConfig(level=logging.INFO, format="%(thread)s %(threadName)s %(message)s")
import datetime

def calc():
    sum = 0
    for _ in range(100000000):
        sum += 1

start = datetime.datetime.now()
lst = []

# calc()
# calc()
# calc()
# calc()
for _ in range(5):
    t = threading.Thread(target=calc)
    t.start()
    lst.append(t)

for t in lst:
    t.join()


delta = (datetime.datetime.now() - start).total_seconds()
print(delta)
