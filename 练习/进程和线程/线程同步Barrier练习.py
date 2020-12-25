# import threading
# import logging
#
# FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
# def worker(barrier:threading.Barrier):
#     logging.info('waiting for {} threads.'.format(barrier.n_waiting))
#     try:
#         barrier_id = barrier.wait()
#         logging.info('after barrier {}'.format(barrier_id))
#     except threading.BrokenBarrierError:
#         logging.info('Broken Barrier')
#
# barrier = threading.Barrier(3)
#
# for x in range(9):
#     threading.Thread(target=worker, name='worker-{}'.format(x), args=(barrier,)).start()
#
# logging.info('started')
# ==================================
# import threading
# import logging
#
# FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
# def worker(barrier:threading.Barrier):
#     logging.info('waiting for {} threads.'.format(barrier.n_waiting))
#     try:
#         barrier_id = barrier.wait()
#         logging.info('after barrier {}'.format(barrier_id))
#     except threading.BrokenBarrierError:
#         logging.info('Broken Barrier. run.')
#
# barrier = threading.Barrier(3)
#
# for x in range(0, 9):
#     if x == 2:
#         barrier.abort()
#     elif x == 6:
#         barrier.reset()
#     threading.Event().wait(1)
#     threading.Thread(target=worker, name='worker-{}'.format(x), args=(barrier,)).start()
# ==============================================
# wait方法超时实例
# 如果wait方法超时发生，屏障将处于broken状态，直到reset
# import threading
# import logging
#
# FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
# def worker(barrier:threading.Barrier, i:int):
#     logging.info('waiting for {} threads.'.format(barrier.n_waiting))
#     try:
#         logging.info(barrier.broken)
#         if i < 3:
#             barrier_id = barrier.wait(1)
#         else:
#             if i == 6:
#                 barrier.reset()
#             barrier_id = barrier.wait()
#         logging.info('after barrier {}'.format(barrier_id))
#     except threading.BrokenBarrierError:
#         logging.info('Broken Barrier. run.')
#
# barrier = threading.Barrier(3)
#
# for x in range(0, 9):
#     threading.Event().wait(2)
#     threading.Thread(target=worker, name='worker-{}'.format(x), args=(barrier, x)).start()
# ===================================================
# 凑够一波一起执行，凑多少个用`parties`参数指定
import threading
import logging
logging.basicConfig(level=logging.INFO, format="%(thread)d %(threadName)s %(message)s")

def work(barrier:threading.Barrier):
    logging.info("n_waiting = {}".format(barrier.n_waiting))
    try:
        bid = barrier.wait()
        logging.info("after barrier {}".format(bid))
    except threading.BrokenBarrierError:
        logging.info("Broken Barrier in {}".format(threading.current_thread().name))

barrier = threading.Barrier(3)

for x in range(5):
    threading.Thread(target=work, args=(barrier,)).start()
    # if x == 4:
    #     barrier.abort()